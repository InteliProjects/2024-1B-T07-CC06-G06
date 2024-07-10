import React from 'react';
import ReactDOM from 'react-dom/client';
// Importing reset.css for global styles reset
import './reset.css';
// Importing AppRoutes component for defining application routes
import AppRoutes from './routes/routes';
import { AppProvider } from './context/AppContext';

// Rendering the AppRoutes component to the DOM
ReactDOM.createRoot(document.getElementById('root')).render(
  <AppProvider>
    <AppRoutes />
  </AppProvider>
);
