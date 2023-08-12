import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import MainPage from "./pages/MainPage";
import LoginPage from "./pages/LoginPage"
import HomePage from "./pages/HomePage";
import CreateAccountPage from "./pages/CreateAccountPage";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route exact path="/" element={<MainPage />} />
          <Route exact path="/home" element={<HomePage />} />
          <Route exact path="/login" element={<LoginPage />} />
          <Route exact path="/create-account" element={<CreateAccountPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
