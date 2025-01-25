import axios from 'axios';

const auth = {
  login: async (username, password) => {
    try {
      const response = await axios.post('/api/login', { username, password });
      return response.data;
    } catch (error) {
      console.error('Error logging in:', error);
      throw error;
    }
  },

  register: async (username, password) => {
    try {
      const response = await axios.post('/api/register', { username, password });
      return response.data;
    } catch (error) {
      console.error('Error registering:', error);
      throw error;
    }
  },

  logout: async () => {
    try {
      const response = await axios.post('/api/logout');
      return response.data;
    } catch (error) {
      console.error('Error logging out:', error);
      throw error;
    }
  },

  getCurrentUser: async () => {
    try {
      const response = await axios.get('/api/current_user');
      return response.data;
    } catch (error) {
      console.error('Error getting current user:', error);
      throw error;
    }
  },
};

export default auth;
