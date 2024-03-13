import { Applications } from "../models/applications"
import { api } from '../boot/axios'
import { getAuthToken } from "./useAuth"


export function useAppoints(){

  const router = useRouter()

  const getApps = async() => {
    const response = await api.get<Applications[]>('personals/applications/list', {
      headers: {
        Authorization: getAuthToken()
      }
    })
    return response.data
  }
  const filteredDate = async(date: string) => {
    const response = await api.get<Applications[]>(`personals/applications/list/?date=${date}`, {
      headers: {
        Authorization: getAuthToken()
      }
    })
    return response.data
  }

  const filteredType = async(type: string) => {
    const response = await api.get<Applications[]>(`personals/applications/list/?typepr=${type}`, {
      headers: {
        Authorization: getAuthToken()
      }
    })
    return response.data
  }

  const filteredCity = async(city: string) => {
    const response = await api.get<Applications[]>(`personals/applications/list/?city=${city}`, {
      headers: {
        Authorization: getAuthToken()
      }
    })
    return response.data
  }

  const filteredCityDate = async(city: string, date: string) => {
    const response = await api.get<Applications[]>(`personals/applications/list/?city=${city}&date=${date}`, {
      headers: {
        Authorization: getAuthToken()
      }
    })
    return response.data
  }

  const putVisit = async (id: number | string, visit: number, firstname: string, lastname: string) => {
    const response = await api.patch(`personals/applications/update/${id}`, {firstname, lastname, visit }, {
      headers: {
        Authorization: getAuthToken()
      }
    })
    location.reload()
    return response.data
  }

  const createForm = async(data: FormData) => {
    try{
      const response = await api.post('personals/applications/create/', data, {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: getAuthToken()
        }
      })
      return response.data
    } catch(e){
      console.log(e)
    }
  }

  const generalFilter = async(city:string, date:string, type:string, ) =>{
    const response = await api.get<Applications[]>(`personals/applications/list/?city=${city}&date=${date}&typepr=${type}`, {
      headers: {
        Authorization: getAuthToken()
      }
    })
    return response.data
  }

  return{
    getApps,
    filteredCity,
    filteredDate,
    filteredType,
    filteredCityDate,
    createForm,
    generalFilter,
    putVisit
  }

}