import { useNavigate } from "react-router";
import { Button } from "./ui/button";
import { ScrollArea } from "./ui/scroll-area";
import { Separator } from "./ui/separator";
import Navbar from "./Navbar";
import { User } from "lucide-react";
import { NavLink } from "react-router-dom";
import { useEffect, useState } from "react";
import { baseBackendUrl } from "@/lib/constants";
import { useAuth0 } from "@auth0/auth0-react";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


type Lobby = {
  id: number,
  players: number
};

const Home = () => {
  const { user } = useAuth0();



  const createLobby = async () => {
    const createRes = await fetch(`${baseBackendUrl}/create-lobby`, { method: 'POST' });
    const createData = await createRes.json();
    navigate(`/game/${createData.lobbyCode}`);
  };

  const [lobbies, setLobbies] = useState<Lobby[]>([]);

  const fetchLobbies = async () => {
    const lobbiesRes = await fetch(`${baseBackendUrl}/get-lobbies`, { method: 'GET' });
    const lobbiesData = await lobbiesRes.json() as { lobbies: number[] };

    const fullLobbiesData = await Promise.all(lobbiesData.lobbies.map((lobby) => {
      return (async () => {
        const playerCountRes = await fetch(`${baseBackendUrl}/get-lobby-player-count/${lobby}`, { method: 'GET' });
        const playerCountData = await playerCountRes.json();
        const playerCount = playerCountData['player-count'] as number;

        return {
          id: lobby,
          players: playerCount
        };
      })();
    }));

    setLobbies(fullLobbiesData);
  };

  // const joinGame = async (id: number) => {
  //   const joinGameRes = await fetch(`${baseBackendUrl}/join-lobby/${id}`, {
  //     method: 'POST',
  //     headers: {
  //       'Content-Type': 'application/json'
  //     },
  //     body: JSON.stringify({
  //       username: user.name
  //     })
  //   });
    
  //   // TODO: maybe check if successful first

  //   navigate(`/game/${id}`);
  // };

  const navigate = useNavigate();

  const handleNotAuthenticated = () => {
    toast.success('You need to log in!', {
      position: "top-right",
      autoClose: 5000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });
  }

  useEffect(() => {
    fetchLobbies();
  }, []);

  return (
    <div className="min-h-screen w-full bg-slate-950 text-white">
      <Navbar />
      <div className="px-48 py-24 flex items-center justify-center flex-col">
        <h1 className="text-7xl">Debug Debacle</h1>
        <p className="mt-5 text-lg">Compete against others to fix bugs in code.</p>
        <Button onClick={createLobby} variant="secondary" className="mt-5">Create a Lobby</Button>
        {lobbies.length > 0 && (
          <>
            <p className="text-slate-500 my-2">or</p>
            
            <ScrollArea className="max-h-72 w-48 rounded-md border border-slate-500">
              <div className="py-4 px-2">
                <h4 className="mb-4 text-sm font-medium leading-none text-center">Join a Lobby</h4>
                {lobbies.map((lobby, i) => (
                  <>
                    <NavLink key={lobby.id} className="cursor-pointer flex items-center justify-between py-2 px-2 hover:bg-slate-800 transition" to={`/game/${lobby.id}`}>
                      <span className="text-sm">
                        #{lobby.id}
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
          </>
        )}
      </div>
    </div>
  )
};

export default Home;