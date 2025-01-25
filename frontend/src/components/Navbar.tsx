import { Gamepad2, Link, Timer, User } from "lucide-react";
import { Button } from "./ui/button";
import { NavLink } from "react-router-dom";

interface NavbarProps {}

const Navbar = ({}: NavbarProps) => {
  return (
    <nav className="h-12 w-full text-white bg-slate-800 flex justify-between items-center px-5">
      <div className="flex items-center gap-x-10">
        <NavLink className="font-mono font-bold text-xl mr-5" to="/">Bug Fixer</NavLink>
      </div>
      <div className="flex items-center gap-x-2">
        <Button>Sign In</Button>
      </div>
    </nav>
  )
}

export default Navbar;