import { Suspense } from "react";
import { useRoutes, Routes, Route } from "react-router-dom";
import Game from "./components/game";
import routes from "tempo-routes";
import Home from "./components/home";
import Leaderboard from "./components/leaderboard";

function App() {
  return (
    <Suspense fallback={<p>Loading...</p>}>
      <>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/game/:gameId" element={<Game />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
        </Routes>
        {import.meta.env.VITE_TEMPO === "true" && useRoutes(routes)}
      </>
    </Suspense>
  );
}

export default App;
