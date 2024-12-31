<template>
    <div class="about-us">
      <h1>About Us</h1>
      <p>
        Aplikasi ini menggunakan teknologi pengenalan citra untuk memprediksi tingkat
        kematangan buah apel berdasarkan warna HSV dan algoritma KNN.
        Sistem prediksi ini juga sangat bergantung oleh data yang ada pada dataset, oleh karena itu jika data gambar yang dimasukkan tidak sesuai,
        maka efektifitas atau akurasi dari sistem prediksi ini juga akan menurun.
      </p>
    </div>
  </template>
  
  <script>
  export default {
    name: "AboutUs",
  };
  </script>
  
  <style>
  .about-us {
    text-align: center;
    margin: 30px auto;
    max-width: 500px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    background-color: #f9f9f9;
    font-family: Arial, sans-serif;
  }
  
  h1 {
    color: #333;
  }
  
  p {
    margin-top: 20px;
    font-size: 18px;
    color: #555;
  }
  </style>
  