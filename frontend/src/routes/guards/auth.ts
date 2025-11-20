import useAuthStore from "@/stores/authStore"
import { storeToRefs } from "pinia"
import type { NavigationGuardNext, RouteLocationNormalizedGeneric, RouteLocationNormalizedLoadedGeneric } from "vue-router"

export default (_to: RouteLocationNormalizedGeneric, _form: RouteLocationNormalizedLoadedGeneric, next: NavigationGuardNext) => {
  const { isAuthenticated } = storeToRefs(useAuthStore())
  if (isAuthenticated.value) {
    return next()
  }
  return next({ name: 'Login', replace: true })
}
