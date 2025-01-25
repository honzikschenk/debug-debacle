export const handleError = (error) => {
  console.error('Error:', error);
  return {
    message: error.message || 'An error occurred',
    stack: error.stack || 'No stack trace available',
  };
};

export const displayStackTrace = (stack) => {
  return stack.split('\n').map((line, index) => (
    <div key={index}>{line}</div>
  ));
};
