import React from "react";
import { Button } from "./ui/button";
import { Card } from "./ui/card";
import { ScrollArea } from "./ui/scroll-area";
import { Separator } from "./ui/separator";
import TestCase from "./TestCase";
import TestResults from "./TestResults";
import { Play } from "lucide-react";

interface TestCase {
  input: string;
  expectedOutput: string;
  actualOutput?: string;
  passed?: boolean;
}

interface TestPanelProps {
  testCases?: TestCase[];
  onRunTests?: () => void;
  isRunning?: boolean;
  score?: number;
}

const TestPanel = ({
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
  onRunTests = () => {},
  isRunning = false,
  score = 66,
}: TestPanelProps) => {
  return (
    <div className="h-full bg-slate-900 flex flex-col">
      <div className="p-4 border-b border-slate-800">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-semibold text-slate-100">Test Cases</h2>
          <Button
            onClick={onRunTests}
            disabled={isRunning}
            className="flex items-center gap-2"
          >
            <Play className="w-4 h-4" />
            {isRunning ? "Running..." : "Run Tests"}
          </Button>
        </div>
      </div>

      <div className="flex-1 flex flex-col">
        <ScrollArea className="flex-1">
          <div className="p-4 space-y-4">
            <Card className="bg-slate-800/50 p-4">
              <h3 className="text-sm font-medium text-slate-200 mb-2">
                Available Test Cases
              </h3>
              <div className="space-y-4">
                {testCases.map((testCase, index) => (
                  <TestCase
                    key={index}
                    index={index + 1}
                    input={testCase.input}
                    expectedOutput={testCase.expectedOutput}
                    actualOutput={testCase.actualOutput}
                    passed={testCase.passed}
                  />
                ))}
              </div>
            </Card>
          </div>
        </ScrollArea>

        <Separator className="bg-slate-800" />

        <div className="p-4">
          <TestResults
            results={testCases.map((test, index) => ({
              testName: `Test Case ${index + 1}`,
              passed: test.passed || false,
              input: test.input,
              expectedOutput: test.expectedOutput,
              actualOutput: test.actualOutput || test.expectedOutput,
            }))}
            score={score}
          />
        </div>
      </div>
    </div>
  );
};

export default TestPanel;
