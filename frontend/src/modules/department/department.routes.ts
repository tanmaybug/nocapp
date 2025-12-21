import type { RouteRecordRaw } from 'vue-router'
import { authGuard } from '@/router/guards'
import DepartmentLayout from '@/layouts/DepartmentLayout.vue'
import { ROLE } from '@/modules/auth/stores'

const adminRoutes: RouteRecordRaw = {
  path: '/department',
  component: DepartmentLayout,
  beforeEnter: authGuard,
  meta: { roles: [ROLE.DEPARTMENT] },
  children: [
    {
      path: 'dashboard',
      name: 'DepartmentDashboard',
      component: () => import('./pages/DashboardPage.vue')
    },
  ],
}

export default adminRoutes
