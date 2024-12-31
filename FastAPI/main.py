from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn
import cv2
import numpy as np
from joblib import load
import os

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ubah '*' ke domain tertentu untuk produksi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "knn_model.joblib")
if not os.path.exists(model_path):
    raise FileNotFoundError("Model file not found. Ensure knn_model.joblib is available.")

knn_model = load(model_path)

@app.get("/")
async def health_check():
    return "The health check is successful!"
    
# Function to preprocess image and extract HSV features
def extract_hsv_features_from_image(image_bytes):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Failed to decode image.")
    img_resized = cv2.resize(img, (100, 100))
    hsv_img = cv2.cvtColor(img_resized, cv2.COLOR_BGR2HSV)
    h_mean = np.mean(hsv_img[:, :, 0])
    s_mean = np.mean(hsv_img[:, :, 1])
    v_mean = np.mean(hsv_img[:, :, 2])
    return [[h_mean, s_mean, v_mean]]

# API endpoint for image classification
@app.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    try:
        if not file.filename.lower().endswith((".jpg", ".jpeg", ".png")):
            raise HTTPException(status_code=400, detail="Invalid file type. Please upload a JPG or PNG image.")
        image_bytes = await file.read()
        hsv_features = extract_hsv_features_from_image(image_bytes)
        prediction = knn_model.predict(hsv_features)
        label_mapping = {0: "Tidak Matang", 1: "Matang"}
        result = label_mapping.get(prediction[0], "Unknown")
        return JSONResponse(content={"prediction": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
