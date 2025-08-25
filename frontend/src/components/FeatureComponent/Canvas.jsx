import { useState, useEffect } from 'react';
import { API_CONFIG } from '/config'; // 导入配置

export default function Canvas({ imageUrl}) {
    const [fullImageUrl, setFullImageUrl] = useState(null);
    const [isDragging, setIsDragging] = useState(false);
    const [position, setPosition] = useState({ x: 0, y: 0 });
    const [dragStart, setDragStart] = useState({ x: 0, y: 0 });
    const [rotation, setRotation] = useState(0);
    const [scale, setScale] = useState(1);
    const [stretch, setStretch] = useState({ x: 1, y: 1 });

    useEffect(() => {
        if (imageUrl) {
            setFullImageUrl(`${API_CONFIG.baseUrl}${imageUrl}`);
        }
    }, [imageUrl]);

    const handleMouseDown = (e) => {
        setIsDragging(true);
        setDragStart({
            x: e.clientX - position.x,
            y: e.clientY - position.y
        });
    };

    const handleMouseMove = (e) => {
        if (isDragging) {
            setPosition({
                x: e.clientX - dragStart.x,
                y: e.clientY - dragStart.y
            });
        }
    };

    const handleMouseUp = () => {
        setIsDragging(false);
    };

    const handleRotate = (amount) => {
        setRotation(prev => {
            const newRotation = prev + amount;
            return ((newRotation % 360) + 360) % 360;
        });
    };

    const handleRotateInput = (e) => {
        const value = parseFloat(e.target.value);
        if (!isNaN(value)) {
            setRotation(((value % 360) + 360) % 360);
        }
    };

    const handleScale = (factor) => {
        setScale(prev => Math.max(0.1, prev + factor));
    };

    const handleStretch = (dimension, factor) => {
        setStretch(prev => ({
            ...prev,
            [dimension]: Math.max(0.1, prev[dimension] + factor)
        }));
    };

    return (
        <div className="top-[36.5px] fixed right-0 w-290 h-full bg-gray-100 shadow-lg">
            <div className="absolute left-2 top-2 p-2 bg-white rounded">
                <div className="flex gap-2">
                    <p className="text-sm font-stretch-ultra-condensed">rotation(deg)</p>
                    <p className="text-sm font-stretch-ultra-condensed pl-2">scaling</p>
                    <p className="text-sm font-stretch-ultra-condensed pl-2.5">stretching:x</p>
                    <p className="text-sm font-stretch-ultra-condensed">stretching:y</p>
                </div>
                <div className="flex gap-2 h-6">
                    <input type="number" value={rotation} onChange={handleRotateInput} className="w-15 text-md font-stretch-ultra-condensed outline-1 hover:ring-2 hover:ring-[#3b82f6]/50 hover:border-[#3b82f6] transition-all rounded shadow" min="0" max="360" placeholder='旋转角度'/>
                    <img src="/add.svg" onClick={() => handleScale(0.1)} className="bg-white rounded shadow-sm p-1 transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-md" />
                    <img src="/minimize.svg" onClick={() => handleScale(-0.1)} className="bg-white rounded shadow-sm pb-2.5 w-6 transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-md" />
                    <img src="/add.svg" onClick={() => handleStretch('x', 0.1)} className="bg-white rounded shadow-sm p-1 transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-md" />
                    <img src="/minimize.svg" onClick={() => handleStretch('x', -0.1)} className="bg-white rounded shadow-sm pb-2.5 w-6 transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-md" />
                    <img src="/add.svg" onClick={() => handleStretch('y', 0.1)} className="bg-white rounded shadow-sm p-1 transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-md" />
                    <img src="/minimize.svg" onClick={() => handleStretch('y', -0.1)} className="bg-white rounded shadow-sm pb-2.5 w-6 transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-md" />
                </div>
            </div>
            <div className="w-full h-full flex justify-center items-center p-8 pb-16">
                <img 
                    src={fullImageUrl} 
                    alt="Generated image" 
                    className="max-w-full max-h-full object-contain cursor-move select-none"
                    style={{
                        transform: `
                            translate(${position.x}px, ${position.y}px)
                            rotate(${rotation}deg)
                            scale(${scale * stretch.x}, ${scale * stretch.y})
                        `
                    }}                
                    onMouseDown={handleMouseDown}
                    onMouseUp={handleMouseUp}
                    onMouseMove={handleMouseMove}
                />
            </div>
        </div>
    )
}