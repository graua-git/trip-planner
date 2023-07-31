import url from './api.json'
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import { useState, useEffect } from 'react';
import MainPage from "./pages/MainPage"
import HomePage from "./pages/HomePage";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route exact path="/" element={<MainPage />} />
          <Route exact path="/home" element={<HomePage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
