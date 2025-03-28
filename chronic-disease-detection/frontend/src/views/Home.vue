<template>
  <main class="flex-grow">
    <section class="hero bg-blue-50 py-20">
      <div class="container mx-auto px-4 text-center">
        <h1 class="text-4xl md:text-5xl font-bold text-blue-800 mb-6">
          Chronic Disease Detection System
        </h1>
        <p class="text-xl text-gray-600 max-w-2xl mx-auto mb-8">
          Advanced machine learning models to help healthcare professionals assess patient risks
        </p>
        <router-link 
          to="/predict" 
          class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition-colors"
        >
          Get Started
        </router-link>
      </div>
    </section>

    <section class="features py-16">
      <div class="container mx-auto px-4">
        <h2 class="text-3xl font-bold text-center mb-12">Key Features</h2>
        <div class="grid md:grid-cols-3 gap-8">
          <div class="feature-card p-6 rounded-lg shadow-md">
            <div class="text-blue-500 mb-4">
              <i class="fas fa-chart-line text-4xl"></i>
            </div>
            <h3 class="text-xl font-semibold mb-3">Accurate Predictions</h3>
            <p class="text-gray-600">
              Our models achieve over 90% accuracy in detecting chronic disease risks.
            </p>
          </div>
          <div class="feature-card p-6 rounded-lg shadow-md">
            <div class="text-blue-500 mb-4">
              <i class="fas fa-shield-alt text-4xl"></i>
            </div>
            <h3 class="text-xl font-semibold mb-3">HIPAA Compliant</h3>
            <p class="text-gray-600">
              All patient data is encrypted and securely stored.
            </p>
          </div>
          <div class="feature-card p-6 rounded-lg shadow-md">
            <div class="text-blue-500 mb-4">
              <i class="fas fa-lightbulb text-4xl"></i>
            </div>
            <h3 class="text-xl font-semibold mb-3">Explainable AI</h3>
            <p class="text-gray-600">
              Understand model decisions with SHAP and LIME explanations.
            </p>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
export default {
  name: 'HomeView'
}
</script>

<style scoped>
.hero {
  background-image: linear-gradient(to bottom, rgba(239, 246, 255, 0.9), rgba(219, 234, 254, 0.9));
}

.feature-card {
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}
</style>