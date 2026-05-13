<template>
  <div class="page fill-height d-flex align-center justify-center login-view position-relative overflow-hidden">
    <login-form width="500" />
  </div>
</template>

<script setup lang="ts">
import LoginForm from '../components/LoginForm.vue'
</script>

<style scoped>
.login-view::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url('@/assets/login-background.jpg');
  background-size: cover;
  background-position: center;
  filter: blur(5px);
  transform: scale(1.05);
  z-index: 0;
}

.login-view>* {
  position: relative;
  z-index: 1;
}
</style>