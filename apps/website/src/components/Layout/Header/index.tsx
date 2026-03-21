"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { headerData } from "../Header/Navigation/menuData";
import Logo from "./Logo";
import HeaderLink from "../Header/Navigation/HeaderLink";
import MobileHeaderLink from "../Header/Navigation/MobileHeaderLink";
import Signin from "@/components/Auth/SignIn";
import SignUp from "@/components/Auth/SignUp";
import { Icon } from "@iconify/react";
import { useTheme } from "next-themes";
import { SunIcon, MoonIcon } from "@heroicons/react/24/solid";

const Header: React.FC = () => {
  const pathUrl = usePathname();
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  const [navbarOpen, setNavbarOpen] = useState(false);
  const [sticky, setSticky] = useState(false);
  const [isSignInOpen, setIsSignInOpen] = useState(false);
  const [isSignUpOpen, setIsSignUpOpen] = useState(false);

  const navbarRef = useRef<HTMLDivElement>(null);
  const signInRef = useRef<HTMLDivElement>(null);
  const signUpRef = useRef<HTMLDivElement>(null);
  const mobileMenuRef = useRef<HTMLDivElement>(null);

  // When mounted, set the mounted state to true
  useEffect(() => {
    setMounted(true);
  }, []);

  // Function to handle scroll to set sticky class
  const handleScroll = () => {
    setSticky(window.scrollY >= 80);
  };

  // Function to handle click outside
  const handleClickOutside = (event: MouseEvent) => {
    if (
      signInRef.current &&
      !signInRef.current.contains(event.target as Node)
    ) {
      setIsSignInOpen(false);
    }
    if (
      signUpRef.current &&
      !signUpRef.current.contains(event.target as Node)
    ) {
      setIsSignUpOpen(false);
    }
    if (
      mobileMenuRef.current &&
      !mobileMenuRef.current.contains(event.target as Node) &&
      navbarOpen
    ) {
      setNavbarOpen(false);
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", handleScroll);
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      window.removeEventListener("scroll", handleScroll);
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [navbarOpen, isSignInOpen, isSignUpOpen]);

  // Effect to handle body overflow
  useEffect(() => {
    if (isSignInOpen || isSignUpOpen || navbarOpen) {
      document.body.style.overflow = "hidden"; // Prevent scrolling
    } else {
      document.body.style.overflow = ""; // Reset scrolling
    }
  }, [isSignInOpen, isSignUpOpen, navbarOpen]);

  // Don't render the theme toggle until mounted to avoid hydration mismatch
  const renderThemeToggle = () => {
    if (!mounted) {
      return (
        <button
          aria-label="Toggle theme"
          className="flex h-8 w-8 items-center justify-center text-body-color duration-300"
        >
          <SunIcon className="h-6 w-6 text-white" />
        </button>
      );
    }

    return (
      <button
        aria-label="Toggle theme"
        onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
        className="flex h-8 w-8 items-center justify-center text-body-color duration-300"
      >
        {theme === "dark" ? (
          <SunIcon className="h-6 w-6 text-white" />
        ) : (
          <MoonIcon className="h-6 w-6 text-white" />
        )}
      </button>
    );
  };

  return (
    <header
      className={`fixed h-28 top-0 py-2 z-50 w-full transition-all ${
        sticky 
          ? "shadow-lg bg-darkheader" 
          : "shadow-none bg-darkheader"
      }`}
    >
      <div className="container mx-auto lg:max-w-(--breakpoint-xl) md:max-w-(--breakpoint-md) flex justify-between lg:items-center xl:gap-16 lg:gap-8 px-4 py-6">
        <div className="">
          <Logo />
        </div>
        <nav className="hidden lg:flex grow items-center xl:justify-start justify-center space-x-10 text-17 text-white">
          {headerData.map((item, index) => (
            <HeaderLink key={index} item={item} />
          ))}
        </nav>
        <div className="flex items-center gap-4">
          {renderThemeToggle()}
          <Link
            href="/contact"
            className="hidden lg:flex items-center bg-primary border border-primary text-white px-4 py-2 gap-2 rounded-lg text-16 font-semibold hover:bg-transparent hover:text-primary"
          >
            Contact Sales
            <Icon icon="solar:arrow-right-linear" width="24" height="24" />
          </Link>
          {isSignInOpen && (
            <div
              ref={signInRef}
              className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex items-center justify-center z-50 m-0"
            >
              <div className="relative mx-auto w-full max-w-md overflow-hidden rounded-lg bg-white px-8 py-14 text-center">
                <button
                  onClick={() => setIsSignInOpen(false)}
                  className="bg-[url('/images/icon/closed.svg')] bg-no-repeat bg-contain w-5 h-5 absolute top-0 right-0 mr-8 mt-8"
                  aria-label="Close Sign In Modal"
                ></button>
                <Signin />
              </div>
            </div>
          )}
          {/* 
          <Link
            href="/track-trace"
            className="hidden lg:flex items-center border border-primary bg-transparent text-primary px-4 py-2 gap-2 rounded-lg text-16 font-semibold hover:bg-primary hover:text-white"
          >
            Track Shipment
            <Icon icon="solar:arrow-right-linear" width="24" height="24" />
          </Link>
          */}
          {isSignUpOpen && (
            <div
              ref={signUpRef}
              className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex items-center justify-center z-50"
            >
              <div className="relative mx-auto w-full max-w-md overflow-hidden rounded-lg bg-white px-8 py-14 text-center">
                <button
                  onClick={() => setIsSignUpOpen(false)}
                  className="bg-[url('/images/icon/closed.svg')] bg-no-repeat bg-contain w-5 h-5 absolute top-0 right-0 mr-8 mt-8"
                  aria-label="Close Sign Up Modal"
                ></button>
                <SignUp />
              </div>
            </div>
          )}
          <button
            onClick={() => setNavbarOpen(!navbarOpen)}
            className="block lg:hidden p-2 rounded-lg"
            aria-label="Toggle mobile menu"
          >
            <span className="block w-6 h-0.5 bg-white"></span>
            <span className="block w-6 h-0.5 bg-white mt-1.5"></span>
            <span className="block w-6 h-0.5 bg-white mt-1.5"></span>
          </button>
        </div>
      </div>
      <div
        ref={mobileMenuRef}
        className={`lg:hidden fixed top-0 right-0 h-full w-full bg-darkheader shadow-lg transform transition-transform duration-300 max-w-xs ${
          navbarOpen ? "-translate-x-0" : "translate-x-full"
        }`}
      >
        <div className="flex items-center justify-between p-4">
          <h2 className="text-lg font-bold text-white">
            Menu
          </h2>
          <button
            onClick={() => setNavbarOpen(false)}
            aria-label="Close mobile menu"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              className="text-white"
            >
              <path
                fill="none"
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
        <nav className="flex flex-col items-start p-4">
          {headerData.map((item, index) => (
            <MobileHeaderLink key={index} item={item} />
          ))}
          <div className="mt-4 flex flex-col space-y-4 w-full">
            <Link
              href="/contact"
              className="bg-transparent border border-primary text-white px-4 py-2 rounded-lg hover:bg-primary"
              onClick={() => {
                setNavbarOpen(false); // Close the mobile menu
              }}
            >
              Contact Sales
            </Link>
            {/* 
            <Link
              href="/track-trace"
              className="bg-primary text-white px-4 py-2 rounded-lg hover:bg-blue-700"
              onClick={() => {
                setNavbarOpen(false); // Close the mobile menu
              }}
            >
              Track Shipment
            </Link>
            */}
          </div>
        </nav>
      </div>
    </header>
  );
};

export default Header;