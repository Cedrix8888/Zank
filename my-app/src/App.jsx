import { Routes, Route} from 'react-router-dom';
import Layout from "./components/Layout.jsx";
import Home from "./pages/Home.jsx";

export default function App() {
  return (
    <div className="bg-white">
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
        </Route>
      </Routes>
    </div>
  )
}