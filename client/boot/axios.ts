import axios, { AxiosInstance, AxiosResponse, AxiosError } from 'axios'

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance
    $api: AxiosInstance
  }
}

const getAuthToken = () => {
  if (localStorage.getItem('token')) {
    return `Bearer ${localStorage.getItem('token')}`
  }
}

const api = axios.create({
  baseURL: 'https://localhost:8000/api/v1/',
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
    Authorization: getAuthToken(),
  },
})

export { api }