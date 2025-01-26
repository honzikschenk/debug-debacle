import Editor, { OnMount, useMonaco } from '@monaco-editor/react';
import React, { useEffect, useRef } from "react";
import { Card } from "./ui/card";
import "@/lib/prism-theme.css";

interface CodeEditorProps {
  code?: string;
  onChange?: (code: string) => void;
  onRun?: () => void;
}

const CodeEditor = ({
  code = '',
  onChange = () => {},
  onRun = () => {},
}: CodeEditorProps) => {
  const preRef = useRef<HTMLPreElement>(null);

  const monaco = useMonaco();

  useEffect(() => {
    if (!monaco) return;
    monaco.editor.defineTheme('my-theme', {
      base: 'vs-dark',
      inherit: true,
      rules: [],
      colors: {
        'editor.background': '#0f172a',
      }
    });

    monaco.editor.setTheme('my-theme');
  }, [monaco]);

  

  // const onKeyDown: React.KeyboardEventHandler<HTMLTextAreaElement> = (e) => {
  //   // Fix indent
  //   if (e.key == "Tab") {
  //     e.preventDefault();
  //     const start = e.currentTarget.selectionStart;
  //     const end = e.currentTarget.selectionEnd;

  //     e.currentTarget.value = e.currentTarget.value.substring(0, start) + "\t" + e.currentTarget.value.substring(end);

  //     e.currentTarget.selectionStart = e.currentTarget.selectionEnd = start + 1;

  //     onChange(e.currentTarget.value);
  //   } else if (e.key == "Enter") {
  //     const start = e.currentTarget.selectionStart;
  //     const end = e.currentTarget.selectionEnd;
  //     if (e.currentTarget.value.charAt(start - 1) === ':') {
  //       e.preventDefault();
  //       // Count necessary indentation
  //       const lastLineBreak = e.currentTarget.value.substring(0, start).lastIndexOf('\n');
  //       let tabsNeeded = 1;
  //       if (lastLineBreak !== -1) {
  //         let i = lastLineBreak + 1;
  //         while (i < e.currentTarget.value.length && [9].includes(e.currentTarget.value.charCodeAt(i))) {
  //           tabsNeeded++;
  //           i++;
  //         }
  //         console.log(tabsNeeded, "!");
  //       }

  //       e.currentTarget.value = e.currentTarget.value.substring(0, start) + "\n" + ("\t".repeat(tabsNeeded)) + e.currentTarget.value.substring(end);

  //       e.currentTarget.selectionStart = e.currentTarget.selectionEnd = start + 1 + tabsNeeded;

  //       onChange(e.currentTarget.value);
  //     }
  //   }
  // };

  // const editorRef = useRef(null);

  // const handleEditorDidMount: OnMount = (editor, monaco) => {
  //   editorRef.current = editor;
  // }

  return (
    <Card className="h-full flex flex-col bg-slate-950 border-slate-800">
      <div className="flex items-center justify-between p-4 border-b border-slate-800">
        <h2 className="text-lg font-semibold text-slate-100">
          Code Editor
        </h2>
      </div>
      <div className="flex-1 p-4">
        <div className="relative h-full">
        <Editor
          defaultLanguage="python"
          // defaultValue="# some comment"
          theme="my-theme"
          value={code}
          onChange={onChange}
          // onMount={handleEditorDidMount}
        />
        </div>
      </div>
    </Card>
  );
};

export default CodeEditor;
