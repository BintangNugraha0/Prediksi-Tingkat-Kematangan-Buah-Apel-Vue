import { createRouter, createWebHistory } from 'vue-router';
import ImageUploader from '../components/ImageUploader.vue';
import AboutUs from '../components/AboutUs.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: ImageUploader,
  },
  {
    path: '/about',
    name: 'AboutUs',
    component: AboutUs,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
