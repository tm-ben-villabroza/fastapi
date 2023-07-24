"use client";

import React from "react";
import axios from "axios";
import useSWR from "swr";
import { EmotionService } from "@/services/emotion";

const fetchEmotions = async () => {
  const result = await axios.get("http://localhost:8000/emotion/read/all");
  console.log(result);
  return result.data;
};

function EmotionsAll() {
  const { data, error, isLoading } = useSWR(
    "/emotion/read/all",
    EmotionService.getAllEmotions
  );

  console.log(error);
  if (error) return <div>failed to load</div>;
  if (isLoading) return <div>loading...</div>;

  return <div>hello {JSON.stringify(data?.data)}!</div>;
}

export default EmotionsAll;
