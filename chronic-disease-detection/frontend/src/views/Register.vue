<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Create an account
        </h2>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="register">
        <div class="rounded-md shadow-sm space-y-4">
          <div>
            <label for="email" class="sr-only">Email address</label>
            <input
              id="email"
              v-model="email"
              name="email"
              type="email"
              autocomplete="email"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
              placeholder="Email address"
            >
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              id="password"
              v-model="password"
              name="password"
              type="password"
              autocomplete="new-password"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
              placeholder="Password"
            >
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            :disabled="isLoading"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
              <i class="fas fa-user-plus" :class="{'opacity-0': isLoading}"></i>
              <i class="fas fa-spinner fa-spin" :class="{'opacity-0': !isLoading}"></i>
            </span>
            <span v-if="!isLoading">Register</span>
            <span v-else>Registering...</span>
          </button>
        </div>
      </form>
      
      <div class="text-center text-sm text-gray-600">
        <p>Already have an account? <router-link to="/login" class="text-blue-600 hover:text-blue-500">Login</router-link></p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../store/auth'

export default {
  name: 'RegisterView',
  setup() {
    const email = ref('')
    const password = ref('')
    const isLoading = ref(false)
    const router = useRouter()
    const authStore = useAuthStore()

    const register = async () => {
      isLoading.value = true
      try {
        // In a real app, this would call your registration API
        // await authStore.register({ email: email.value, password: password.value })
        // For now, we'll simulate successful registration
        await new Promise(resolve => setTimeout(resolve, 1000))
        router.push('/login')
      } catch (error) {
        console.error('Registration failed:', error)
        alert('Failed to register. Please try again.')
      } finally {
        isLoading.value = false
      }
    }

    return {
      email,
      password,
      isLoading,
      register
    }
  }
}
</script>