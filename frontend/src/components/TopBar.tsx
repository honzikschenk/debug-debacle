import { Gamepad2, Link, Timer, User } from "lucide-react";
import { Button } from "./ui/button";
import { NavLink } from "react-router-dom";

interface TopBarProps {
  time: number;
}

const TopBar = ({ time }: TopBarProps) => {
  return (
    <nav className="h-12 w-full text-white bg-slate-800 flex justify-between items-center px-5 relative z-20">
      <div className="flex items-center gap-x-10">
        <NavLink className="font-mono font-bold text-xl mr-5" to="/">Bug Fixer</NavLink>
        <div className="flex items-center gap-x-2">
          <User />
          5 players
        </div>
        <div className="flex items-center gap-x-2">
          <Gamepad2 />
          LeetCode
        </div>
        <div className="flex items-center gap-x-2">
          <Timer />
          {Math.floor(time / 60)}:{String(time % 60).padStart(2, '0')}
        </div>
      </div>
      <div className="flex items-center gap-x-2">
        <Button>Copy Link <Link className="w-4 h-4 ml-2" /></Button>
        <Button>Sign In</Button>
      </div>
    </nav>
  )
}

export default TopBar;