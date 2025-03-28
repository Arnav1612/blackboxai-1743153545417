<template>
  <main class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-8">Chronic Disease Risk Assessment</h1>
    
    <div class="grid md:grid-cols-2 gap-8">
      <!-- Patient Input Form -->
      <div class="bg-white rounded-lg shadow-md p-6">
        <h2 class="text-xl font-semibold mb-4">Patient Information</h2>
        
        <form @submit.prevent="submitForm">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
            <div v-for="field in formFields" :key="field.name">
              <label class="block text-gray-700 mb-2">{{ field.label }}</label>
              <input
                v-model="formData[field.name]"
                :type="field.type"
                :step="field.step"
                class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                required
              >
            </div>
          </div>
          
          <button
            type="submit"
            class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded-lg transition-colors"
            :disabled="isLoading"
          >
            <span v-if="!isLoading">Assess Risk</span>
            <span v-else>Processing...</span>
          </button>
        </form>
      </div>
      
      <!-- Results Panel -->
      <div class="bg-white rounded-lg shadow-md p-6">
        <h2 class="text-xl font-semibold mb-4">Assessment Results</h2>
        
        <div v-if="results" class="space-y-6">
          <div class="p-4 rounded-lg" :class="riskClass">
            <h3 class="text-lg font-bold mb-2">Diabetes Risk</h3>
            <div class="flex items-center justify-between mb-2">
              <span>Probability:</span>
              <span class="font-bold">{{ (results.probability * 100).toFixed(1) }}%</span>
            </div>
            <div class="flex items-center justify-between">
              <span>Risk Level:</span>
              <span class="font-bold">{{ results.risk_level }}</span>
            </div>
          </div>
          
          <div v-if="results.explanation" class="bg-gray-50 p-4 rounded-lg">
            <h3 class="text-lg font-bold mb-2">Key Factors</h3>
            <ul class="space-y-2">
              <li v-for="(factor, index) in results.explanation" :key="index" class="flex justify-between">
                <span>{{ factor.feature }}:</span>
                <span :class="{'text-green-600': factor.impact > 0, 'text-red-600': factor.impact < 0}">
                  {{ factor.impact > 0 ? 'Increases' : 'Decreases' }} risk by {{ Math.abs(factor.impact).toFixed(1) }}%
                </span>
              </li>
            </ul>
          </div>
        </div>
        
        <div v-else class="text-center py-12 text-gray-500">
          <i class="fas fa-chart-line text-4xl mb-4"></i>
          <p>Submit patient information to get risk assessment results</p>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  name: 'PredictView',
  setup() {
    const formFields = [
      { name: 'age', label: 'Age (years)', type: 'number' },
      { name: 'bmi', label: 'BMI', type: 'number', step: '0.1' },
      { name: 'glucose', label: 'Glucose (mg/dL)', type: 'number' },
      { name: 'blood_pressure', label: 'Blood Pressure (mmHg)', type: 'number' },
      { name: 'skin_thickness', label: 'Skin Thickness (mm)', type: 'number' },
      { name: 'insulin', label: 'Insulin (μU/mL)', type: 'number' },
      { name: 'pregnancies', label: 'Pregnancies', type: 'number' },
      { name: 'diabetes_pedigree', label: 'Diabetes Pedigree', type: 'number', step: '0.001' }
    ]

    const formData = ref(Object.fromEntries(formFields.map(f => [f.name, ''])))
    const results = ref(null)
    const isLoading = ref(false)

    const riskClass = computed(() => {
      if (!results.value) return ''
      const risk = results.value.probability
      if (risk < 0.3) return 'bg-green-100 text-green-800'
      if (risk < 0.7) return 'bg-yellow-100 text-yellow-800'
      return 'bg-red-100 text-red-800'
    })

    const submitForm = async () => {
      isLoading.value = true
      try {
        const response = await axios.post('/predictions/diabetes', formData.value)
        results.value = response.data
      } catch (error) {
        console.error('Prediction failed:', error)
        alert('Failed to get prediction. Please try again.')
      } finally {
        isLoading.value = false
      }
    }

    return {
      formFields,
      formData,
      results,
      isLoading,
      riskClass,
      submitForm
    }
  }
}
</script>