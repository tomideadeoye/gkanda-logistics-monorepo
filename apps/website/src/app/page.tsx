"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 p-4 md:p-8">
      <main className="max-w-4xl mx-auto py-12">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold tracking-tight mb-4">Welcome to Next.js + ShadCN UI</h1>
          <p className="text-lg text-gray-600 dark:text-gray-300">
            A modern web application built with Next.js, TypeScript, Tailwind CSS, and ShadCN UI components
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <Card>
            <CardHeader>
              <CardTitle>Get Started</CardTitle>
              <CardDescription>Begin building your application</CardDescription>
            </CardHeader>
            <CardContent>
              <p className="mb-4">
                This project includes the following technologies:
              </p>
              <ul className="list-disc pl-5 space-y-2">
                <li>Next.js 14+ with App Router</li>
                <li>TypeScript</li>
                <li>Tailwind CSS</li>
                <li>ShadCN UI Components</li>
              </ul>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Try Components</CardTitle>
              <CardDescription>Interactive examples</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <Label htmlFor="email">Email</Label>
                <Input id="email" type="email" placeholder="Enter your email" />
              </div>
              <div className="flex gap-4 pt-2">
                <Button>Primary</Button>
                <Button variant="secondary">Secondary</Button>
              </div>
            </CardContent>
          </Card>
        </div>

        <div className="mt-12">
          <h2 className="text-2xl font-bold text-center mb-6">Project Pages</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <Button asChild>
              <Link href="/test">Component Tests</Link>
            </Button>
            <Button asChild>
              <Link href="/wire-mesh">Wire Mesh Calculator</Link>
            </Button>
            <Button asChild variant="secondary">
              <Link href="/screenshot-comparison">Screenshot Comparison</Link>
            </Button>
          </div>
        </div>

        <div className="mt-8">
          <h2 className="text-2xl font-bold text-center mb-6">HTML Versions</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <Button asChild variant="outline">
              <Link href="/html-versions/original-design.html" target="_blank">Original Design</Link>
            </Button>
            <Button asChild variant="outline">
              <Link href="/html-versions/improved-version.html" target="_blank">Improved Version</Link>
            </Button>
            <Button asChild variant="outline">
              <Link href="/html-versions/comparison.html" target="_blank">Comparison</Link>
            </Button>
          </div>
        </div>

        <div className="mt-12 text-center space-y-4">
          <Button size="lg" asChild>
            <a 
              href="https://ui.shadcn.com/docs" 
              target="_blank" 
              rel="noopener noreferrer"
              className="inline-flex items-center"
            >
              View ShadCN Documentation
            </a>
          </Button>
        </div>
      </main>
      
      <footer className="max-w-4xl mx-auto mt-16 py-8 border-t border-gray-200 dark:border-gray-800 text-center text-sm text-gray-500 dark:text-gray-400">
        <p>Built with Next.js, TypeScript, Tailwind CSS, and ShadCN UI</p>
      </footer>
    </div>
  );
}