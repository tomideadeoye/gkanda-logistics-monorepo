import Image from "next/image";
import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function Screenshots() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 p-4 md:p-8">
      <main className="max-w-6xl mx-auto py-12">
        <div className="text-center mb-12">
          <h1 className="text-3xl font-bold tracking-tight mb-4">Screenshots</h1>
          <p className="text-lg text-gray-600 dark:text-gray-300 mb-6">
            View the original screenshots from the documentation
          </p>
          <Button asChild>
            <Link href="/">← Back to Home</Link>
          </Button>
        </div>

        <div className="space-y-12">
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
            <h2 className="text-xl font-semibold mb-4 text-center">Screenshot 1</h2>
            <div className="relative w-full h-auto">
              <Image
                src="/Screenshot 2025-09-30 at 03.58.37.png"
                alt="Screenshot 1"
                width={1920}
                height={1080}
                className="w-full h-auto rounded-lg"
              />
            </div>
          </div>

          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
            <h2 className="text-xl font-semibold mb-4 text-center">Screenshot 2</h2>
            <div className="relative w-full h-auto">
              <Image
                src="/Screenshot 2025-09-30 at 04.05.43.png"
                alt="Screenshot 2"
                width={1920}
                height={1080}
                className="w-full h-auto rounded-lg"
              />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}