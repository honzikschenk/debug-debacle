import { baseBackendUrl } from "@/lib/constants";
import { useEffect, useState } from "react"
import Navbar from "./Navbar";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableNorm, TableRow } from "./ui/table";

type Score = {
  name: string;
  seconds: number;
}

const Leaderboard = () => {
  const [scores, setScores] = useState<Score[]>([]);

  const fetchScores = async () => {
    const scoresRes = await fetch(`${baseBackendUrl}/leaderboard`, { method: 'GET' });
    // console.log('tadsafasd')
    const scoresData = await scoresRes.json();
    setScores(scoresData.scores);
  };

  useEffect(() => {
    fetchScores();
  }, []);

  return (
    <div className="min-h-screen w-full bg-slate-950 text-white">
      <Navbar />
      <h2 className="text-3xl font-bold text-center mt-5">Leaderboard</h2>
      <div className="flex items-center justify-center flex-col">
        <div className="w-96">
          <TableNorm>
            <TableHeader>
              <TableRow>
                <TableHead>#</TableHead>
                <TableHead>Name</TableHead>
                <TableHead># Seconds Left</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {scores.map((score, i) => (
                <TableRow key={i}>
                  <TableCell>{i + 1}</TableCell>
                  <TableCell>{score.name}</TableCell>
                  <TableCell>{score.seconds}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </TableNorm>
        </div>
      </div>
    </div>
  )
};

export default Leaderboard;