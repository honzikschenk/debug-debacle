import React from "react";
import { Card } from "./ui/card";
import { Badge } from "./ui/badge";
import { CheckCircle, XCircle } from "lucide-react";

interface TestCaseProps {
  input?: string;
  expectedOutput?: string;
  actualOutput?: string;
  passed?: boolean;
  index?: number;
}

const TestCase = ({
  input = 'print("Hello World")',
  expectedOutput = "Hello World",
  actualOutput = "Hello World",
  passed = true,
  index = 1,
}: TestCaseProps) => {
  return (
    <Card className="p-4 mb-4 bg-slate-950 border-slate-800">
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <div className="flex items-center gap-2 mb-2">
            <h3 className="text-sm font-medium text-slate-200">
              Test Case {index}
            </h3>
            <Badge
              variant={passed ? "default" : "destructive"}
              className="flex items-center gap-1"
            >
              {passed ? (
                <CheckCircle className="w-3 h-3" />
              ) : (
                <XCircle className="w-3 h-3" />
              )}
              {passed ? "Passed" : "Failed"}
            </Badge>
          </div>

          <div className="space-y-2">
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
          </div>
        </div>
      </div>
    </Card>
  );
};

export default TestCase;
