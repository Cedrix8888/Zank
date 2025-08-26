import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import { API_CONFIG } from './config'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
  ],
  server: {
    proxy: {
      '/api': {
      target: API_CONFIG.baseUrl,
      changeOrigin: true,
      }
    },
    allowedHosts: [
      "gpu-t4-hm-12l9p99kyrux1.asia-east1-c.c.codatalab-user-runtimes.internal",
      "localhost",
      "127.0.0.1"
    ]
  },
})
