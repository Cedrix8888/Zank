import { Outlet } from 'react-router-dom';
import Header from './FeatureComponent/Header.jsx';

export default function Layout() {
  return (
    <div>
        <Header />
        <main>
          <Outlet />
        </main>
    </div>
  );
};