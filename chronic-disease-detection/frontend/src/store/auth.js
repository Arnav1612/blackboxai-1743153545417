import { defineStore } from 'pinia'
import axios from 'axios'
import router from '../router'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null
  }),
  getters: {
    isAuthenticated: (state) => !!state.token
  },
  actions: {
    async login({ email, password }) {
      try {
        const response = await axios.post('/api/auth/login', {
          email,
          password
        })
        
        this.token = response.data.token
        this.user = response.data.user
        localStorage.setItem('token', this.token)
        
        router.push('/')
        return true
      } catch (error) {
        console.error('Login failed:', error)
        return false
      }
    },
    async logout() {
      this.token = null
      this.user = null
      localStorage.removeItem('token')
      router.push('/login')
    },
    async checkAuth() {
      if (!this.token) return false
      
      try {
        const response = await axios.get('/api/auth/me', {
          headers: {
            Authorization: `Bearer ${this.token}`
          }
        })
        this.user = response.data.user
        return true
      } catch (error) {
        this.logout()
        return false
      }
    }
  }
})