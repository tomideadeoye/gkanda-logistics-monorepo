import type { Metadata } from "next";

export const metadata: Metadata = {
  metadataBase: new URL("https://www.gkaports.com"),
  title: "Abimbola Okubena - Commercial Director | GK&A Logistics",
  description: "Connect with Abimbola Okubena, Commercial Director of GK&A Logistics Services Ltd.",
  openGraph: {
    title: "Abimbola Okubena - Commercial Director | GK&A Logistics",
    description: "Connect with Abimbola Okubena, Commercial Director of GK&A Logistics Services Ltd.",
    url: "https://www.gkaports.com/commercial-director",
    siteName: "GK&A Logistics",
    images: [{ url: "/gkaassets/gk & a logo.png", width: 1200, height: 630, alt: "GK&A Logistics" }],
    locale: "en_US",
    type: "website",
  },
};

export default function Layout({ children }: { children: React.ReactNode }) {
  return children;
}
