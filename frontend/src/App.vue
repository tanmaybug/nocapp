<script setup lang="ts">
import DialogBox from '@/components/common/DialogBox.vue'
</script>

<template>
  <v-app>
    <router-view />
  </v-app>
  <DialogBox />
</template>

<style scoped>
body {
  margin: 0
}
</style>
