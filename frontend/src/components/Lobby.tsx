import { Link, Loader2, User } from "lucide-react";
import { Button } from "./ui/button";
import { useToast } from "@/hooks/use-toast"
import { baseFrontendUrl } from "@/lib/constants";

interface LobbyProps {
  id: number;
  onStart: () => void;
  players: string[];
  isLoading: boolean;
}

const Lobby = ({ id, onStart, players, isLoading }: LobbyProps) => {

  const { toast } = useToast();

  const copyCode = (): void => {
    navigator.clipboard.writeText(`${baseFrontendUrl}/game/${id}`)
    toast({
      title: "Code Copied!",
      description: "You can now share the code with your friends."
    })
  }

  return (
    <div className="absolute backdrop-blur-md z-20 w-screen h-screen flex items-center justify-center text-white">
      <div className="max-w-3xl max-h-96 flex items-center flex-col gap-y-2">
        <h2 className="flex font-semibold text-3xl">Lobby #{id}</h2>
        <div className="flex items-center"><User className="h-4 w-4" /> {players.length}: <span className="text-sm ml-2">{players.join(', ')}</span></div>
        <Button onClick={copyCode} variant="secondary" className="flex items-center gap-x-2">
          Copy Link
        </Button>
        <Button onClick={onStart} variant="secondary" className="flex items-center gap-x-2 bg-green-500 hover:bg-green-600">
          Start
        </Button>
        {isLoading && <Loader2 className="animate-spin" />}
      </div>
    </div>
  )
}

export default Lobby;
