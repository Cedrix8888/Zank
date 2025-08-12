import { Link, useLocation } from 'react-router-dom';
import './Sidebar.css';


function Sidebar() {
    const location = useLocation();
    const getPlaceholder = () => {
        switch (location.pathname) {
            case '/':
                return 'Search in Dashboard';
            case '/projects':
                return 'Search in Projects';
            case '/settings':
                return 'Search in Settings';
            default:
                return '';
        }
    }
    return (
        <div className="sidebar">
            <div className="sidebar-input">
                <input type="text" placeholder="" />
            </div>
            <nav className="sidebar-nav">
                <ul>
                    <li>
                        <Link to="/">Dashboard</Link>
                    </li>
                    <li>
                        <Link to="/projects">Projects</Link>
                    </li>
                    <li>
                        <Link to="/settings">Settings</Link>
                    </li>
                </ul>
            </nav>
        </div>
    );
}

export default Sidebar;