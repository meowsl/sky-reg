// import { defineStore } from 'pinia'
// import { jwtDecode } from 'jwt-decode'
// import { api } from '../boot/axios'
// import type { JWTTokenDecode, AuthState } from 'models/auth'


// export const useAuth = defineStore('authStore', {
//   state: (): AuthState => ({
//       user: {
//           id: undefined,
//           firstName: undefined,
//           lastName: undefined,
//       },
//   }),
//   actions: {
//       async userLogin(login: string, password: string) {
//           await api
//               .post('/auth/token/', { login, password })
//               .then(e => {
//                   const token = e.data.access
//                   localStorage.setItem('token', token)
//                   alert(token)
//                   this.router.push({ path: '/' })
//               })
//               .catch(e => {
//                   console.error(e)
//               })
//       },
//   },
// })

