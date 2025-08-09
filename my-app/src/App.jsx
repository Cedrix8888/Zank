import { Routes, Route} from 'react-router-dom';
import Layout from "./components/Layout/Layout.jsx";
import Home from "./pages/Home/Home.jsx";
function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
        </Route>
      </Routes>
    </div>
  )
}

export default App
