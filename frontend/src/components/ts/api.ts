import axios from "axios";
import { apiUrl } from "./states";


export const APIRequest = axios.create({
    baseURL: apiUrl,
})