import SignUp from "@/components/Auth/SignUp";
import Breadcrumb from "@/components/Common/Breadcrumb";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Sign Up - GK&A Logistics Services Ltd",
  description: "Create an account with GK&A Logistics to access our services and track your shipments.",
  openGraph: {
    title: "Sign Up - GK&A Logistics Services Ltd",
    description: "Create an account with GK&A Logistics to access our services and track your shipments.",
    url: "https://www.gkaports.com.ng/signup",
    siteName: "GK&A Logistics",
    images: [
      {
        url: "/gkaassets/gk & a logo.png",
        width: 1200,
        height: 630,
        alt: "GK&A Logistics Sign Up",
      },
    ],
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Sign Up - GK&A Logistics Services Ltd",
    description: "Create an account with GK&A Logistics to access our services and track your shipments.",
    images: ["/gkaassets/gk & a logo.png"],
  },
};

const SignupPage = () => {
  return (
    <>
      <Breadcrumb pageName="Sign Up Page" />

      <SignUp />
    </>
  );
};

export default SignupPage;
