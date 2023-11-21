import { Applications } from "../models/applications"
import { api } from '../boot/axios'

export function useAppoints(){

  const getApps = async() => {
    const response = await api.get<Applications[]>('personals/applications/list')
    return response.data
  }
  const filteredDate = async(date: string) => {
    const response = await api.get<Applications[]>(`personals/applications/list/?date=${date}`)
    return response.data
  }

  const filteredType = async(type: string) => {
    const response = await api.get<Applications[]>(`personals/applications/list/?typepr=${type}`)
    return response.data
  }

  const filteredCity = async(city: string) => {
    const response = await api.get<Applications[]>(`personals/applications/list/?city=${city}`)
    return response.data
  }

  const filteredCityDate = async(city: string, date: string) => {
    const response = await api.get<Applications[]>(`personals/applications/list/?city=${city}&date=${date}`)
    return response.data
  }

  return{
    getApps,
    filteredCity,
    filteredDate, filteredType, filteredCityDate
  }

}