import { useState, useEffect } from 'react';

export default function Canvas({ imageUrl}) {
    const [fullImageUrl, setFullImageUrl] = useState(null);

    useEffect(() => {
        if (imageUrl) {
            const baseUrl = 'http://localhost:8000';
            setFullImageUrl(`${baseUrl}${imageUrl}`);
        }
    }, [imageUrl]);

    return (
        <div className="top-[36.5px] fixed right-0 w-290 h-full bg-gray-100 shadow-lg">
            <div className="w-full h-full flex justify-center items-center p-4">
                <img src={fullImageUrl} alt="Generated image" className="max-w-full max-h-full object-contain" />
            </div>
        </div>
    )
}