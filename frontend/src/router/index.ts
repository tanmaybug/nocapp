import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import useAuthStore, { ROLE } from '@/modules/auth/stores'
import authRoutes from '@/modules/auth/auth.routes'
import departmentRoutes from '@/modules/department/department.routes'
import institutionRoutes from '@/modules/institution/institution.routes'
import { authGuard } from './guards'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    beforeEnter: authGuard,
    redirect: () => ({ name: 'Dashboard', replace: true }),
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    beforeEnter: authGuard,
    redirect: () => {
      const store = useAuthStore()
      switch (store.role) {
        case ROLE.INSTITUTION:
          return { name: 'InstitutionDashboard', replace: true }
        case ROLE.DEPARTMENT:
          return { name: 'DepartmentDashboard', replace: true }
        default:
          return { name: 'NotFound', replace: true }
      }
    },
  },
  authRoutes,
  departmentRoutes,
  institutionRoutes,
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('./NotFound.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})
export default router
