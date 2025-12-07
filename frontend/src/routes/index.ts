import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import auth from './guards/auth'
import guest from './guards/guest'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    redirect: () => ({ name: 'Dashboard', replace: true }),
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    beforeEnter: auth,
    component: () => import('../views/DashboardView.vue'),
  },
  {
    path: '/registration',
    name: 'Registration',
    beforeEnter: guest,
    component: () => import('../views/RegistrationView.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    beforeEnter: guest,
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
