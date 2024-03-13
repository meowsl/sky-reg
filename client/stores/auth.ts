import { defineStore } from 'pinia'
import { api } from '../boot/axios'
import { jwtDecode } from 'jwt-decode'
import type { JWTTokenDecode, AuthState } from '../models/auth'

export const useAuthStore = defineStore('authStore', {
  state: (): AuthState => ({
    user: {
      id: undefined,
      firstName: undefined,
      lastName: undefined,
    },
  }),
  actions: {
    async userLogin(username: string, password: string) {
      await api
        .post('/auth/token/', { username, password })
        .then(e => {
          const token = e.data.access
          localStorage.setItem('token', token)
          this.router.push({ path: '/' })
        })
        .catch(e => {
          console.log(e)
        })
    },
    async userLogout() {
      await api
        .post('auth/logout/')
        .then(() => {
          this.clear()
          this.router.push({ path: '/login' })
        })
        .catch(e => {
          console.log(e)
        })
    },
    clear() {
      this.user = null
    },
  },
})
