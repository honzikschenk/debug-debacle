import React from "react";
import { Progress } from "@/components/ui/progress";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { CheckCircle, XCircle } from "lucide-react";

interface TestResult {
  testName: string;
  passed: boolean;
  input: string;
  expectedOutput: string;
  actualOutput: string;
}

interface TestResultsProps {
  results: TestResult[];
  score: number;
}

const TestResults = ({
  results = [
    {
      testName: "Test Case 1",
      passed: true,
      input: "5",
      expectedOutput: "25",
      actualOutput: "25",
    },
    {
      testName: "Test Case 2",
      passed: false,
      input: "3",
      expectedOutput: "9",
      actualOutput: "8",
    },
  ],
  score = 50,
}: TestResultsProps) => {
  return (
    <div className="p-4 bg-background border rounded-lg">
      <div className="mb-4">
        <div className="flex items-center justify-between mb-2">
          <h3 className="text-lg font-semibold">Test Results</h3>
          <Badge variant={score >= 80 ? "success" : "destructive"}>
            {score}% Passing
          </Badge>
        </div>
        <Progress value={score} className="h-2" />
      </div>

      <div className="space-y-3">
        {results.map((result, index) => (
          <Card key={index} className="p-3">
            <div className="flex items-start justify-between">
              <div className="flex items-center gap-2">
                {result.passed ? (
                  <CheckCircle className="h-5 w-5 text-green-500" />
                ) : (
                  <XCircle className="h-5 w-5 text-red-500" />
                )}
                <span className="font-medium">{result.testName}</span>
              </div>
              <Badge variant={result.passed ? "success" : "destructive"}>
                {result.passed ? "PASS" : "FAIL"}
              </Badge>
            </div>
            <div className="mt-2 text-sm space-y-1">
              <div className="grid grid-cols-2 gap-2">
                <div>
                  <span className="text-muted-foreground">Input:</span>
                  <div className="font-mono bg-muted p-1 rounded">
                    {result.input}
                  </div>
                </div>
                <div>
                  <span className="text-muted-foreground">
                    Expected Output:
                  </span>
                  <div className="font-mono bg-muted p-1 rounded">
                    {result.expectedOutput}
                  </div>
                </div>
              </div>
              {!result.passed && (
                <div>
                  <span className="text-muted-foreground">Actual Output:</span>
                  <div className="font-mono bg-muted p-1 rounded">
                    {result.actualOutput}
                  </div>
                </div>
              )}
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default TestResults;
