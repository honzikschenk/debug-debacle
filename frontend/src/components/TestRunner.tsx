import React from "react";
import { Button } from "./ui/button";
import { ScrollArea } from "./ui/scroll-area";
import { Play } from "lucide-react";
import TestCase from "./TestCase";
import ScoreDisplay from "./ScoreDisplay";

interface TestRunnerProps {
  testCases?: Array<{
    input: string;
    expectedOutput: string;
    actualOutput?: string;
    passed?: boolean;
  }>;
  onRunTests?: () => void;
  score?: number;
  totalTests?: number;
  passedTests?: number;
  players: {
    username: string;
    passed: boolean;
  }[];
}

const TestRunner = ({
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
  onRunTests,
  score,
  totalTests,
  passedTests,
  players
}: TestRunnerProps) => {
  return (
    <div className="h-full flex flex-col bg-slate-900 border-l border-slate-800">
      <div className="p-4 border-b border-slate-800">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-lg font-semibold text-slate-200">Test Cases</h2>
          <Button onClick={onRunTests} variant="secondary" className="flex items-center gap-2">
            <Play className="w-4 h-4" />
            Run Tests
          </Button>
        </div>
        <ScoreDisplay
          score={score}
          totalTests={totalTests}
          passedTests={passedTests}
        />
      </div>

      <h2 className="text-lg font-semibold text-slate-200 ml-4 mt-4">Other Players</h2>

      <ScrollArea className="flex-1 p-4">
        <div className="space-y-4">
          {players.map((player, index) => (
            <TestCase
              key={player.username}
              name={player.username}
              passed={player.passed}
            />
          ))}
        </div>
      </ScrollArea>
    </div>
  );
};

export default TestRunner;
