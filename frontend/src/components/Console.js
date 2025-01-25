import React from 'react';

const Console = ({ output }) => {
  return (
    <div className="console">
      <pre>{output}</pre>
    </div>
  );
};

export default Console;
