import React, { useEffect, useRef, useState } from "react";
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable";
import CodeEditor from "./CodeEditor";
import TestRunner from "./TestRunner";
import TopBar from "./TopBar";
import { useNavigate, useParams } from "react-router";
import Lobby from "./Lobby";
import { socket } from "@/socket";
import { useAuth0 } from "@auth0/auth0-react";
import { baseBackendUrl } from "@/lib/constants";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "./ui/dialog";
import { Button } from "./ui/button";
import { ordinal } from "@/lib/utils";

interface GameProps {
  initialCode?: string;
  testCases?: Array<{
    input: string;
    expectedOutput: string;
    actualOutput?: string;
    passed?: boolean;
  }>;
  score?: number;
  totalTests?: number;
  passedTests?: number;
}

type PlayerScores = {
  username: string;
  passed: boolean;
};

export type Submission = {
  time: Date;
  passed: boolean;
}

const Game = ({
  initialCode = 'def Fibonacci(n):\n  # Check if input is 0 then it will\n  # print incorrect input\n  if n < 0:\n    print("Incorrect input")\n  # Check if n is 0\n  # then it will return 0\n  elif n == 0:\n    return 0\n\n  # Check if n is 1,2\n  # it will return 1\n  elif n == 1 or n == 2:\n    return 1\n\n  else:\n    return Fibonacci(n-1) + Fibonacci(n-2)\n\n  # Driver Program\n  print(Fibonacci(9))\n',
  totalTests = 3,
  passedTests = 2,
}: GameProps) => {
  const [code, setCode] = useState(initialCode);
  const [time, setTime] = useState(0);
  const [maxTime, setMaxTime] = useState(1);
  const [started, setStarted] = useState(false);
  const [joinedSocket, setJoinedSocket] = useState(false);
  const [players, setPlayers] = useState<string[]>([]);
  const [score, setScore] = useState(0);
  const [inProgPlayers, setInProgPlayers] = useState<string[]>([]);
  const [passedPlayers, setPassedPlayers] = useState<string[]>([]);
  const [isTesting, setIsTesting] = useState(false);
  const [submissions, setSubmissions] = useState<Submission[]>([]);
  const [congratsOpen, setCongratsOpen] = useState(false);
  const [place, setPlace] = useState<number | null>(null);
  const [passed, setPassed] = useState(false);
  const [timeoutOpen, setTimeoutOpen] = useState(false);

  const interval = useRef<NodeJS.Timeout>();

  useEffect(() => {
    function handleTimer() {
      interval.current = setInterval(() => {
        setTime((prev) => prev - 1);
      }, 1000);
    }

    if(time <= 0 && interval.current) {
      if (!passed) {
        submitCode();
      }
      clearInterval(interval.current);
    }
    if(time === maxTime) {
      handleTimer();
    }
  }, [time, maxTime]);

  const { gameId } = useParams();

  const { user } = useAuth0();

  const navigate = useNavigate();

  const leaveGame = () => {
    navigate('/');
    socket.emit('leave_lobby', {'lobbyCode': parseInt(gameId), 'username': user.name});
  }

  const handleRunCode = () => {
    console.log("Running code:", code);
  };

  const handleRunTests = () => {
    submitCode();
  };

  const handleStart = async () => {
    const startRes = await fetch(`${baseBackendUrl}/start-game/${gameId}`, { method: 'POST' });
  };

  const fetchPlayers = async () => {
    const currentPlayersRes = await fetch(`${baseBackendUrl}/get-lobby-players/${gameId}`, { method: 'GET' });
    const { players } = await currentPlayersRes.json();

    setPlayers(players);
    setInProgPlayers(players);
  };

  const submitCode = async () => {
    setIsTesting(true);
    const submissionRes = await fetch(`${baseBackendUrl}/submission/${gameId}`, {
      method: 'POST',
      body: JSON.stringify({ username: user.name, submission: code }),
      headers: {
        'Content-Type': 'application/json'
      }
    });

    const { success } = await submissionRes.json();

    setSubmissions([{ time: new Date(), passed: success }, ...submissions])
    if (!success && time <= 0) {
      setTimeoutOpen(true);
    }
    setIsTesting(false);
  };

  useEffect(() => {
    if (passed) {
      setPlace(passedPlayers.length);
      setCongratsOpen(true);
    }
  }, [passed]);

  useEffect(() => {
    fetchPlayers();
  }, []);


  useEffect(() => {
    if (user?.name && !joinedSocket) {
      socket.emit('join_lobby', {
        lobbyCode: parseInt(gameId),
        username: user.name
      });

      socket.on('start-game', (msg) => {
        setStarted(true);
        setCode(msg.code);

        setTime(msg.time);
        setMaxTime(msg.time);
      })

      socket.on('joined_lobby', (msg) => {
        setPlayers((prev) => [...prev, msg]);
        setInProgPlayers((prev) => [...prev, msg]);
      });

      socket.on('submission', (msg) => {
        if (msg.score[1] / msg.score[0] === 1 && !passedPlayers.includes(msg.username)) {
          if (msg.username === user?.name) {
            setPassed(true);
          }
          setInProgPlayers((prev) => prev.filter((player) => player !== msg.username));
          setPassedPlayers((prev) => [...prev, msg.username]);
        }
      });

      setJoinedSocket(true);
    }
  }, [user?.name, joinedSocket, socket, gameId]);

  return (
    <div className="h-screen w-full bg-slate-950 flex flex-col">
      {!started && <Lobby id={parseInt(gameId)} onStart={handleStart} players={players} />}
      <Dialog open={congratsOpen} onOpenChange={(open) => setCongratsOpen(open)}>
        <DialogContent className="sm:max-w-[425px]">
          <DialogHeader>
            <DialogTitle>You found the bug!</DialogTitle>
            <DialogDescription>
              &#127881; Congrats! You finished {ordinal(place)}.
            </DialogDescription>
          </DialogHeader>
        </DialogContent>
      </Dialog>

      <Dialog open={timeoutOpen} onOpenChange={(open) => setTimeoutOpen(open)}>
        <DialogContent className="sm:max-w-[425px]">
          <DialogHeader>
            <DialogTitle>Out of time!</DialogTitle>
            <DialogDescription>
              &#9200; You're out of time! Check the bottom right to see the results.
            </DialogDescription>
          </DialogHeader>
        </DialogContent>
      </Dialog>

      <TopBar time={time} playerCount={players.length} lobbyCode={parseInt(gameId)} leaveGame={leaveGame} />
      
      <ResizablePanelGroup direction="horizontal">
        <ResizablePanel defaultSize={50} minSize={30}>
          <CodeEditor code={code} onChange={setCode} onRun={handleRunCode} />
        </ResizablePanel>

        <ResizableHandle />

        <ResizablePanel defaultSize={50} minSize={30}>
          <TestRunner
            // testCases={playerSocres}
            submissions={submissions}
            onRunTests={handleRunTests}
            score={score}
            totalTests={totalTests}
            passedTests={passedTests}
            isTesting={isTesting}
            inProgPlayers={inProgPlayers}
            passedPlayers={passedPlayers}
            user={user?.name}
            passed={passed || time <= 0}
          />
        </ResizablePanel>
      </ResizablePanelGroup>
    </div>
  );
};

export default Game;
