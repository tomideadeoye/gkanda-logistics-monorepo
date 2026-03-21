import Signin from "@/components/Auth/SignIn";
import Breadcrumb from "@/components/Common/Breadcrumb";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Sign In - GK&A Logistics Services Ltd",
  description: "Sign in to your GK&A Logistics account to manage your shipments and track orders.",
  openGraph: {
    title: "Sign In - GK&A Logistics Services Ltd",
    description: "Sign in to your GK&A Logistics account to manage your shipments and track orders.",
    url: "https://www.gkaports.com.ng/signin",
    siteName: "GK&A Logistics",
    images: [
      {
        url: "/gkaassets/gk & a logo.png",
        width: 1200,
        height: 630,
        alt: "GK&A Logistics Sign In",
      },
    ],
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Sign In - GK&A Logistics Services Ltd",
    description: "Sign in to your GK&A Logistics account to manage your shipments and track orders.",
    images: ["/gkaassets/gk & a logo.png"],
  },
};

const SigninPage = () => {
  return (
    <>
      <Breadcrumb pageName="Sign In Page" />

      <Signin />
    </>
  );
};

export default SigninPage;
