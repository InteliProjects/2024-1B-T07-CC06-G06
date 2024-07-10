import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
// Importing Cluster component
import Cluster from '../pages/Cluster/Cluster';
// Importing Algorithms component
import Algorithms from '../pages/Algorithms/Algorithms';
// Importing Initial component
import Initial from '../pages/Initial/Initial';

// Importing reset.css for global styles reset
import '../reset.css';
// Importing styles.css for global styles
import '../styles.css';

// Component for defining application routes
const AppRoutes = () => {
  return (
    <BrowserRouter> 
      <Routes>
        <Route exact path='/' element={<Initial />} />
        <Route exact path="/cluster" element={<Cluster />} />
        <Route exact path='/algoritmo' element={<Algorithms />}></Route>
      </Routes>
    </BrowserRouter>
  );
};

// Exporting AppRoutes component
export default AppRoutes;
