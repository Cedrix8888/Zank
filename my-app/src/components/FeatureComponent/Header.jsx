'use client'

export default function Header() {
    return (
        <header className="fixed border-b-gray-200 inset-x-0 top-0 z-50 bg-white">
            <nav className="flex items-center justify-between pt- px-8">
                <a href="#">
                    <img src="/zank.svg" alt="Zank Logo" className="h-8 w-8" />
                </a>
                <div className="flex gap-x-12">
                    <a href="#" className="text-sm/6 font-semibold text-gray-900">Features</a>
                    <a href="#" className="text-sm/6 font-semibold text-gray-900">Gallery</a>
                </div>
                <div className="flex flex-1 justify-end">
                    <a href="#" className="text-sm/6 font-semibold text-gray-900">Log in</a>
                </div>
            </nav>
        </header>
    );
}