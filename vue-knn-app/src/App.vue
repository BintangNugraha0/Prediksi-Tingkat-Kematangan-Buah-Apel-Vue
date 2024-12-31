<template>
  <div id="app">
    <header>
      <nav>
        <router-link to="/">Home</router-link>
        <span class="separator">|</span>
        <router-link to="/about">About Us</router-link>
      </nav>
    </header>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: "App",
  mounted() {
    // Tambahkan listener resize untuk mengubah layout jika diperlukan
    window.addEventListener("resize", this.handleResize);
    this.handleResize(); // Pastikan layout sesuai saat pertama kali dimuat
  },
  beforeUnmount() {
    // Hapus listener resize saat komponen dihancurkan
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    handleResize() {
      const width = window.innerWidth;
      console.log(`Current width: ${width}px`);
      // Anda dapat menambahkan logika tambahan di sini jika ingin mengatur ulang layout secara dinamis
    },
  },
};
</script>

<style>
/* Global Styles */
body {
  margin: 0;
  font-family: 'Source Sans Pro', sans-serif;
  background: linear-gradient(135deg, #161616, #4f4d5a);
  padding: 0;
}

#app {
  text-align: center;
  min-height: 100vh; /* Pastikan elemen mengambil tinggi penuh */
  display: flex;
  flex-direction: column;
}

/* Header Styles */
header {
  background-color: #333;
  padding: 15px;
  color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: sticky; /* Buat header tetap di atas saat scroll */
  top: 0;
  z-index: 1000;
}

nav {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
}

nav a {
  color: white;
  text-decoration: none;
  font-size: 1rem;
  padding: 5px 10px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

nav a:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

/* Pemisah di antara link */
.separator {
  color: white;
  margin: 0 5px;
  display: inline-block;
}

/* Main Content Styles */
main {
  flex: 1; /* Pastikan main konten fleksibel */
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

/* Responsive Design */
@media (max-width: 768px) {
  nav {
    flex-direction: column;
  }

  .separator {
    display: none; /* Sembunyikan pemisah pada perangkat kecil */
  }

  nav a {
    font-size: 0.9rem;
    padding: 8px;
  }
}

@media (max-width: 400px) {
  #app {
    padding: 5px; /* Kurangi padding untuk aplikasi */
  }

  header {
    padding: 10px; /* Header lebih kecil di perangkat kecil */
  }

  nav a {
    font-size: 0.8rem; /* Font lebih kecil */
  }

  main {
    flex-direction: column; /* Susunan kolom untuk konten */
  }
}
</style>
