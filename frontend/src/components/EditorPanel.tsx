import React from "react";
import CodeEditor from "./CodeEditor";
import { Card } from "./ui/card";

interface EditorPanelProps {
  code?: string;
  onCodeChange?: (code: string) => void;
  onRunCode?: () => void;
}

const EditorPanel = ({
  code = '# Write your Python code here\nprint("Hello World!")',
  onCodeChange = () => {},
  onRunCode = () => {},
}: EditorPanelProps) => {
  return (
    <div className="h-full bg-slate-900 p-4">
      <Card className="h-full border-0 bg-transparent">
        <div className="h-full">
          <CodeEditor code={code} onChange={onCodeChange} onRun={onRunCode} />
        </div>
      </Card>
    </div>
  );
};

export default EditorPanel;
