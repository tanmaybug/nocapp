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
     {
      path: 'pending-noc-applications',
      name: 'DepartmentPendingNOCApplications',
      component: () => import('./pages/PendingNOCApplicationsPage.vue')
    },
    {
      path: 'inprocess-noc-applications',
      name: 'DepartmentInProcessNOCApplications',
      component: () => import('./pages/InProcessNOCApplicationsPage.vue')
    },
    {
      path: 'completed-noc-applications',
      name: 'DepartmentCompletedNOCApplications',
      component: () => import('./pages/CompletedNOCApplicationsPage.vue')
    },
  ],
}

export default adminRoutes
