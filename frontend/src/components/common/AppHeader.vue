<template>
  <v-app-bar color="primary" dark elevated>
    <v-app-bar-nav-icon class="d-md-none" @click="drawer = !drawer" />
    <v-toolbar-title class="ms-2"><v-btn text to="/">NOC Portal</v-btn></v-toolbar-title>
    <v-spacer />

    <!-- Desktop / tablet nav buttons -->
    <div class="d-none d-md-flex">
      <template v-if="isAuthenticated">
        <v-btn class="me-2" text @click="logout()" v-if="isAuthenticated">Log Out</v-btn>
      </template>
      <template v-else>
        <v-btn class="me-2" text :to="{ name: 'Registration' }" v-if="!isAuthenticated">Registration</v-btn>
        <v-btn class="me-2" text :to="{ name: 'Login' }" v-if="!isAuthenticated">Login</v-btn>
      </template>
    </div>
  </v-app-bar>

  <!-- Mobile drawer (only visible on small screens) -->
  <v-navigation-drawer v-model="drawer" temporary class="d-md-none">
    <v-list>
      <v-list-item :to="{ name: 'Registration' }" @click="drawer = false" v-if="!isAuthenticated">
        <v-list-item-title>Registration</v-list-item-title>
      </v-list-item>
      <v-list-item :to="{ name: 'Login' }" @click="drawer = false" v-if="!isAuthenticated">
        <v-list-item-title>Login</v-list-item-title>
      </v-list-item>
      <v-list-item :to="{ name: 'NOCApplication' }" @click="drawer = false" v-if="isAuthenticated">
        <v-list-item-title>NOC Application</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script setup lang="ts">
import router from '@/router'
import useAuthStore from '@/modules/auth/stores'
import { storeToRefs } from 'pinia'
import { ref } from 'vue'

const drawer = ref(false)
const authStore = useAuthStore()
const { isAuthenticated } = storeToRefs(authStore)
const logout = () => {
  authStore.logout()
  router.push({ name: 'Login' })
}
</script>

<style scoped></style>
