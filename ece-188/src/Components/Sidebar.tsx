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
    <div className="fixed w-24 h-screen m-0 bg-white flex flex-col shadow-lg">
        <div className="w-full h-1/6 bg-black">
            <p className="mt-10 font-bold text-white text-center">Story Quest</p>
        </div>
        <SideBarIcon icon={<BsBookHalf size="30" />} />
        <SideBarIcon icon={<IoSettingsOutline size="30" />} />
        <SideBarIcon icon={<MdLocalGroceryStore size="30" />} />
    </div>
  );
}

const SideBarIcon = ({ icon } : {icon: any}) => {
    return(
        <div className="sidebar-icon">
            {icon}
        </div>
    );
}

export default Sidebar