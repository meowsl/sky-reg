import { Applications } from "../models/applications"

export function useAppoints(){
  const { $api } = useNuxtApp()

  const getApps = async () => {
    const appsList = ref<Applications[]>([])
    appsList.value = await $api<Applications[]>('personals/applications/list/')
    return appsList.value
  }

  const filteredDate = async (date: string) => {
    const appsList = ref<Applications[]>([])
    appsList.value = await $api<Applications[]>(`personals/applications/list/?date=${date}`)
    return appsList.value
  }

  const filteredType = async (type: string) => {
    const appsList = ref<Applications[]>([])
    appsList.value = await $api<Applications[]>(`personals/applications/list/?typepr=${type}`)
    return appsList.value
  }

  const filteredCity = async(city: string) =>{
    const appsList = ref<Applications[]>([])
    appsList.value = await $api<Applications[]>(`personals/applications/list/?city=${city}`)
    return appsList.value
  }

  const filteredCityDate = async(city: string, date: string) =>{
    const appsList = ref<Applications[]>([])
    appsList.value = await $api<Applications[]>(`personals/applications/list/?city=${city}&date=${date}`)
    return appsList.value
  }

  return{
    getApps,
    filteredDate,
    filteredType,
    filteredCity,
    filteredCityDate
  }

}