"use client"

import * as React from "react";
import { FaUserCircle } from "react-icons/fa";

const ProfileButton = () => {
  return (
    <div className="absolute h-10 flex flex-row mt-5 mr-0 p-0 justify-center items-center">
        <img className="mb-2 mr-0 p-0" width="60px" height="60px" src="streak.png"></img>
        <p className="text-4xl font-bold m-3 ml-0 mb-2 p-0">308</p>
        <button>
            <FaUserCircle size="36"></FaUserCircle>
        </button>
    </div>
  );
}

export default ProfileButton