// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss',     '@nuxt/icon',],
  runtimeConfig: {

    public: {
      BACKEND_URL: "http://127.0.0.1:5000"
    }
  },
})
