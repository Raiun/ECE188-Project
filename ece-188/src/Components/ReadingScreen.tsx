"use client"

import * as React from "react";
import { AudioManager } from "./AudioManager";
import { useTranscriber } from "../hooks/useTranscriber";

const ReadingScreen = () => {
  const transcriber = useTranscriber();

  return (
    <div className="w-full h-30 flex flex-col ml-10 mr-10 mt-12 bg-white overflow-hidden shadow-lg justify-center items-center">
        <h1 className="mt-10 mb-10 m-auto font-bold text-center text-xl">
            Read Along!
        </h1>
        <AudioManager transcriber={transcriber}></AudioManager>
    </div>
  );
}

export default ReadingScreen