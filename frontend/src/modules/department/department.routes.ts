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
      path: 'noc-applications',
      redirect: () => ({ name: 'DepartmentNOCApplications', params: { type: 'pending' }, replace: true }),
    },
    {
      path: 'noc-applications/:type',
      name: 'DepartmentNOCApplications',
      component: () => import('./pages/NOCApplicationsPage.vue')
    },
     {
      path: 'noc-applications-pending',
      name: 'DepartmentNOCApplicationsPending',
      redirect: () => ({ name: 'DepartmentNOCApplications', params: { type: 'pending' }, replace: true }),
    },
    {
      path: 'noc-applications-inprocess',
      name: 'DepartmentNOCApplicationsInProcess',
      redirect: () => ({ name: 'DepartmentNOCApplications', params: { type: 'in-process' }, replace: true }),
    },
    {
      path: 'noc-applications-completed',
      name: 'DepartmentNOCApplicationsCompleted',
      redirect: () => ({ name: 'DepartmentNOCApplications', params: { type: 'completed' }, replace: true }),
    },
  ],
}

export default adminRoutes
