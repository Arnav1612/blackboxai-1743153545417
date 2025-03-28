<template>
  <main class="container mx-auto px-4 py-8">
    <div class="max-w-3xl mx-auto">
      <h1 class="text-3xl font-bold mb-6">About Chronic Disease Detection</h1>
      
      <div class="prose max-w-none">
        <section class="mb-8">
          <h2 class="text-2xl font-semibold mb-4">Our Mission</h2>
          <p class="mb-4">
            The Chronic Disease Detection System is designed to assist healthcare professionals in early identification 
            of patients at risk for chronic diseases including diabetes, cardiovascular conditions, and cancer.
          </p>
          <p>
            By leveraging machine learning algorithms on patient health data, we provide accurate risk assessments 
            that can inform preventive care strategies.
          </p>
        </section>
        
        <section class="mb-8">
          <h2 class="text-2xl font-semibold mb-4">Technology</h2>
          <p class="mb-4">
            Our system utilizes state-of-the-art machine learning models including:
          </p>
          <ul class="list-disc pl-6 mb-4">
            <li>Random Forest Classifiers</li>
            <li>Gradient Boosting Machines</li>
            <li>Neural Networks</li>
          </ul>
          <p>
            We incorporate explainable AI techniques like SHAP and LIME to provide transparent insights into model predictions.
          </p>
        </section>
        
        <section class="mb-8">
          <h2 class="text-2xl font-semibold mb-4">Data Privacy</h2>
          <p class="mb-4">
            We take patient privacy and data security seriously. Our system is designed to be fully compliant with:
          </p>
          <ul class="list-disc pl-6 mb-4">
            <li>HIPAA (Health Insurance Portability and Accountability Act)</li>
            <li>GDPR (General Data Protection Regulation)</li>
          </ul>
          <p>
            All patient data is encrypted both in transit and at rest, with strict access controls.
          </p>
        </section>
        
        <section>
          <h2 class="text-2xl font-semibold mb-4">Development Team</h2>
          <p>
            This system was developed by a team of machine learning engineers, healthcare professionals, 
            and software developers committed to improving patient outcomes through technology.
          </p>
        </section>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: 'AboutView'
}
</script>

<style scoped>
.prose h2 {
  @apply text-blue-600;
}
</style>