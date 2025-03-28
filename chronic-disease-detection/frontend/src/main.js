import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import pinia from './store'
import axios from 'axios'
import './styles/tailwind.css'
import '@fortawesome/fontawesome-free/css/all.min.css'

// Set base API URL
axios.defaults.baseURL = process.env.VUE_APP_API_URL || 'http://localhost:8000'

const app = createApp(App)

app.use(router)
app.use(pinia)

// Global error handler
app.config.errorHandler = (err) => {
  console.error('Vue error:', err)
}

app.mount('#app')
