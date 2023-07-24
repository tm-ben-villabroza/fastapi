import { AxiosResponse } from "axios";
import api from "./api";

interface LoginResponse {
  token: string;
}

interface LoginPayload {
  email: string;
  password: string;
}

export class AuthService {
  static async postLogin(
    payload: LoginPayload
  ): Promise<AxiosResponse<LoginResponse>> {
    const subdirectory = "/auth/login";
    const response = await api
      .post(subdirectory, payload)
      .catch(function (error) {
        return Promise.reject(error);
      });
    return response;
  }
}
