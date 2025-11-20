import useAuthStore from '@/stores/authStore'
import { storeToRefs } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import auth from './guards/auth'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/HomeView.vue'),
  },
  {
    path: '/registration',
    name: 'Registration',
    component: () => import('../views/RegistrationView.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/LoginView.vue'),
  },
  {
    path: '/noc-application',
    name: 'NOCApplication',
    component: () => import('../views/NOCApplicationView.vue'),
    beforeEnter: auth,
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/NotFound.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})
export default router
