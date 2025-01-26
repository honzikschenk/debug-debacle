import React from "react";
import { Progress } from "./ui/progress";
import { cn } from "@/lib/utils";
import { ScrollArea } from "./ui/scroll-area";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "./ui/table";
import { Badge } from "./ui/badge";
import { CheckCircle, XCircle } from "lucide-react";

interface ScoreDisplayProps {
  submissions: {
    time: Date;
    passed: boolean;
  }[];
}

const History = ({
  submissions
}: ScoreDisplayProps) => {
  return (
    <div className="w-full p-4 bg-slate-950 border border-slate-500 rounded-lg shadow-sm text-white">
      <div className="mb-2">
        <h3 className="text-sm font-medium">Submissions</h3>
        <div className="mt-2">
          {submissions.length === 0 ?
            <p className="text-xs text-slate-300">No submissions yet!</p>
          :
              <Table className="max-h-12 overflow-y-auto relative h-fit">
                <TableHeader>
                  <TableRow>
                    <TableHead>#</TableHead>
                    <TableHead>Status</TableHead>
                    <TableHead>Time</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {submissions.map((sub, i) => (
                    <TableRow key={i}>
                      <TableCell>{submissions.length - i - 1}</TableCell>
                      <TableCell>
                        <Badge
                          className={cn("flex items-center gap-1", sub.passed ? 'bg-green-600 hover:bg-green-700' : 'bg-red-500 hover:bg-red-600')}
                        >
                          {sub.passed ? (
                            <CheckCircle className="w-3 h-3" />
                          ) : (
                            <XCircle className="w-3 h-3" />
                          )}
                          {sub.passed ? "Passed" : "Failed"}
                        </Badge>
                      </TableCell>
                      <TableCell>
                        {sub.time.toLocaleTimeString()}
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
          }
        </div>
      </div>
    </div>
  );
};

export default History;
