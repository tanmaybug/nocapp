import type { RouteRecordRaw } from 'vue-router'
import { guestGuard } from '@/router/guards'
import AuthLayout from '@/layouts/AuthLayout.vue'

const authRoutes: RouteRecordRaw = {
  path: '/',
  component: AuthLayout,
  children: [
    {
      path: 'login',
      name: 'Login',
      beforeEnter: guestGuard,
      component: () => import('./pages/LoginPage.vue'),
    },
    {
      path: 'registration',
      name: 'Registration',
      beforeEnter: guestGuard,
      component: () => import('./pages/RegistrationPage.vue'),
    },
  ],
}

export default authRoutes
