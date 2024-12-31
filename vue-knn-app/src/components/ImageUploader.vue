<template>
  <div class="image-uploader">
    <h2>Prediksi Tingkat Kematangan Buah Apel 
      menggunakan Algoritma KNN dan Ekstraksi warna HSV </h2>

    <!-- Deskripsi tambahan -->
    <p class="instructions">
      Unggah gambar apel untuk memprediksi tingkat kematangannya. Pastikan gambar jelas dan format file sesuai (JPG/PNG).
    </p>

    <!-- Input file untuk mengunggah gambar -->
    <div class="upload-section">
      <input type="file" @change="handleFileUpload" accept="image/*" />
      <!-- Tombol prediksi muncul di bawah gambar -->
      <button v-if="selectedFile" @click="submitImage">Upload & Prediksi</button>
      <!-- Tombol reset -->
      <button v-if="selectedFile" @click="reset" class="reset-button">Reset</button>
    </div>

    <!-- Indikator loading -->
    <div v-if="loading" class="loading">
      <p>Memproses gambar, harap tunggu...</p>
    </div>

    <!-- Tampilkan gambar yang diunggah -->
    <div v-if="previewImage" class="image-preview">
      <h3>Gambar yang Diunggah:</h3>
      <img :src="previewImage" alt="Uploaded Image" />
    </div>

    <!-- Hasil prediksi -->
    <div v-if="prediction" class="result">
      <h3>Hasil Prediksi:</h3>
      <p>{{ prediction }}</p>
    </div>

    <!-- Error handling -->
    <div v-if="error" class="error">
      <p>{{ error }}</p>
    </div>

    <!-- Footer -->
    <footer class="footer">
      <p>© 2024 Prediksi Kematangan Apel | Dibuat oleh [Nama Anda]</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      selectedFile: null,
      previewImage: null,
      prediction: null,
      error: null,
      loading: false, // Tambahkan ini
    };
  },
  methods: {
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0];
      if (this.selectedFile) {
        // Buat preview gambar
        this.previewImage = URL.createObjectURL(this.selectedFile);
      }
    },
    async submitImage() {
      if (!this.selectedFile) {
        this.error = "Silakan pilih gambar terlebih dahulu.";
        return;
      }

      this.error = null;
      this.prediction = null;
      this.loading = true; // Aktifkan loading

      const formData = new FormData();
      formData.append("file", this.selectedFile);

      try {
        const response = await axios.post("http://127.0.0.1:8000/classify", formData, {
          headers: { "Content-Type": "multipart/form-data" },
        });
        this.prediction = response.data.prediction;
      } catch (err) {
        this.error = err.response?.data?.detail || "Terjadi kesalahan saat memproses gambar.";
      } finally {
        this.loading = false; // Nonaktifkan loading
      }
    },
    reset() {
      this.selectedFile = null;
      this.previewImage = null;
      this.prediction = null;
      this.error = null;
    },
  },
};
</script>

<style>
.image-uploader {
  text-align: center;
  margin: 20px auto;
  max-width: 90%; /* Gunakan max-width 90% untuk perangkat kecil */
  padding: 15px; /* Padding lebih kecil */
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #f9f9f9;
  font-family: Arial, sans-serif;
}

h2 {
  color: #333;
  margin-bottom: 20px;
}

.instructions {
  font-size: 14px;
  color: #666;
  margin-bottom: 10px;
}

.upload-section {
  margin-bottom: 20px;
}

.upload-section input {
  margin-bottom: 10px; /* Ruang antara input dan tombol */
  max-width: 100%; /* Input tidak melebihi lebar kontainer */
}

button {
  padding: 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-left: 5px;
}

button:hover {
  background-color: #45a049;
}

.reset-button {
  margin-top: 10px;
  padding: 10px;
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.reset-button:hover {
  background-color: #d32f2f;
}

.loading {
  margin-top: 20px;
  color: #4caf50;
  font-size: 16px;
  font-weight: bold;
}

.image-preview {
  margin: 20px 0;
}

.image-preview img {
  max-width: 100%;
  height: auto;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

.result {
  margin-top: 20px;
  font-size: 18px;
  color: #333;
}

.error {
  color: white;
  background-color: #f44336;
  padding: 10px;
  border-radius: 5px;
  margin-top: 10px;
  font-size: 14px;
}

.footer {
  margin-top: 20px;
  padding: 10px 0;
  text-align: center;
  background-color: #f1f1f1;
  color: #555;
  font-size: 14px;
}

@media (max-width: 768px) {
  .image-uploader {
    max-width: 95%;
  }

  h2 {
    font-size: 18px;
  }

  .upload-section input {
    font-size: 14px;
  }

  button {
    font-size: 14px;
    padding: 8px 12px;
  }
}


@media (max-width: 400px) {
  .image-uploader {
    padding: 10px; /* Padding lebih kecil untuk perangkat kecil */
  }

  button {
    width: 100%; /* Full width pada perangkat kecil */
  }

  .image-preview img {
    max-width: 100%; /* Gambar sepenuhnya fleksibel */
    height: auto; /* Pastikan proporsi gambar tetap */
  }
}
</style>
