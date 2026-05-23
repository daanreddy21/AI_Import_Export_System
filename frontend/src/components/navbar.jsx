import React from "react";
export default function Navbar() {
  const user = JSON.parse(localStorage.getItem("user"));
  return (
    <header className="bg-white shadow px-6 py-4 flex justify-between items-center">
      <h2 className="text-2xl font-bold text-gray-800">
        Admin Dashboard
      </h2>
      <div className="flex items-center gap-4">
        <div className="text-right">
          <h3 className="font-semibold leading-tight">
            {user?.name || "Guest"}
          </h3>
          <p className="text-sm text-gray-500 capitalize">
            {user?.role || "User"}
          </p>
        </div>
        <div className="w-10 h-10 rounded-full bg-black text-white flex items-center justify-center font-bold">
          {user?.name ? user.name.charAt(0).toUpperCase() : "U"}
        </div>
      </div>
    </header>
  );
}