import { Outlet } from 'react-router-dom';
import SideBar from '../FeatureComponent/SideBar/SideBar.jsx';
import './Layout.css';

function Layout() {
  return (
    <div className='layout'>
      <SideBar />
      <main className="main-content">
        <Outlet />
      </main>
      <footer>
        <p>© 2025 Zank_Designer</p>
      </footer>
    </div>
  );
};

export default Layout;