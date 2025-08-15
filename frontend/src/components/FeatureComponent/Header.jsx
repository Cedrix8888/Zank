import { Link } from 'react-router-dom';
'use client'

export default function Header() {
    return (
        <header className="fixed border-b-gray-400 inset-x-0 top-0 z-50 bg-white">
            <nav className="flex items-center justify-between px-8">
                <Link to="/" className='flex'>
                    <img src="/favicon.svg" alt="Zank Logo" className="h-8 w-8" />
                    <p className="font-serif text-[16px] text-black font-semibold pt-[10px] pl-1">Zank</p>
                </Link>
                <div className="flex gap-x-36 pr-10">
                    <a href="#" className="text-[19px] px-8 py-1 text-black font-semibold inline-block transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-sm">Features</a>
                    <a href="#" className="text-[19px] px-8 py-1 text-black font-semibold inline-block transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-sm">Gallery</a>
                </div>
                <a href="#" className="flex justify-end py-1 -mr-8 pl-4 transition-all hover:bg-[#fefefe] hover:-translate-y-0.25 hover:shadow-sm">
                    <p className="text-[17px] text-black font-semibold font-mono tracking-tight">Login</p>
                    <img src="/right_arrow.svg" alt="right_arrow" className="h-6 w-6" />
                </a>
            </nav>
        </header>
    );
}