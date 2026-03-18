"use client";

import Link from "next/link";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Menu, X } from "lucide-react";
import { ThemeToggle } from "@/components/theme-toggle";

export function Navigation() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <nav className="border-b border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link href="/" className="text-xl font-bold">
              GKALogistics
            </Link>
          </div>
          
          {/* Desktop Navigation */}
          <div className="hidden sm:flex items-center space-x-4">
            <Button variant="ghost" asChild>
              <Link href="/">Home</Link>
            </Button>
            <Button variant="ghost" asChild>
              <Link href="/test">Component Tests</Link>
            </Button>
            <Button variant="ghost" asChild>
              <Link href="/wire-mesh">Wire Mesh Calculator</Link>
            </Button>
            <Button variant="ghost" asChild>
              <Link href="/screenshots">Screenshots</Link>
            </Button>
            <ThemeToggle />
          </div>
          
          {/* Mobile menu button */}
          <div className="sm:hidden flex items-center space-x-2">
            <ThemeToggle />
            <Button 
              variant="ghost" 
              size="icon"
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              aria-label="Toggle menu"
            >
              {isMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
            </Button>
          </div>
        </div>
      </div>
      
      {/* Mobile Navigation */}
      {isMenuOpen && (
        <div className="sm:hidden border-t border-gray-200 dark:border-gray-800">
          <div className="px-2 pt-2 pb-3 space-y-1">
            <Button variant="ghost" className="w-full justify-start" asChild>
              <Link href="/" onClick={() => setIsMenuOpen(false)}>
                Home
              </Link>
            </Button>
            <Button variant="ghost" className="w-full justify-start" asChild>
              <Link href="/test" onClick={() => setIsMenuOpen(false)}>
                Component Tests
              </Link>
            </Button>
            <Button variant="ghost" className="w-full justify-start" asChild>
              <Link href="/wire-mesh" onClick={() => setIsMenuOpen(false)}>
                Wire Mesh Calculator
              </Link>
            </Button>
            <Button variant="ghost" className="w-full justify-start" asChild>
              <Link href="/screenshots" onClick={() => setIsMenuOpen(false)}>
                Screenshots
              </Link>
            </Button>
          </div>
        </div>
      )}
    </nav>
  );
}