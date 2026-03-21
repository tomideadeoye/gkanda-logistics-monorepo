import ContactForm from "@/components/Contact/Form";
import ContactInfo from "@/components/Contact/ContactInfo";
import Location from "@/components/Contact/OfficeLocation";
import React from "react";
import HeroSub from "@/components/SharedComponents/HeroSub";
import { Metadata } from "next";
export const metadata: Metadata = {
  title: "Contact Us - GK&A Logistics Services Ltd",
  description: "Get in touch with GK&A Logistics Services Ltd. Contact our team for maritime logistics services, partnership opportunities, and port terminal operations at NPA Lighter Terminal, Ikorodu.",
  openGraph: {
    title: "Contact Us - GK&A Logistics Services Ltd",
    description: "Get in touch with GK&A Logistics Services Ltd. Contact our team for maritime logistics services, partnership opportunities, and port terminal operations at NPA Lighter Terminal, Ikorodu.",
    url: "https://www.gkaports.com.ng/contact",
    siteName: "GK&A Logistics",
    images: [
      {
        url: "/gkaassets/gk & a logo.png",
        width: 1200,
        height: 630,
        alt: "GK&A Logistics Contact",
      },
    ],
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Contact Us - GK&A Logistics Services Ltd",
    description: "Get in touch with GK&A Logistics Services Ltd. Contact our team for maritime logistics services, partnership opportunities, and port terminal operations at NPA Lighter Terminal, Ikorodu.",
    images: ["/gkaassets/gk & a logo.png"],
  },
};

const page = () => {
  const breadcrumbLinks = [
    { href: "/", text: "Home" },
    { href: "/contact", text: "Contact" },
  ];
  return (
    <>
      <HeroSub
        title="Contact Us"
        description="Letraset sheets containing Lorem Ipsum passages and more recently with desktop publishing Variou"
        breadcrumbLinks={breadcrumbLinks}
      />
      <ContactInfo />
      <ContactForm />
      <Location />
    </>
  );
};

export default page;
