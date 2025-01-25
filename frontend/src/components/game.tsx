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

  const { gameId } = useParams();

  const handleRunCode = () => {
    console.log("Running code:", code);
  };

  const handleRunTests = () => {
    console.log("Running tests...");
  };

  useEffect(() => {
    setInterval(() => setTime((prev) => prev - 1), 1000);
  }, []);

  return (
    <div className="h-screen w-full bg-slate-950 flex flex-col">
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
