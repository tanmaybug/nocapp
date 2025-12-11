import useAuthStore, { type Role } from "@/stores/authStore"
import { storeToRefs } from "pinia"
import type { NavigationGuardNext, RouteLocationNormalizedGeneric, RouteLocationNormalizedLoadedGeneric } from "vue-router"

export default (to: RouteLocationNormalizedGeneric, _form: RouteLocationNormalizedLoadedGeneric, next: NavigationGuardNext) => {
  const { isAuthenticated, role } = storeToRefs(useAuthStore())
  if (isAuthenticated.value && role.value){
    if ((to.meta?.roles as Role[])?.includes(role.value) === false) {
      return next({ name: 'NotFound', replace: true })
    }
    return next()
  }
  return next({ name: 'Login', replace: true })
}
