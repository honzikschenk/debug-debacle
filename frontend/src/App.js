import React, { useState } from 'react';
import CodeEditor from './components/CodeEditor';
import Console from './components/Console';
import RunButton from './components/RunButton';
import Feedback from './components/Feedback';
import './styles/App.css';

function App() {
  const [code, setCode] = useState('');
  const [output, setOutput] = useState('');
  const [feedback, setFeedback] = useState('');

  const handleRunCode = async () => {
    try {
      const response = await api.runCode(code);
      setOutput(response.data.output);
      setFeedback(response.data.feedback);
    } catch (error) {
      setOutput('Error executing code');
      setFeedback('');
    }
  };

  return (
    <div className="app">
      <div className="editor-container">
        <CodeEditor code={code} setCode={setCode} />
      </div>
      <div className="console-container">
        <Console output={output} />
      </div>
      <div className="run-button-container">
        <RunButton onClick={handleRunCode} />
      </div>
      <div className="feedback-container">
        <Feedback feedback={feedback} />
      </div>
    </div>
  );
}

export default App;
