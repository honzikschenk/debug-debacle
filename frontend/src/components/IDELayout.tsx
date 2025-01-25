import React from "react";
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable";
import EditorPanel from "./EditorPanel";
import TestPanel from "./TestPanel";

interface IDELayoutProps {
  code?: string;
  onCodeChange?: (code: string) => void;
  onRunTests?: () => void;
  isRunning?: boolean;
  testCases?: Array<{
    input: string;
    expectedOutput: string;
    actualOutput?: string;
    passed?: boolean;
  }>;
  score?: number;
}

const IDELayout = ({
  code,
  onCodeChange = () => {},
  onRunTests = () => {},
  isRunning = false,
  testCases,
  score,
}: IDELayoutProps) => {
  return (
    <div className="h-screen w-full bg-slate-900">
      <ResizablePanelGroup
        direction="horizontal"
        className="h-full rounded-lg border border-slate-800"
      >
        <ResizablePanel defaultSize={50} minSize={30}>
          <EditorPanel
            code={code}
            onCodeChange={onCodeChange}
            onRunCode={onRunTests}
          />
        </ResizablePanel>

        <ResizableHandle />

        <ResizablePanel defaultSize={50} minSize={30}>
          <TestPanel
            testCases={testCases}
            onRunTests={onRunTests}
            isRunning={isRunning}
            score={score}
          />
        </ResizablePanel>
      </ResizablePanelGroup>
    </div>
  );
};

export default IDELayout;
