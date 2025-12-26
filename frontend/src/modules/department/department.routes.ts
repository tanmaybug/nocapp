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
      path: 'noc-applications', // Redirect to default type 'pending'
      redirect: () => ({ name: 'DepartmentNOCApplications', params: { type: 'pending' }, replace: true }),
    },
    {
      path: 'noc-applications/type/:type',
      name: 'DepartmentNOCApplications',
      component: () => import('./pages/NOCApplicationsPage.vue')
    },
     {
      path: 'noc-applications/:registrationId',
      name: 'DepartmentNOCProfileView',
      component: () => import('./pages/NOCProfileViewPage.vue')
    }
  ],
}

export default adminRoutes
