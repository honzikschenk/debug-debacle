import React from "react";
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable";
import CodeEditor from "./CodeEditor";
import TestRunner from "./TestRunner";

interface HomeProps {
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

const Home = ({
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
}: HomeProps) => {
  const [code, setCode] = React.useState(initialCode);

  const handleRunCode = () => {
    console.log("Running code:", code);
  };

  const handleRunTests = () => {
    console.log("Running tests...");
  };

  return (
    <div className="h-screen w-full bg-slate-950">
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

export default Home;
