import React, { useEffect, useRef } from "react";
import { Card } from "./ui/card";
import { Button } from "./ui/button";
import { Play } from "lucide-react";
import Prism from "prismjs";
import "prismjs/components/prism-python";
import "@/lib/prism-theme.css";

interface CodeEditorProps {
  code?: string;
  onChange?: (code: string) => void;
  onRun?: () => void;
}

const CodeEditor = ({
  code = '# Write your Python code here\nprint("Hello World!")',
  onChange = () => {},
  onRun = () => {},
}: CodeEditorProps) => {
  const preRef = useRef<HTMLPreElement>(null);

  const onKeyDown: React.KeyboardEventHandler<HTMLTextAreaElement> = (e) => {
    // Fix indent
    if (e.key == "Tab") {
      e.preventDefault();
      const start = e.currentTarget.selectionStart;
      const end = e.currentTarget.selectionEnd;

      e.currentTarget.value = e.currentTarget.value.substring(0, start) + "\t" + e.currentTarget.value.substring(end);

      e.currentTarget.selectionStart = e.currentTarget.selectionEnd = start + 1;
    }
  };

  useEffect(() => {
    if (preRef.current) {
      const html = Prism.highlight(code, Prism.languages.python, 'python');
      preRef.current.innerHTML = html;
    }
  }, [code]);

  return (
    <Card className="h-full flex flex-col bg-slate-950 border-slate-800">
      <div className="flex items-center justify-between p-4 border-b border-slate-800">
        <h2 className="text-sm font-medium text-slate-200">
          Python Code Editor
        </h2>
        <Button
          size="sm"
          onClick={onRun}
          className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700"
        >
          <Play className="w-4 h-4" />
          Run Code
        </Button>
      </div>
      <div className="flex-1 p-4">
        <div className="relative h-full">
          <textarea
            value={code}
            onChange={(e) => onChange(e.target.value)}
            onKeyDown={onKeyDown}
            className="w-full h-full resize-none bg-transparent text-transparent font-mono text-sm p-4 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-600 caret-white absolute top-0 left-0 z-10"
            spellCheck="false"
            placeholder="Write your Python code here..."
          />
          <pre
            ref={preRef}
            className="w-full h-full font-mono text-sm p-4 rounded-md prism-editor overflow-hidden"
          >
          </pre>
        </div>
      </div>
    </Card>
  );
};

export default CodeEditor;
