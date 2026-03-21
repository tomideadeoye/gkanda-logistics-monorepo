import HeroSub from "@/components/SharedComponents/HeroSub";
import Payment from "@/components/Home/Payment";
import Benefit from "@/components/Home/Benefit";
import Spend from "@/components/Home/Spend";
import { Metadata } from "next";
export const metadata: Metadata = {
  title: "Services - GK&A Logistics Services Ltd",
  description: "Comprehensive maritime logistics services including port terminal operations, cargo handling, secure storage, and import/export coordination at NPA Lighter Terminal, Ikorodu.",
  openGraph: {
    title: "Services - GK&A Logistics Services Ltd",
    description: "Comprehensive maritime logistics services including port terminal operations, cargo handling, secure storage, and import/export coordination at NPA Lighter Terminal, Ikorodu.",
    url: "https://www.gkaports.com.ng/services",
    siteName: "GK&A Logistics",
    images: [
      {
        url: "/gkaassets/GKA-Rail-Connectivity-pdf-image-001.jpg",
        width: 1200,
        height: 630,
        alt: "GK&A Logistics Services",
      },
    ],
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Services - GK&A Logistics Services Ltd",
    description: "Comprehensive maritime logistics services including port terminal operations, cargo handling, secure storage, and import/export coordination at NPA Lighter Terminal, Ikorodu.",
    images: ["/gkaassets/GKA-Rail-Connectivity-pdf-image-001.jpg"],
  },
};

const Services = () => {
  const breadcrumbLinks = [
    { href: "/", text: "Home" },
    { href: "/services", text: "Services" },
  ];
  return (
    <>
      <HeroSub
        title="Services"
        description="Discover a wealth of insightful materials meticulously crafted to provide you with a comprehensive understanding of the latest trends."
        breadcrumbLinks={breadcrumbLinks}
      />
      <Payment />
      <Benefit />
      <Spend />
    </>
  );
};

export default Services;
