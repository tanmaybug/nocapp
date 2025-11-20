<script setup lang="ts">
import AppHeader from '@/components/AppHeader.vue'
import DialogBox from '@/components/DialogBox.vue';
</script>

<template>
  <v-app>
    <AppHeader />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
  <DialogBox />
</template>

<style scoped>
body {
  margin: 0
}
</style>
