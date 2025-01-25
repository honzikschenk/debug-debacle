import { Gamepad2, Link, Timer, User } from "lucide-react";
import { Button } from "./ui/button";

const TopBar = () => {
  return (
    <nav className="h-12 w-full text-white bg-slate-800 flex justify-between items-center px-5">
      <div className="flex items-center gap-x-10">
        <h1 className="font-mono font-bold text-xl mr-5">Bug Fixer</h1>
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
          2:10
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