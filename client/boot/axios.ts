import axios, { AxiosInstance, AxiosResponse, AxiosError } from 'axios'

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance
    $api: AxiosInstance
  }
}

const api = axios.create({
  baseURL: 'https://sky-reg.ru/api/v1/',
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
  },
})


export { api }