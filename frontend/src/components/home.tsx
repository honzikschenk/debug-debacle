import { useNavigate } from "react-router";
import TopBar from "./TopBar";
import { Button } from "./ui/button";
import { ScrollArea } from "./ui/scroll-area";
import { Separator } from "./ui/separator";
import Navbar from "./Navbar";

const Home = () => {
  const createLobby = async () => {
    // TODO: create lobby then route
    navigate(`/game/${Math.floor(Math.random() * 100)}`);
  };

  const navigate = useNavigate();

  const lobbies = [
    {
      name: 'test',
      id: 'test',
      players: 2
    },
    {
      name: 'test',
      id: 'test',
      players: 2
    },
    {
      name: 'test',
      id: 'test',
      players: 2
    },
    {
      name: 'test',
      id: 'test',
      players: 2
    }
  ]

  return (
    <div className="min-h-screen w-full bg-slate-950 text-white">
      <Navbar />
      <div className="px-48 py-24 flex items-center justify-center flex-col">
        <h1 className="text-7xl">Code Fixer</h1>
        <p className="mt-5 text-lg">Compete with others to fix bugs in code.</p>
        <Button onClick={createLobby} variant="secondary" className="mt-5">Create a Lobby</Button>
        <p className="mt-10">Join a Lobby:</p>
        <ScrollArea className="h-72 w-48 mt-2">
          {lobbies.map((lobby) => (
            <>
              <div key={lobby.id}>
                {lobby.name}
              </div>
              <Separator className="my-2 fill-slate-200" />
            </>
          ))}
        </ScrollArea>
      </div>
    </div>
  )
};

export default Home;