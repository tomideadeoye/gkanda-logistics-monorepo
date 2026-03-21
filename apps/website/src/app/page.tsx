import React from "react";
import { Metadata } from "next";
import Hero from "@/components/Home/Hero";
import Payment from "@/components/Home/Payment";
import Benefit  from "@/components/Home/Benefit";
import Spend from "@/components/Home/Spend";
import Method from "@/components/Home/Method";
import Mobile from "@/components/Home/Mobile";
import Search from "@/components/Home/Search";
{/* import Pricing from "@/components/Home/Pricing"; */}
import Solution from "@/components/Home/Solution";

export const metadata: Metadata = {
  title: "GK&A Logistics - Building Nigeria's Future in Inland Ports & Logistics",
  description: "GK&A Logistics Services Ltd - Driving innovation in maritime infrastructure and logistics through two transformative projects in Ikorodu, Lagos.",
  openGraph: {
    title: "GK&A Logistics - Building Nigeria's Future in Inland Ports & Logistics",
    description: "GK&A Logistics Services Ltd - Driving innovation in maritime infrastructure and logistics through two transformative projects in Ikorodu, Lagos.",
    url: "https://www.gkaports.com.ng",
    siteName: "GK&A Logistics",
    images: [
      {
        url: "/gkaassets/gka-logistics-logo.png",
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
    title: "GK&A Logistics - Building Nigeria's Future in Inland Ports & Logistics",
    description: "GK&A Logistics Services Ltd - Driving innovation in maritime infrastructure and logistics through two transformative projects in Ikorodu, Lagos.",
    images: ["/gkaassets/gka-logistics-logo.png"],
  },
};

export default function Home() {
  return (
    <main>
      <Hero />
      <Payment />
      <Benefit />
      <Spend />
      <Method />
      <Mobile />
      <Search />
      {/* <Pricing /> */}
      <Solution />
      
    </main>
  );
}
