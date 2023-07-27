import { AuthLogoutEventName } from "@/contexts/AuthContext";
import axios from "axios";

const apiUrl = "http://localhost:8000";

const api = axios.create({
  baseURL: `${apiUrl}`,
  withCredentials: true,
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response.status === 401) {
      window.location.href = "/auth/login";

      const AuthLogoutEvent = new Event(AuthLogoutEventName);
      document.dispatchEvent(AuthLogoutEvent);
    }
  }
);

export default api;
