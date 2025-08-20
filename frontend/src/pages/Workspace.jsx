import SideBar from '../components/FeatureComponent/SideBar.jsx';
import Canvas from '../components/FeatureComponent/Canvas.jsx';
import { useState } from 'react';

export default function Workspace() {
    const [imageUrl, setImageUrl] = useState(null);

    return (
        <div>
            <SideBar setImageUrl={ setImageUrl } />
            <Canvas imageUrl={ imageUrl } />
        </div>
    )
}