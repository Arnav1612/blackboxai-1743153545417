<template>
  <nav class="bg-blue-600 text-white shadow-lg">
    <div class="container mx-auto px-4 py-3 flex justify-between items-center">
      <div class="flex items-center space-x-4">
        <router-link to="/" class="text-xl font-bold">Chronic Disease Detection</router-link>
      </div>
      <div class="flex items-center space-x-6">
        <router-link 
          v-for="route in routes" 
          :key="route.path" 
          :to="route.path"
          class="hover:text-blue-200 transition-colors"
          active-class="text-blue-200 font-medium"
        >
          {{ route.name }}
        </router-link>
        <button 
          v-if="isAuthenticated"
          @click="logout"
          class="hover:text-blue-200 transition-colors"
        >
          Logout
        </button>
      </div>
    </div>
  </nav>
</template>

<script>
import { useAuthStore } from '../store/auth'
import { storeToRefs } from 'pinia'

export default {
  name: 'NavBar',
  data() {
    return {
      routes: [
        { path: '/', name: 'Home' },
        { path: '/predict', name: 'Predict' },
        { path: '/about', name: 'About' }
      ]
    }
  },
  setup() {
    const authStore = useAuthStore()
    const { isAuthenticated } = storeToRefs(authStore)
    
    const logout = () => {
      authStore.logout()
    }

    return { isAuthenticated, logout }
  }
}
</script>
