import React from 'react';
import { Routes, Route } from 'react-router-dom';
import ConcernsPage from './pages/ConcernsPage';
import './App.css';

const App = () => {
  return (
    <div className="app">
      <Routes>
        <Route path="/" element={<ConcernsPage />} />
        <Route path="/concerns" element={<ConcernsPage />} />
      </Routes>
    </div>
  );
};

export default App;