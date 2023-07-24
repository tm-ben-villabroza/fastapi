import axios from "axios";

const apiUrl = "http://localhost:8000";

const api = axios.create({
  baseURL: `${apiUrl}`,
  withCredentials: true,
});

export default api;
