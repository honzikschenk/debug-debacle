import React, { useEffect, useState } from "react";
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable";
import CodeEditor from "./CodeEditor";
import TestRunner from "./TestRunner";
import TopBar from "./TopBar";
import { useParams } from "react-router";
import Lobby from "./Lobby";
import { socket } from "@/socket";
import { useAuth0 } from "@auth0/auth0-react";
import { baseBackendUrl } from "@/lib/constants";

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

const Game = ({
  initialCode = '# Write your Python code here\nprint("Hello World!")',
  testCases = [
    {
      input: 'print("Hello World")',
      expectedOutput: "Hello World",
      passed: true,
    },
    {
      input: "print(2 + 2)",
      expectedOutput: "4",
      actualOutput: "5",
      passed: false,
    },
    {
      input: 'print("Python")',
      expectedOutput: "Python",
      passed: true,
    },
  ],
  score = 66,
  totalTests = 3,
  passedTests = 2,
}: GameProps) => {
  const [code, setCode] = useState(initialCode);
  const [time, setTime] = useState(500);
  const [started, setStarted] = useState(false);
  const [joinedSocket, setJoinedSocket] = useState(false);

  const { gameId } = useParams();

  const { user } = useAuth0();

  const handleRunCode = () => {
    console.log("Running code:", code);
  };

  const handleRunTests = () => {
    console.log("Running tests...");
  };

  const handleStart = async () => {
    const startRes = await fetch(`${baseBackendUrl}/start-game/${gameId}`, { method: 'POST' });
  };

  useEffect(() => {
    setInterval(() => setTime((prev) => prev - 1), 1000);
    if (user?.email && !joinedSocket) {
      socket.emit('join_lobby', {
        lobbyCode: parseInt(gameId),
        username: user.email
      });

      socket.on('start-game', (msg) => {
        setStarted(true);
      })

      // socket.on('joined_lobby', (msg) => {
      //   console.log(msg);
      // });

      setJoinedSocket(true);
    }
  }, [user?.email, joinedSocket, socket, gameId]);

  return (
    <div className="h-screen w-full bg-slate-950 flex flex-col">
      {!started && <Lobby id={parseInt(gameId)} onStart={handleStart} />}
      <TopBar time={time} />
      <ResizablePanelGroup direction="horizontal">
        <ResizablePanel defaultSize={50} minSize={30}>
          <CodeEditor code={code} onChange={setCode} onRun={handleRunCode} />
        </ResizablePanel>

        <ResizableHandle />

        <ResizablePanel defaultSize={50} minSize={30}>
          <TestRunner
            testCases={testCases}
            onRunTests={handleRunTests}
            score={score}
            totalTests={totalTests}
            passedTests={passedTests}
          />
        </ResizablePanel>
      </ResizablePanelGroup>
    </div>
  );
};

export default Game;
