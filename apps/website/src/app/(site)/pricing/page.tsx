import Pricing from "@/components/Home/Pricing";
import HeroSub from "@/components/SharedComponents/HeroSub";
import React from "react";
import { Metadata } from "next";
export const metadata: Metadata = {
  title: "Pricing - GK&A Logistics Services Ltd",
  description: "Transparent pricing for maritime logistics services including port terminal operations, cargo handling, storage solutions, and import/export coordination.",
  openGraph: {
    title: "Pricing - GK&A Logistics Services Ltd",
    description: "Transparent pricing for maritime logistics services including port terminal operations, cargo handling, storage solutions, and import/export coordination.",
    url: "https://www.gkaports.com.ng/pricing",
    siteName: "GK&A Logistics",
    images: [
      {
        url: "/gkaassets/gk & a logo.png",
        width: 1200,
        height: 630,
        alt: "GK&A Logistics Pricing",
      },
    ],
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Pricing - GK&A Logistics Services Ltd",
    description: "Transparent pricing for maritime logistics services including port terminal operations, cargo handling, storage solutions, and import/export coordination.",
    images: ["/gkaassets/gk & a logo.png"],
  },
};

const page = () => {
  const breadcrumbLinks = [
    { href: "/", text: "Home" },
    { href: "/pricing", text: "Pricing" },
  ];
  return (
    <>
      <HeroSub
        title="Pricing"
        description="Whether you're an individual, a small team, or a growing enterprise, we have a plan that aligns perfectly with your goals."
        breadcrumbLinks={breadcrumbLinks}
      />
      <Pricing />
    </>
  );
};

export default page;
