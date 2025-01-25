import React, { useEffect, useRef } from 'react';
import * as monaco from 'monaco-editor';
import { languages } from '../utils/languageSupport';

const CodeEditor = ({ code, setCode }) => {
  const editorRef = useRef(null);

  useEffect(() => {
    if (editorRef.current) {
      const editor = monaco.editor.create(editorRef.current, {
        value: code,
        language: 'javascript',
        theme: 'vs-dark',
        automaticLayout: true,
      });

      editor.onDidChangeModelContent(() => {
        setCode(editor.getValue());
      });

      return () => {
        editor.dispose();
      };
    }
  }, [code, setCode]);

  useEffect(() => {
    languages.forEach((language) => {
      monaco.languages.register({ id: language.id });
      monaco.languages.setMonarchTokensProvider(language.id, language.tokensProvider);
      monaco.languages.setLanguageConfiguration(language.id, language.configuration);
    });
  }, []);

  return <div className="code-editor" ref={editorRef} />;
};

export default CodeEditor;
