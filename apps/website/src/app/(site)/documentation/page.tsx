import { Documentation } from "@/components/Documentation/Documentation";
import { Metadata } from "next";
export const metadata: Metadata = {
  title: "Documentation - GK&A Logistics Services Ltd",
  description: "Comprehensive documentation for GK&A Logistics services, procedures, and operational guidelines.",
  openGraph: {
    title: "Documentation - GK&A Logistics Services Ltd",
    description: "Comprehensive documentation for GK&A Logistics services, procedures, and operational guidelines.",
    url: "https://www.gkaports.com.ng/documentation",
    siteName: "GK&A Logistics",
    images: [
      {
        url: "/gkaassets/gk & a logo.png",
        width: 1200,
        height: 630,
        alt: "GK&A Logistics Documentation",
      },
    ],
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Documentation - GK&A Logistics Services Ltd",
    description: "Comprehensive documentation for GK&A Logistics services, procedures, and operational guidelines.",
    images: ["/gkaassets/gk & a logo.png"],
  },
};

export default function Page() {
  return (
    <>
      <Documentation />
    </>
  );
}
