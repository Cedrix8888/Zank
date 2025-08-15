import { Routes, Route} from 'react-router-dom';
import Layout from "./components/Layout.jsx";
import Home from "./pages/Home.jsx";
import Workspace from "./pages/Workspace.jsx"

export default function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="/workspace" element={<Workspace />}>
            <Route path=":id" element={<Workspace />} />
          </Route>
        </Route>
      </Routes>
    </div>
  )
}