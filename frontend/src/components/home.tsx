import { useNavigate } from "react-router";
import TopBar from "./TopBar";
import { Button } from "./ui/button";
import { ScrollArea } from "./ui/scroll-area";
import { Separator } from "./ui/separator";
import Navbar from "./Navbar";
import { User } from "lucide-react";
import { NavLink } from "react-router-dom";

const Home = () => {
  const createLobby = async () => {
    // TODO: create lobby then route
    navigate(`/game/${Math.floor(Math.random() * 100)}`);
  };

  const navigate = useNavigate();

  const lobbies = [
    {
      name: 'Lobby 1',
      id: 'test',
      players: 2
    },
    {
      name: 'Lobby 2',
      id: 'test',
      players: 1
    },
    {
      name: 'Lobby 3',
      id: 'test',
      players: 4
    },
    {
      name: 'Lobby 4',
      id: 'test',
      players: 3
    }
  ]

  return (
    <div className="min-h-screen w-full bg-slate-950 text-white">
      <Navbar />
      <div className="px-48 py-24 flex items-center justify-center flex-col">
        <h1 className="text-7xl">Code Fixer</h1>
        <p className="mt-5 text-lg">Compete with others to fix bugs in code.</p>
        <Button onClick={createLobby} variant="secondary" className="mt-5">Create a Lobby</Button>

        <p className="text-slate-500 my-2">or</p>
        
        <ScrollArea className="max-h-72 w-48 rounded-md border border-slate-500">
          <div className="py-4 px-2">
            <h4 className="mb-4 text-sm font-medium leading-none text-center">Join a Lobby</h4>
            {lobbies.map((lobby, i) => (
              <>
                <NavLink key={lobby.id} className="flex items-center justify-between py-2 px-2 hover:bg-slate-800 transition" to={`/game/${lobby.id}`}>
                  <span className="text-sm">
                    {lobby.name}
                  </span>
                  <span className="text-xs flex items-center">
                    <User className="w-3 h-3" /> {lobby.players}
                  </span>
                </NavLink>
                {i !== lobbies.length - 1 &&
                  <Separator className="bg-slate-500" />
                }
              </>
            ))}
          </div>
        </ScrollArea>
      </div>
    </div>
  )
};

export default Home;