import { io } from 'socket.io-client';
import { baseBackendUrl } from './lib/constants';

export const socket = io(baseBackendUrl);