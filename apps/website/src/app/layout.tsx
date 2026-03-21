import { DM_Sans } from "next/font/google";
import "./globals.css";
import Header from "@/components/Layout/Header";
import Footer from "@/components/Layout/Footer";
import { ThemeProvider } from "next-themes";
import { AuthDialogProvider } from "./context/AuthDialogContext";
import ScrollToTop from "@/components/ScrollToTop";
import type { Metadata } from 'next';
const dmsans = DM_Sans({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: 'GK&A Logistics - Maritime Infrastructure & Logistics Development',
  description: 'GK&A Logistics Services Ltd - Nigeria\'s leading maritime infrastructure and logistics development company, pioneering inland ports and logistics solutions.',
  openGraph: {
    title: 'GK&A Logistics - Maritime Infrastructure & Logistics Development',
    description: 'GK&A Logistics Services Ltd - Nigeria\'s leading maritime infrastructure and logistics development company, pioneering inland ports and logistics solutions.',
    url: 'https://www.gkaports.com.ng',
    siteName: 'GK&A Logistics',
    images: [
      {
        url: '/gkaassets/gk & a logo.png',
        width: 1200,
        height: 630,
        alt: 'GK&A Logistics Services',
      },
    ],
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'GK&A Logistics - Maritime Infrastructure & Logistics Development',
    description: 'GK&A Logistics Services Ltd - Nigeria\'s leading maritime infrastructure and logistics development company, pioneering inland ports and logistics solutions.',
    images: ['/gkaassets/gk & a logo.png'],
  },
  icons: {
    icon: '/favicon/favicon.ico',
    shortcut: '/favicon/favicon.ico',
    apple: '/favicon/apple-touch-icon.png',
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={`${dmsans.className}`}>
        <AuthDialogProvider>
          <ThemeProvider
            attribute="class"
            enableSystem={false}
            defaultTheme="light"
          >
            <Header />
            {children}
            <Footer />
            <ScrollToTop />
          </ThemeProvider>
        </AuthDialogProvider>
      </body>
    </html>
  );
}
