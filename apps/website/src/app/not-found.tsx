import NotFound from "@/components/NotFound";
import HeroSub from "@/components/SharedComponents/HeroSub";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Page Not Found - GK&A Logistics Services Ltd",
  description: "The page you're looking for doesn't exist. Return to our homepage to find the information you need.",
  openGraph: {
    title: "Page Not Found - GK&A Logistics Services Ltd",
    description: "The page you're looking for doesn't exist. Return to our homepage to find the information you need.",
    url: "https://www.gkaports.com.ng/404",
    siteName: "GK&A Logistics",
    images: [
      {
        url: "/gkaassets/gk & a logo.png",
        width: 1200,
        height: 630,
        alt: "GK&A Logistics 404",
      },
    ],
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Page Not Found - GK&A Logistics Services Ltd",
    description: "The page you're looking for doesn't exist. Return to our homepage to find the information you need.",
    images: ["/gkaassets/gk & a logo.png"],
  },
};

const ErrorPage = () => {
  const breadcrumbLinks = [
    { href: "/", text: "Home" },
    { href: "/contact", text: "404" },
  ];
  return (
    <>
      <HeroSub
        title="404"
        description="We Can't Seem to Find The Page You're Looking For"
        breadcrumbLinks={breadcrumbLinks}
      />
      <NotFound />
    </>
  );
};

export default ErrorPage;
