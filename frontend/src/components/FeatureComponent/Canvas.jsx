import { useState, useEffect } from 'react';

export default function Canvas({ images }) {
    // images is now expected to be a dict: {layerName: imagePath}
    const [activeLayer, setActiveLayer] = useState(null);
    const [layerControls, setLayerControls] = useState({});
    
    // Initialize controls for new layers
    useEffect(() => {
        const newControls = {};
        Object.keys(images || {}).forEach(layer => {
            if (!layerControls[layer]) {
                newControls[layer] = {
                    isDragging: false,
                    position: { x: 0, y: 0 },
                    dragStart: { x: 0, y: 0 },
                    rotation: 0,
                    scale: 1,
                    stretch: { x: 1, y: 1 }
                };
            }
        });
        setLayerControls(prev => ({ ...prev, ...newControls }));
    }, [images]);

    const handleMouseDown = (layer) => (e) => {
        // Set the clicked layer as active
        setActiveLayer(layer);
        setLayerControls(prev => ({
            ...prev,
            [layer]: {
                ...prev[layer],
                isDragging: true,
                dragStart: {
                    x: e.clientX - prev[layer].position.x,
                    y: e.clientY - prev[layer].position.y
                }
            }
        }));
        // Prevent event from bubbling to lower layers
        e.stopPropagation();
    };

    const handleMouseMove = (e) => {
        if (activeLayer && layerControls[activeLayer]?.isDragging) {
            setLayerControls(prev => ({
                ...prev,
                [activeLayer]: {
                    ...prev[activeLayer],
                    position: {
                        x: e.clientX - prev[activeLayer].dragStart.x,
                        y: e.clientY - prev[activeLayer].dragStart.y
                    }
                }
            }));
        }
    };

    const handleMouseUp = () => {
        if (activeLayer) {
            setLayerControls(prev => ({
                ...prev,
                [activeLayer]: {
                    ...prev[activeLayer],
                    isDragging: false
                }
            }));
        }
    };

    const handleRotateInput = (layer) => (e) => {
        const value = parseFloat(e.target.value);
        if (!isNaN(value)) {
            setLayerControls(prev => ({
                ...prev,
                [layer]: {
                    ...prev[layer],
                    rotation: ((value % 360) + 360) % 360
                }
            }));
        }
    };

    const handleScale = (layer) => (factor) => {
        setLayerControls(prev => ({
            ...prev,
            [layer]: {
                ...prev[layer],
                scale: Math.max(0.1, prev[layer].scale + factor)
            }
        }));
    };

    const handleStretch = (layer) => (dimension, factor) => {
        setLayerControls(prev => ({
            ...prev,
            [layer]: {
                ...prev[layer],
                stretch: {
                    ...prev[layer].stretch,
                    [dimension]: Math.max(0.1, prev[layer].stretch[dimension] + factor)
                }
            }
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
                    <input 
                        type="number" 
                        value={layerControls[activeLayer]?.rotation || 0} 
                        onChange={handleRotateInput(activeLayer)} 
                        className="w-15 text-md font-stretch-ultra-condensed outline-1 hover:ring-2 hover:ring-[#3b82f6]/50 hover:border-[#3b82f6] transition-all rounded shadow" 
                        min="0" 
                        max="360" 
                        placeholder='旋转角度'
                    />
                    <img src="/add.svg" onClick={() => handleScale(activeLayer)(0.1)} className="bg-white rounded shadow-sm p-1 transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-md" />
                    <img src="/minimize.svg" onClick={() => handleScale(activeLayer)(-0.1)} className="bg-white rounded shadow-sm pb-2.5 w-6 transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-md" />
                    <img src="/add.svg" onClick={() => handleStretch(activeLayer)('x', 0.1)} className="bg-white rounded shadow-sm p-1 transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-md" />
                    <img src="/minimize.svg" onClick={() => handleStretch(activeLayer)('x', -0.1)} className="bg-white rounded shadow-sm pb-2.5 w-6 transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-md" />
                    <img src="/add.svg" onClick={() => handleStretch(activeLayer)('y', 0.1)} className="bg-white rounded shadow-sm p-1 transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-md" />
                    <img src="/minimize.svg" onClick={() => handleStretch(activeLayer)('y', -0.1)} className="bg-white rounded shadow-sm pb-2.5 w-6 transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-md" />
                </div>
            </div>
            <div className="w-full h-full flex justify-center items-center p-8 pb-16 relative">
                {Object.entries(images || {}).map(([layer, path], idx) => (
                    <img
                        key={layer}
                        src={path}
                        alt={`Layer ${layer}`}
                        className={`max-w-full max-h-full object-contain cursor-move select-none absolute top-0 left-0 ${
                            activeLayer === layer ? 'ring-2 ring-blue-500' : ''
                        }`}
                        style={{
                            zIndex: idx,
                            transform: layerControls[layer] ? `
                                translate(${layerControls[layer].position.x}px, ${layerControls[layer].position.y}px)
                                rotate(${layerControls[layer].rotation}deg)
                                scale(${layerControls[layer].scale * layerControls[layer].stretch.x}, 
                                      ${layerControls[layer].scale * layerControls[layer].stretch.y})
                            ` : 'none'
                        }}
                        onMouseDown={handleMouseDown(layer)}
                        onMouseUp={handleMouseUp}
                        onMouseMove={handleMouseMove}
                    />
                ))}
            </div>
        </div>
    )
}