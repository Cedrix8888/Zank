import { Outlet } from 'react-router-dom';
import Header from './FeatureComponent/Header.jsx';

export default function Layout() {
  return (
    <div className="min-h-screen pt-16">
        <Header />
        <main>
          <Outlet />
        </main>
    </div>
  );
};