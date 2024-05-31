"use client"

import * as React from "react";
import { IconType } from "react-icons";
import { BsBookHalf } from "react-icons/bs";
import { IoSettingsOutline } from "react-icons/io5";
import { MdLocalGroceryStore } from "react-icons/md";

type Props = {
    iconType: IconType
};  

const Sidebar = () => {
  return (
    <div className="w-24 h-screen m-0 bg-white flex flex-col shadow-lg">
        <div className="w-full h-12 bg-black">
            <p className="m-auto font-bold font-serif text-white text-center">Story</p>
            <p className="m-auto font-bold font-serif text-white text-center">Quest</p>
        </div>
        <SideBarIcon icon={<BsBookHalf size="30" />} text="Stories" />
        <SideBarIcon icon={<MdLocalGroceryStore size="30" />} text="Store" />
        <SideBarIcon icon={<IoSettingsOutline size="30" />} text="Settings" />
    </div>
  );
}

const SideBarIcon = ({ icon, text = "tooltip 💡" } : {icon: any, text: string}) => {
    return(
        <div className="sidebar-icon group">
            {icon}

            <span className="sidebar-tooltip group-hover:scale-100">
                {text}
            </span>
        </div>
    );
}

export default Sidebar