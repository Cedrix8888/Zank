'use client'

export default function Header() {
    return (
        <header className="fixed border-b-[0.5px] border-gray-200 inset-x-0 top-0 z-50">
            <nav className="flex items-center justify-between px-8">
                <div className="flex flex-1">
                    <a href="#" className="-m-1.5 p-1.5">
                        <img src="/zank.svg" alt="" className="h-8 w-auto" />
                    </a>
                </div>
                <div className="flex gap-x-12">
                    <a href="#" class="text-sm/6 font-semibold text-gray-900">Features</a>
                    <a href="#" class="text-sm/6 font-semibold text-gray-900">Gallery</a>
                </div>
                <div class="flex flex-1 justify-end">
                    <a href="#" class="text-sm/6 font-semibold text-gray-900">Log in</a>
                </div>
            </nav>
        </header>
    );
}