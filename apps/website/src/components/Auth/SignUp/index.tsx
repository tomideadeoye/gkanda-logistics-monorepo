"use client";
import Link from "next/link";
import { useRouter } from "next/navigation";
import toast from "react-hot-toast";
import Logo from "@/components/Layout/Header/Logo"
import { useState } from "react";
import Loader from "@/components/Common/Loader";
const SignUp = () => {
  const router = useRouter();
  const [loading, setLoading] = useState(false);

  const handleSubmit = (e: any) => {
    e.preventDefault();

    setLoading(true);
    const data = new FormData(e.currentTarget);
    const value = Object.fromEntries(data.entries());
    const finalData = { ...value };

    // Mock registration - replace with your actual registration logic
    setTimeout(() => {
      toast.success("Successfully registered");
      setLoading(false);
      router.push("/signin");
    }, 1000);
  };

  return (
    <>
      <div className="mb-10 text-center mx-auto inline-block max-w-[160px]">
        <Logo />
      </div>

      <span className="z-1 relative my-8 block text-center">
        <span className="-z-1 absolute left-0 top-1/2 block h-px w-full bg-border"></span>
        <span className="text-body-secondary relative z-10 inline-block bg-white px-3 text-base">
          Sign Up
        </span>
      </span>

      <form onSubmit={handleSubmit}>
        <div className="mb-[22px]">
          <input
            type="text"
            placeholder="Name"
            name="name"
            required
            className="w-full rounded-md border border-border border-solid bg-transparent px-5 py-3 text-base text-dark outline-hidden transition placeholder:text-grey focus:border-primary focus-visible:shadow-none"
          />
        </div>
        <div className="mb-[22px]">
          <input
            type="email"
            placeholder="Email"
            name="email"
            required
            className="w-full rounded-md border border-border border-solid bg-transparent px-5 py-3 text-base text-dark outline-hidden transition placeholder:text-grey focus:border-primary focus-visible:shadow-none"
          />
        </div>
        <div className="mb-[22px]">
          <input
            type="password"
            placeholder="Password"
            name="password"
            required
            className="w-full rounded-md border border-border border-solid bg-transparent px-5 py-3 text-base text-dark outline-hidden transition placeholder:text-grey focus:border-primary focus-visible:shadow-none"
          />
        </div>
        <div className="mb-9">
          <button
            type="submit"
            className="flex w-full cursor-pointer items-center justify-center rounded-md bg-primary px-5 py-3 text-base text-white transition duration-300 ease-in-out hover:bg-blue-700"
          >
            Sign Up {loading && <Loader />}
          </button>
        </div>
      </form>

      <p className="text-body-secondary mb-4 text-base">
        By creating an account you are agree with our
        <a href="/#" className="text-primary hover:underline">
          Privacy
        </a>
        and
        <a href="/#" className="text-primary hover:underline">
          Policy
        </a>
      </p>

      <p className="text-body-secondary text-base">
        Already have an account?
        <Link
          href="/"
          className="pl-2 text-primary hover:underline"
        >
          Sign In
        </Link>
      </p>
    </>
  );
};

export default SignUp;