import { Link, useParams} from 'react-router-dom';
import { useState } from 'react';
import { API_CONFIG } from '/config'; // 导入配置

export default function Sidebar({ setImages }) {
    const [isLoading, setIsLoading] = useState(false);
    const { id } = useParams();

    const [formData, setFormData] = useState({
        user_id: "zx",
        width: 1024,
        height: 1024,
        color: "#000000",
        prompt_pos: "glass bottle, high quality",
        prompt_neg: "face asymmetry, eyes asymmetry, deformed eyes, open mouth"
    });

    function handleChange(e) {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (isLoading) return;

        try {
        setIsLoading(true);
        
        let endpoint = '';
        let submitData;

            switch (id) {
                case 'rgb':
                    endpoint = '/api/img/rgb';
                    submitData = {
                        user_id: formData.user_id,
                        width: formData.width, 
                        height: formData.height,
                        color: formData.color
                    };
                    break;
                case 'layer':
                    endpoint = '/api/img/layer';
                    submitData = {
                        user_id: formData.user_id,
                        width: formData.width, 
                        height: formData.height,
                        prompt_pos: formData.prompt_pos,
                        prompt_neg: formData.prompt_neg
                    };
                    break;
                case 'svg':
                    endpoint = '/api/img/svg';
                    submitData = {};
                default:
                    submitData = {};
            }
    
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': "application/json",
                'api-key': "u#Tqw(]%CTO+u&[FQ&G6apADEmKzOqc[Aqk-6W~Z"
            },
            body: JSON.stringify(submitData)
        });

        if (response.ok) {
            const result = await response.json();
            if (id === 'rgb') {
                setImages(prev => ({ ...prev, rgb: `${API_CONFIG.baseUrl}/${result.local_path}` }));
            } else if (id === 'layer') {
                setImages(prev => ({ ...prev, trans: `${API_CONFIG.baseUrl}/${result.local_path}` }));
            } else if (id === 'svg') {
                setImages(prev => ({ ...prev, svg: `${API_CONFIG.baseUrl}/${result.local_path}` }));
            }
            console.log('提交成功:', result);
        } else {
            console.error('提交失败');
        }
        } catch (error) {
            console.error('请求出错:', error);
        } finally {
            setIsLoading(false);
        }
    };

    const handleReset = (e) => {

        e.preventDefault();

        switch (id) {
            case 'rgb':
                setFormData(prev => ({
                    ...prev,
                    width: 1080,
                    height: 1920,
                    color: '#000000',
                }));
                break;
            case 'layer':
                setFormData(prev => ({
                    ...prev,
                    prompt_pos: "",
                    prompt_neg: "",
                }));
                break;
            default:
                setFormData({
                    ...prev,
                });
        }
    };

    switch (id) {
        case 'rgb':
            return (
                <div className="top-[36.5px] fixed left-0 w-60 h-full bg-gray-100 shadow-lg">
                    <form className="mx-4 mt-4 h-[20%] bg-gray-200 overflow-hidden space-y-2 shadow-sm" onSubmit={handleSubmit}>
                        <p className="font-stretch-ultra-condensed font-semibold text-center">please make your background basis</p>
                        <div className="flex items-center justify-between gap-x-0.5">
                            <label htmlFor="color_picker" className="font-stretch-ultra-condensed cursor-pointer">color-picker</label>
                            <input type="color" name="color" id="color_picker" className="h-8 cursor-pointer flex-1" value={formData.color} onChange={handleChange} required disabled={isLoading} />
                            <input type="text" name="color" className="w-18 text-sm font-stretch-ultra-condensed outline-1 mr-1 hover:ring-2 hover:ring-[#3b82f6]/50 hover:border-[#3b82f6] transition-all rounded-[2px]" value={formData.color} onChange={handleChange} placeholder="color in #***" required disabled={isLoading} />     
                        </div>
                        <div className="flex items-center justify-between mt-2 gap-x-0.5">
                            <label htmlFor="width" className="font-stretch-ultra-condensed align-top cursor-pointer ">width:</label>
                            <input type="text" name="width" id="width" className="w-16 outline-1 hover:ring-2 hover:ring-[#3b82f6]/50 hover:border-[#3b82f6] transition-all rounded-[2px]" value={formData.width} onChange={handleChange} required disabled={isLoading} />
                            <label htmlFor="height" className="font-stretch-ultra-condensed align-top cursor-pointer">height:</label>
                            <input type="text" name="height" id="height" className="w-16 outline-1 mr-1 hover:ring-2 hover:ring-[#3b82f6]/50 hover:border-[#3b82f6] transition-all rounded-[2px]" value={formData.height} onChange={handleChange} required disabled={isLoading} />
                        </div>
                        <div className='flex justify-center'>
                            <button type="submit" className="text-sm w-[80%] cursor-pointer bg-gray-300 hover:bg-gray-300/70 hover:-translate-y-0.5 transition-all hover:shadow-sm" disabled={isLoading} onClick={handleSubmit}>Submit</button>
                        </div>
                        <div className='flex justify-center'>
                            <button type="button" className="text-sm w-[80%] cursor-pointer bg-gray-300 hover:bg-gray-300/70 hover:-translate-y-0.5 transition-all hover:shadow-sm" disabled={isLoading} onClick={handleReset} >Reset</button>
                        </div>
                    </form>
                    <div className="absolute bottom-[45px] w-full h-16 flex justify-evenly items-center px-12 bg-gray-100 gap-16">
                        <Link to="/workspace/rgb" className="blcok cursor-not-allowed bg-white hover:bg-gray-300 hover:-translate-y-0.5 transition-all hover:shadow-sm rounded-3xl">
                            <img src="/left_arrow.svg" alt="left_arrow" className="h-10 w-12" />
                        </Link>
                        <Link to="/workspace/layer" className="block cursor-pointer bg-white hover:bg-gray-300 hover:-translate-y-0.5 transition-all hover:shadow-sm rounded-3xl">
                            <img src="/right_arrow.svg" alt="right_arrow" className="h-10 w-12" />
                        </Link>
                    </div>
                </div>
            );
        
        case 'layer':
            return (
                <div className="top-[36.5px] fixed left-0 w-60 h-full bg-gray-100 shadow-lg">
                    <form className="mx-4 mt-4 h-[32%] bg-gray-200 overflow-hidden space-y-2 shadow-sm relative" onSubmit={handleSubmit}>
                        <p className="font-stretch-ultra-condensed font-semibold text-center">please make your layers</p>
                        <p className="font-stretch-ultra-condensed font-semibold pl-2">positive_prompt:</p>
                        <div className="flex justify-center">
                            <textarea name="positive_prompt" className="resize-none w-full mx-2 text-sm font-stretch-ultra-condensed outline-1 hover:ring-2 hover:ring-[#3b82f6]/50 hover:border-[#3b82f6] transition-all rounded-[2px]" value={formData.prompt_pos} onChange={handleChange} placeholder="please input your positive prompt" required disabled={isLoading} />
                        </div>
                        <p className="font-stretch-ultra-condensed font-semibold pl-2">negative_prompt:</p>
                        <div className="flex justify-center">
                            <textarea name="positive_prompt" className="resize-none w-full mx-2 text-sm font-stretch-ultra-condensed outline-1 hover:ring-2 hover:ring-[#3b82f6]/50 hover:border-[#3b82f6] transition-all rounded-[2px]" value={formData.prompt_neg} onChange={handleChange} placeholder="please input your negative prompt" required disabled={isLoading} />
                        </div>
                        <div className='flex justify-center'>
                            <button type="submit" className="text-sm w-[80%] cursor-pointer bg-gray-300 hover:bg-gray-300/70 hover:-translate-y-0.5 transition-all hover:shadow-sm" disabled={isLoading} >Submit</button>
                        </div>
                        <div className="flex justify-center">
                            <button type="button" className="text-sm w-[80%] cursor-pointer bg-gray-300 hover:bg-gray-300/70 hover:-translate-y-0.5 transition-all hover:shadow-sm" disabled={isLoading} onClick={handleReset}>Reset</button>
                        </div>
                    </form>
                        <div className="absolute bottom-[45px] w-full h-16 flex justify-evenly items-center px-12 bg-gray-100 gap-16">
                            <Link to="/workspace/rgb" className="blcok cursor-pointer bg-white hover:bg-gray-300 hover:-translate-y-0.5 transition-all hover:shadow-sm rounded-3xl">
                                <img src="/left_arrow.svg" alt="left_arrow" className="h-10 w-12" />
                            </Link>
                            <Link to="/workspace/svg" className="block cursor-pointer bg-white hover:bg-gray-300 hover:-translate-y-0.5 transition-all hover:shadow-sm rounded-3xl">
                                <img src="/right_arrow.svg" alt="right_arrow" className="h-10 w-12" />
                            </Link>
                    </div>
                </div>
            );
        
        case 'svg':
            return(
                <div className="top-[36.5px] fixed left-0 w-60 h-full bg-gray-100 shadow-lg">
                    <form className="mx-4 mt-4 h-[18%] bg-gray-200 overflow-hidden space-y-2 shadow-sm relative" onSubmit={handleSubmit}>
                        <p className="font-stretch-ultra-condensed font-semibold text-center">please make your svg images</p>
                        <div className="flex justify-center">
                            <textarea name="positive_prompt" className="resize-none w-full mx-2 text-sm font-stretch-ultra-condensed outline-1 hover:ring-2 hover:ring-[#3b82f6]/50 hover:border-[#3b82f6] transition-all rounded-[2px]" value={formData.positive_prompt} onChange={handleChange} placeholder="please input your positive prompt" required disabled={isLoading} />
                        </div>
                        <div className='flex justify-center'>
                            <button type="submit" className="text-sm w-[80%] cursor-pointer bg-gray-300 hover:bg-gray-300/70 hover:-translate-y-0.5 transition-all hover:shadow-sm" disabled={isLoading}>Submit</button>
                        </div>
                        <div className="flex justify-center">
                            <button type="button" className="text-sm w-[80%] cursor-pointer bg-gray-300 hover:bg-gray-300/70 hover:-translate-y-0.5 transition-all hover:shadow-sm" disabled={isLoading} onClick={handleReset}>Reset</button>
                        </div>
                    </form>
                        <div className="absolute bottom-[45px] w-full h-16 flex justify-evenly items-center px-12 bg-gray-100 gap-16">
                            <Link to="/workspace/layer" className="blcok cursor-pointer bg-white hover:bg-gray-300 hover:-translate-y-0.5 transition-all hover:shadow-sm rounded-3xl">
                                <img src="/left_arrow.svg" alt="left_arrow" className="h-10 w-12" />
                            </Link>
                            <Link to="/workspace/svg" className="blcok cursor-not-allowed bg-white hover:bg-gray-300 hover:-translate-y-0.5 transition-all hover:shadow-sm rounded-3xl">
                                <img src="/right_arrow.svg" alt="right_arrow" className="h-10 w-12" />
                            </Link>
                    </div>
                </div>
            )
    }
}