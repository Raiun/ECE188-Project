"use client"

import * as React from "react";
import Link from "next/link"

function loadStory() {

}

const Dashboard = () => {
  return (
    <div className="w-full h-30 ml-10 mr-10 mt-12 bg-white overflow-hidden shadow-lg">
        <h1 className="mt-10 m-auto font-bold text-center text-xl">
            Recommended Stories
        </h1>
        <div className="mt-10 grid grid-cols-4 gap-4 place-items-center">
            <div className="w-80 h-48 border-black border-2 hover:bg-gray-300">
              <Link href="/ReadAlong">01</Link>
            </div>
            <div className="w-80 h-48 border-black border-2 hover:bg-gray-300">02</div>
            <div className="w-80 h-48 border-black border-2 hover:bg-gray-300">03</div>
            <div className="w-80 h-48 border-black border-2 hover:bg-gray-300">04</div>
            <div className="w-80 h-48 border-black border-2 hover:bg-gray-300">05</div>
            <div className="w-80 h-48 border-black border-2 hover:bg-gray-300">06</div>
            <div className="w-80 h-48 border-black border-2 hover:bg-gray-300">07</div>
            <div className="w-80 h-48 border-black border-2 hover:bg-gray-300">08</div>
        </div>
    </div>
  );
}

export default Dashboard