import React from "react";
import BlogList from "@/components/Blog/BlogList";
import HeroSub from "@/components/SharedComponents/HeroSub";
import { Metadata } from "next";
export const metadata: Metadata = {
  title: "Blog - GK&A Logistics Services Ltd",
  description: "Latest news, updates, and insights about logistics, maritime operations, and infrastructure development from GK&A Logistics.",
  openGraph: {
    title: "Blog - GK&A Logistics Services Ltd",
    description: "Latest news, updates, and insights about logistics, maritime operations, and infrastructure development from GK&A Logistics.",
    url: "https://www.gkaports.com.ng/blog",
    siteName: "GK&A Logistics",
    images: [
      {
        url: "/gkaassets/bernd-dittrich-LKvT6sCkuPU-unsplash-scaled.jpg",
        width: 1200,
        height: 630,
        alt: "GK&A Logistics Blog",
      },
    ],
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Blog - GK&A Logistics Services Ltd",
    description: "Latest news, updates, and insights about logistics, maritime operations, and infrastructure development from GK&A Logistics.",
    images: ["/gkaassets/bernd-dittrich-LKvT6sCkuPU-unsplash-scaled.jpg"],
  },
};

const Page = () => {
  const breadcrumbLinks = [
    { href: "/", text: "Home" },
    { href: "/blog", text: "Blog" },
  ];
  return (
    <>
      <HeroSub
        title="Blog"
         description=""
        breadcrumbLinks={breadcrumbLinks}  
         />
      <BlogList />
    </>
  );
};

export default Page;
