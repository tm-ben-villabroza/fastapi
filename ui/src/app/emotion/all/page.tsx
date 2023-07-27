"use client";

import React from "react";
import axios from "axios";
import useSWR from "swr";
import { EmotionService } from "@/services/emotion";

const fetchEmotions = async () => {
  const result = await axios.get("http://localhost:8000/emotion/read/all");
  return result.data;
};

function EmotionsAll() {
  const { data, error, isLoading } = useSWR(
    "/emotion/read/all",
    EmotionService.getAllEmotions
  );

  if (error) return <div>Error: {error?.response.data.detail.message}</div>;
  if (isLoading) return <div>loading...</div>;

  return <div>hello {JSON.stringify(data?.data)}!</div>;
}

export default EmotionsAll;
