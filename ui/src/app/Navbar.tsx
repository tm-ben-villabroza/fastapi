"use client";

import React from "react";
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuList,
} from "@/components/ui/navigation-menu";
import Link from "next/link";
import { useAuth } from "@/contexts/AuthContext";

function Navbar() {
  const { email, isLoggedin } = useAuth();
  return (
    <NavigationMenu className="bg-slate-300 p-3">
      <NavigationMenuList>
        <NavigationMenuItem className="pr-4">
          <Link href="/">Home</Link>
        </NavigationMenuItem>
        <NavigationMenuItem className="pr-4">
          <Link href="/auth/login">Login</Link>
        </NavigationMenuItem>
        {isLoggedin ? (
          <NavigationMenuItem>
            <Link href="/emotion/all">All Emotions</Link>
          </NavigationMenuItem>
        ) : null}
        {isLoggedin ? (
          <NavigationMenuItem> Email: {email}</NavigationMenuItem>
        ) : null}
      </NavigationMenuList>
    </NavigationMenu>
  );
}

export default Navbar;
