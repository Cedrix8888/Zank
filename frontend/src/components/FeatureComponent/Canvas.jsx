import { useState, useEffect } from 'react';

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
            const baseUrl = 'http://localhost:8000/';
            setFullImageUrl(`${baseUrl}${imageUrl}`);
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
            // Normalize rotation to stay within 0-360 range
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
            <div className="absolute top-4 left-4 flex flex-col gap-2 z-10">
                <div className="flex gap-2 items-center bg-white p-2 rounded shadow">
                    <button onClick={() => handleRotate(-1)} className="bg-gray-100 px-2 rounded">-1°</button>
                    <button onClick={() => handleRotate(-15)} className="bg-gray-100 px-2 rounded">-15°</button>
                    <input 
                        type="number" 
                        value={rotation} 
                        onChange={handleRotateInput}
                        className="w-16 text-center border rounded"
                        min="0"
                        max="360"
                    />
                    <button onClick={() => handleRotate(15)} className="bg-gray-100 px-2 rounded">+15°</button>
                    <button onClick={() => handleRotate(1)} className="bg-gray-100 px-2 rounded">+1°</button>
                </div>
                <div className="flex gap-2">
                    <button onClick={() => handleScale(0.1)} className="bg-white p-2 rounded shadow">+</button>
                    <button onClick={() => handleScale(-0.1)} className="bg-white p-2 rounded shadow">-</button>
                    <button onClick={() => handleStretch('x', 0.1)} className="bg-white p-2 rounded shadow">↔+</button>
                    <button onClick={() => handleStretch('x', -0.1)} className="bg-white p-2 rounded shadow">↔-</button>
                    <button onClick={() => handleStretch('y', 0.1)} className="bg-white p-2 rounded shadow">↕+</button>
                    <button onClick={() => handleStretch('y', -0.1)} className="bg-white p-2 rounded shadow">↕-</button>
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