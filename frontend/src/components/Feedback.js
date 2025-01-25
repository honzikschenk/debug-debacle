import React from 'react';

const Feedback = ({ feedback }) => {
  return (
    <div className="feedback">
      <pre>{feedback}</pre>
    </div>
  );
};

export default Feedback;
