import Editor, { OnMount, useMonaco } from '@monaco-editor/react';
import React, { useEffect, useRef, useState } from "react";
import { Card } from "./ui/card";
import "@/lib/prism-theme.css";

import dracula from '../themes/dracula.json';
import githubDark from '../themes/github-dark.json';
import monokai from '../themes/monokai.json';
import nightOwl from '../themes/night-owl.json';
import { Popover, PopoverContent, PopoverTrigger } from './ui/popover';
import { Button } from './ui/button';
import { Check, ChevronsUpDown } from 'lucide-react';
import { Command, CommandEmpty, CommandGroup, CommandInput, CommandItem, CommandList } from './ui/command';
import { cn } from '@/lib/utils';

interface CodeEditorProps {
  code?: string;
  onChange?: (code: string) => void;
  onRun?: () => void;
}

const themes = {
  'Night Owl': nightOwl,
  'GitHub Dark': githubDark,
  'Dracula': dracula,
  'Monokai': monokai
};

const CodeEditor = ({
  code = '',
  onChange = () => {},
  onRun = () => {},
}: CodeEditorProps) => {
  const preRef = useRef<HTMLPreElement>(null);

  const monaco = useMonaco();

  useEffect(() => {
    if (!monaco) return;

    for (const theme of Object.keys(themes)) {
      monaco.editor.defineTheme(theme.replace(' ', '-').toLowerCase(), themes[theme]);
    }
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

  const [open, setOpen] = useState(false)
  const [value, setValue] = useState("Night Owl")

  useEffect(() => {
    if (monaco) {
      monaco.editor.setTheme(value.toLowerCase().replace(' ', '-'));
    }
  }, [value, monaco]);

  return (
    <Card className="h-full flex flex-col bg-slate-950 border-slate-800">
      <div className="flex items-center justify-between p-4 border-b border-slate-800">
        <h2 className="text-lg font-semibold text-slate-100">
          Code Editor
        </h2>
        <Popover open={open} onOpenChange={setOpen}>
          <PopoverTrigger asChild>
            <Button
              variant="default"
              role="combobox"
              aria-expanded={open}
              className="w-[200px] justify-between"
            >
              {Object.keys(themes).find((framework) => framework === value)}
              <ChevronsUpDown className="opacity-50" />
            </Button>
          </PopoverTrigger>
          <PopoverContent className="w-[200px] p-0">
            <Command>
              <CommandInput placeholder="Search theme..." className="h-9" />
              <CommandList>
                <CommandEmpty>No theme found.</CommandEmpty>
                <CommandGroup>
                  {Object.keys(themes).map((framework) => (
                    <CommandItem
                      key={framework}
                      value={framework}
                      onSelect={(currentValue) => {
                        setValue(currentValue === value ? "" : currentValue)
                        setOpen(false)
                      }}
                    >
                      {framework}
                      <Check
                        className={cn(
                          "ml-auto",
                          value === framework ? "opacity-100" : "opacity-0"
                        )}
                      />
                    </CommandItem>
                  ))}
                </CommandGroup>
              </CommandList>
            </Command>
          </PopoverContent>
        </Popover>
      </div>
      <div className="flex-1 p-4">
        <div className="relative h-full">
        <Editor
          defaultLanguage="python"
          // defaultValue="# some comment"
          theme="night-owl"
          value={code}
          onChange={onChange}
          options={{ tabSize: 4, detectIndentation: false }}
          // onMount={handleEditorDidMount}
        />
        </div>
      </div>
    </Card>
  );
};

export default CodeEditor;
