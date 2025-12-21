import type { RouteRecordRaw } from 'vue-router'
import { authGuard } from '@/router/guards'
import InstitutionLayout from '@/layouts/InstitutionLayout.vue'
import { ROLE } from '@/modules/auth/stores'

const institutionRoutes: RouteRecordRaw = {
  path: '/institution',
  component: InstitutionLayout,
  beforeEnter: authGuard,
  meta: { roles: [ROLE.INSTITUTION] },
  children: [
    {
      path: 'dashboard',
      name: 'InstitutionDashboard',
      component: () => import('./pages/DashboardPage.vue'),
    },
    {
      path: 'noc-application',
      name: 'NOCApplication',
      component: () => import('./pages/NOCApplicationPage.vue'),
    },
  ],
}

export default institutionRoutes
