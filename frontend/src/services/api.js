import axios from 'axios';

const api = {
  runCode: async (code) => {
    try {
      const response = await axios.post('/execute', { code });
      return response;
    } catch (error) {
      console.error('Error executing code:', error);
      throw error;
    }
  },
};

export default api;
