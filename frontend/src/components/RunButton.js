import React from 'react';

const RunButton = ({ onClick }) => {
  return (
    <button className="run-button" onClick={onClick}>
      Run
    </button>
  );
};

export default RunButton;
