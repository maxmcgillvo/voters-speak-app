import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App';
import './index.css';

// This function can be called from the main HTML page to mount the React app
window.renderYourConcerns = (containerId) => {
  const container = document.getElementById(containerId);
  if (!container) {
    console.error(`Container with ID "${containerId}" not found.`);
    return;
  }
  
  const root = ReactDOM.createRoot(container);
  root.render(
    <React.StrictMode>
      <Router>
        <App />
      </Router>
    </React.StrictMode>
  );
};

// If we're running in development mode, render the app directly
if (process.env.NODE_ENV === 'development') {
  const container = document.getElementById('root') || document.createElement('div');
  if (!container.id) {
    container.id = 'root';
    document.body.appendChild(container);
  }
  
  const root = ReactDOM.createRoot(container);
  root.render(
    <React.StrictMode>
      <Router>
        <App />
      </Router>
    </React.StrictMode>
  );
}

// Export components for direct use
export { default as ConcernsPage } from './pages/ConcernsPage';
export { default as ConcernCard } from './components/ConcernCard/ConcernCard';
export { default as NewsSources } from './components/NewsSources/NewsSources';