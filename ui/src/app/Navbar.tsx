"use client";

import React from "react";
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuList,
} from "@/components/ui/navigation-menu";
import Link from "next/link";

function Navbar() {
  return (
    <NavigationMenu className="bg-slate-300 p-3">
      <NavigationMenuList>
        <NavigationMenuItem className="pr-4">
          <Link href="/">Home</Link>
        </NavigationMenuItem>
        <NavigationMenuItem className="pr-4">
          <Link href="/auth/login">Login</Link>
        </NavigationMenuItem>
        <NavigationMenuItem>
          <Link href="/emotion/all">All Emotions</Link>
        </NavigationMenuItem>
      </NavigationMenuList>
    </NavigationMenu>
  );
}

export default Navbar;
