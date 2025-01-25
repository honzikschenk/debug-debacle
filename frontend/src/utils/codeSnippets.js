export const saveCodeSnippet = (key, code) => {
  try {
    localStorage.setItem(key, code);
  } catch (error) {
    console.error('Error saving code snippet:', error);
  }
};

export const loadCodeSnippet = (key) => {
  try {
    return localStorage.getItem(key);
  } catch (error) {
    console.error('Error loading code snippet:', error);
    return null;
  }
};

export const deleteCodeSnippet = (key) => {
  try {
    localStorage.removeItem(key);
  } catch (error) {
    console.error('Error deleting code snippet:', error);
  }
};

export const listCodeSnippets = () => {
  try {
    const keys = Object.keys(localStorage);
    return keys.filter((key) => key.startsWith('codeSnippet_'));
  } catch (error) {
    console.error('Error listing code snippets:', error);
    return [];
  }
};
