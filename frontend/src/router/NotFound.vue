<template>
  <div class="page not-found-view">
    <v-container class="pa-6" style="max-width:800px; text-align:center">
      <v-card>
        <v-card-title class="text-h5">404 — Page not found</v-card-title>
        <v-card-text>
          The page you are looking for does not exist.
        </v-card-text>
        <v-card-actions class="justify-center">
          <v-btn text to="/">Go to Home</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped></style>
