import axios, { AxiosResponse } from "axios";
import api from "./api";

type EmotionResponse = Emotion[];

interface Emotion {
  id: number;
  name: string;
  create_datetime: string;
}

export class EmotionService {
  static async getAllEmotions(): Promise<AxiosResponse<EmotionResponse>> {
    const subdirectory = "/emotion/read/all";
    return await api.get(subdirectory);
  }
}
