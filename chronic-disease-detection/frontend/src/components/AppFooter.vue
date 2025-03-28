<template>
  <footer class="bg-gray-800 text-white py-6 mt-auto">
    <div class="container mx-auto px-4">
      <div class="flex flex-col md:flex-row justify-between items-center">
        <div class="mb-4 md:mb-0">
          <h3 class="text-xl font-bold">Chronic Disease Detection</h3>
          <p class="text-gray-400 mt-2">Helping healthcare professionals make better decisions</p>
        </div>
        <div class="flex space-x-6">
          <a href="#" class="hover:text-blue-400 transition-colors">
            <i class="fab fa-github text-2xl"></i>
          </a>
          <a href="#" class="hover:text-blue-400 transition-colors">
            <i class="fab fa-twitter text-2xl"></i>
          </a>
          <a href="#" class="hover:text-blue-400 transition-colors">
            <i class="fab fa-linkedin text-2xl"></i>
          </a>
        </div>
      </div>
      <div class="border-t border-gray-700 mt-6 pt-6 text-center text-gray-400">
        <p>&copy; 2023 Chronic Disease Detection System. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter'
}
</script>

<style scoped>
footer {
  box-shadow: 0 -4px 6px -1px rgba(0, 0, 0, 0.1);
}
</style>