import { Gamepad2, Link, Timer, User } from "lucide-react";
import { useToast } from "@/hooks/use-toast"
import { Button } from "./ui/button";
import { NavLink } from "react-router-dom";

interface TopBarProps {
  time: number;
  playerCount: number;
  lobbyCode: number;
}

const TopBar = ({ time, playerCount, lobbyCode }: TopBarProps) => {
  const { toast } = useToast();

  const copyCode = (): void => {
    navigator.clipboard.writeText(lobbyCode.toString())
    toast({
        title: "Code Copied!",
        description: "You can now share the code with your friends.",
      })
  }

  return (
    <nav className="h-12 w-full text-white bg-slate-800 flex justify-between items-center px-5 relative z-20">
      <div className="flex items-center gap-x-10">
        <NavLink className="font-mono font-bold text-xl mr-5" to="/">Bug Fixer</NavLink>
        <div className="flex items-center gap-x-2">
          <User />
          {playerCount} player {playerCount > 1 ? 's' : ''}
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
        <Button onClick={() => copyCode}>Copy Link <Link className="w-4 h-4 ml-2" /></Button>
        <Button variant="destructive">Leave</Button>
      </div>
    </nav>
  )
}

export default TopBar;