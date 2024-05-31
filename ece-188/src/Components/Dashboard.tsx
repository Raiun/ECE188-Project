"use client"

import * as React from "react";

const Dashboard = () => {
  return (
    <div className="w-3/4 h-30 ml-10 mt-12 bg-white overflow-hidden shadow-lg">
        <h1 className="m-auto font-bold text-center">
            Recommended Stories
        </h1>
        <div className="grid grid-cols-4 gap-4">
            <div className="border-black border-2">01</div>
            <div className="border-black border-2">02</div>
            <div className="border-black border-2">03</div>
            <div className="border-black border-2">04</div>
            <div className="border-black border-2">05</div>
            <div className="border-black border-2">06</div>
        </div>
    </div>
  );
}

export default Dashboard