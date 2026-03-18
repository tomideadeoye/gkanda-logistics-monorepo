import Link from "next/link";

export function Footer() {
  return (
    <footer className="border-t border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="md:flex md:items-center md:justify-between">
          <div className="flex justify-center md:justify-start">
            <Link href="/" className="text-xl font-bold">
              GKALogistics
            </Link>
          </div>
          <div className="mt-4 md:mt-0 flex justify-center space-x-6">
            <Link href="#" className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300">
              About
            </Link>
            <Link href="#" className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300">
              Contact
            </Link>
            <Link href="#" className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300">
              Privacy
            </Link>
          </div>
        </div>
        <div className="mt-8 text-center text-sm text-gray-500 dark:text-gray-400">
          <p>© {new Date().getFullYear()} GKALogistics. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
}