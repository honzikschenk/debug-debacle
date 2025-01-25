import React from "react";
import { Progress } from "./ui/progress";
import { cn } from "@/lib/utils";

interface ScoreDisplayProps {
  score?: number; // 0-100
  totalTests?: number;
  passedTests?: number;
}

const ScoreDisplay = ({
  score = 75,
  totalTests = 10,
  passedTests = 7,
}: ScoreDisplayProps) => {
  return (
    <div className="w-full p-4 bg-background border rounded-lg shadow-sm">
      <div className="flex items-center justify-between mb-2">
        <h3 className="text-sm font-medium">Test Results</h3>
        <span
          className={cn(
            "text-sm font-semibold",
            score >= 80
              ? "text-green-500"
              : score >= 50
                ? "text-yellow-500"
                : "text-red-500",
          )}
        >
          {score}%
        </span>
      </div>

      <Progress
        value={score}
        className={cn(
          "h-2",
          score >= 80
            ? "bg-green-200"
            : score >= 50
              ? "bg-yellow-200"
              : "bg-red-200",
        )}
      />

      <div className="flex justify-between mt-2 text-xs text-muted-foreground">
        <span>
          {passedTests} of {totalTests} tests passing
        </span>
        <span>{Math.round((passedTests / totalTests) * 100)}% complete</span>
      </div>
    </div>
  );
};

export default ScoreDisplay;
