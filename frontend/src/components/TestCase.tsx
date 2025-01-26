import React from "react";
import { Card } from "./ui/card";
import { Badge } from "./ui/badge";
import { CheckCircle, XCircle } from "lucide-react";
import { cn } from "@/lib/utils";

interface TestCaseProps {
  // input?: string;
  // expectedOutput?: string;
  // actualOutput?: string;
  passed: boolean;
  index: number;
  name: string;
  user?: string;
}

const TestCase = ({
  // input = 'print("Hello World")',
  // expectedOutput = "Hello World",
  // actualOutput = "Hello World",
  passed,
  index,
  name,
  user
}: TestCaseProps) => {
  return (
    <Card className={cn("p-4 mb-4 bg-slate-950 text-white border-slate-800", {'border border-white': user === name, 'bg-yellow-500 text-black': passed && index === 0, 'bg-gray-400 text-black': passed && index == 1, 'bg-yellow-700': passed && index === 2})}>
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <div className="flex items-center gap-2">
            <h3 className="text-sm font-medium">
              {passed ? `${index + 1}. ${name}` : name}
            </h3>
            <Badge
              className={cn("flex items-center gap-1", passed ? 'bg-green-600' : '')}
            >
              {passed ? (
                <CheckCircle className="w-3 h-3" />
              ) : (
                <XCircle className="w-3 h-3" />
              )}
              {passed ? "Passed" : "In Progress"}
            </Badge>
          </div>

          {/* <div className="space-y-2">
            <div>
              <p className="text-xs text-slate-400">Input:</p>
              <pre className="mt-1 p-2 rounded bg-slate-900 text-sm font-mono text-slate-300">
                {input}
              </pre>
            </div>

            <div>
              <p className="text-xs text-slate-400">Expected Output:</p>
              <pre className="mt-1 p-2 rounded bg-slate-900 text-sm font-mono text-slate-300">
                {expectedOutput}
              </pre>
            </div>

            {!passed && actualOutput && (
              <div>
                <p className="text-xs text-slate-400">Actual Output:</p>
                <pre className="mt-1 p-2 rounded bg-slate-900 text-sm font-mono text-red-300">
                  {actualOutput}
                </pre>
              </div>
            )}
          </div> */}
        </div>
      </div>
    </Card>
  );
};

export default TestCase;
