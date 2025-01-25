import { useNavigate } from "react-router";
import TopBar from "./TopBar";
import { Button } from "./ui/button";

const Home = () => {
  const createLobby = async () => {
    // TODO: create lobby then route
    navigate("/game");
  };

  const navigate = useNavigate();

  return (
    <div className="min-h-screen w-full bg-slate-950 text-white">
      <div className="px-48 py-24 text-center">
        <h1 className="text-7xl">Code Fixer</h1>
        <p className="mt-5 text-lg">Compete with others to fix bugs in code.</p>
        <Button onClick={createLobby} variant="secondary" className="mt-5">Create a Lobby</Button>
      </div>
    </div>
  )
};

export default Home;