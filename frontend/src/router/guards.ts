import { storeToRefs } from 'pinia'
import type { NavigationGuardNext, RouteLocationNormalizedLoaded, RouteLocationNormalized } from 'vue-router'
import useAuthStore, { type Role } from '@/modules/auth/stores'

export function authGuard(
  to: RouteLocationNormalized,
  _from: RouteLocationNormalizedLoaded,
  next: NavigationGuardNext,
) {
  const { isAuthenticated, role } = storeToRefs(useAuthStore())

  if (isAuthenticated.value && role.value) {
    if ((to.meta?.roles as Role[] | undefined)?.includes(role.value) === false) {
      return next({ name: 'NotFound', replace: true })
    }
    return next()
  }

  return next({ name: 'Login', replace: true })
}

export function guestGuard(
  _to: RouteLocationNormalized,
  _from: RouteLocationNormalizedLoaded,
  next: NavigationGuardNext,
) {
  const { isAuthenticated } = storeToRefs(useAuthStore())
  if (!isAuthenticated.value) {
    return next()
  }
  return next({ name: 'Home', replace: true })
}
