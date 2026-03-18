import Image from "next/image";
import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function ScreenshotPage() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 p-4 md:p-8">
      <main className="max-w-6xl mx-auto py-12">
        <div className="text-center mb-12">
          <h1 className="text-3xl font-bold tracking-tight mb-4">Screenshot Display</h1>
          <p className="text-lg text-gray-600 dark:text-gray-300 mb-6">
            Displaying the screenshot from the docs folder
          </p>
          <Button asChild>
            <Link href="/">← Back to Home</Link>
          </Button>
        </div>

        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-4 md:p-8">
          <div className="relative w-full h-auto">
            <Image
              src="/Screenshot 2025-09-30 at 03.58.37.png"
              alt="Screenshot from docs folder"
              width={1920}
              height={1080}
              className="w-full h-auto rounded-lg"
              priority
            />
          </div>
        </div>

        <div className="mt-8 text-center text-sm text-gray-500 dark:text-gray-400">
          <p>Screenshot from /docs/Screenshot 2025-09-30 at 03.58.37.png</p>
        </div>
      </main>
    </div>
  );
}