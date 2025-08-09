import { Outlet, Link } from 'react-router-dom';

function Layout (){
  return (
    <div>
      <nav>
        <Link to="/" className="nav-link">首页</Link>
      </nav>      
      <main>
        <Outlet />
      </main>
      <footer>
        <p>© 2025 Zank_Designer</p>
      </footer>
    </div>
  );
};

export default Layout;