import type { Metadata } from "next";

export const metadata: Metadata = {
  metadataBase: new URL("https://www.gkaports.com"),
  title: "Omobola Abiru - Managing Director | GK&A Logistics",
  description: "Connect with Omobola Abiru, Managing Director of GK&A Logistics Services Ltd - Nigeria's leading maritime logistics partner at NPA Lighter Terminal, Ikorodu.",
  openGraph: {
    title: "Omobola Abiru - Managing Director | GK&A Logistics",
    description: "Connect with Omobola Abiru, Managing Director of GK&A Logistics Services Ltd - Nigeria's leading maritime logistics partner.",
    url: "https://www.gkaports.com/md",
    siteName: "GK&A Logistics",
    images: [
      {
        url: "/gkaassets/gk & a logo.png",
        width: 1200,
        height: 630,
        alt: "GK&A Logistics - Omobola Abiru",
      },
    ],
    locale: "en_US",
    type: "website",
  },
};

export default function MDLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return children;
}
