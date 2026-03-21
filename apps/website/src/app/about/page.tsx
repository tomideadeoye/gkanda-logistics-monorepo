import React from "react";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "About Us - GK&A Logistics Services Ltd",
  description: "Learn about GK&A Logistics Services Ltd, Nigeria's leading maritime infrastructure and logistics development company, pioneering inland ports and logistics solutions.",
  openGraph: {
    title: "About Us - GK&A Logistics Services Ltd",
    description: "Learn about GK&A Logistics Services Ltd, Nigeria's leading maritime infrastructure and logistics development company, pioneering inland ports and logistics solutions.",
    url: "https://www.gkaports.com.ng/about",
    siteName: "GK&A Logistics",
    images: [
      {
        url: "/gkaassets/about_logi.jpg",
        width: 1200,
        height: 630,
        alt: "GK&A Logistics About Us",
      },
    ],
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "About Us - GK&A Logistics Services Ltd",
    description: "Learn about GK&A Logistics Services Ltd, Nigeria's leading maritime infrastructure and logistics development company, pioneering inland ports and logistics solutions.",
    images: ["/gkaassets/about_logi.jpg"],
  },
};

export default function About() {
  return (
    <main className="pt-24 pb-16">
      <div className="container mx-auto lg:max-w-(--breakpoint-xl) px-4">
        {/* Hero Section */}
        <div className="text-center mb-16 pt-16">
          <h1 className="text-4xl md:text-5xl font-bold text-midnight_text mb-6">
            About GK&A Logistics Services Limited
          </h1>
          <div className="text-xl text-muted max-w-3xl mx-auto leading-loose">
            Building Nigeria's Future in<br />
            Inland Ports & Logistics<br />
            Through Innovation.
          </div>
        </div>

        {/* Company Overview */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 mb-16">
          <div>
            <h2 className="text-3xl font-bold text-midnight_text mb-6">Our Mission</h2>
            <p className="text-lg text-muted mb-6">
              GK&A Logistics Services Limited is a Nigerian-based maritime infrastructure and logistics development company committed to reshaping how goods move across the country. Our mission is to provide world-class logistics solutions through the design, development, and operation of inland ports and related infrastructure that are efficient, sustainable, and economically impactful.
            </p>
            <p className="text-lg text-muted">
              We are currently delivering two key projects that position us at the forefront of Nigeria's inland port evolution—both located in the strategically significant Ikorodu region of Lagos.
            </p>
          </div>
          <div className="bg-gray-50 p-8 rounded-lg">
            <h3 className="text-2xl font-bold text-midnight_text mb-4">Strategic Objectives</h3>
            <ul className="space-y-3">
              <li className="flex items-start">
                <span className="w-2 h-2 bg-primary rounded-full mt-2 mr-3 flex-shrink-0"></span>
                <span className="text-midnight_text dark:text-black">Reduce congestion and turnaround time in Lagos' port ecosystem</span>
              </li>
              <li className="flex items-start">
                <span className="w-2 h-2 bg-primary rounded-full mt-2 mr-3 flex-shrink-0"></span>
                <span className="text-midnight_text dark:text-black">Serve as a transitional platform for future large-scale port activity</span>
              </li>
              <li className="flex items-start">
                <span className="w-2 h-2 bg-primary rounded-full mt-2 mr-3 flex-shrink-0"></span>
                <span className="text-midnight_text dark:text-black">Create jobs and logistics stability in the Ikorodu axis</span>
              </li>
            </ul>
          </div>
        </div>

        {/* Key Projects */}
        <div className="mb-16">
          <h2 className="text-3xl font-bold text-midnight_text text-center mb-12">Our Key Projects</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">

            {/* Project One */}
            <div className="bg-white border border-gray-200 rounded-lg p-8">
              <div className="flex items-center mb-4">
                <div className="w-12 h-12 bg-primary rounded-lg flex items-center justify-center mr-4">
                  <span className="text-white font-bold text-xl">🏗</span>
                </div>
                <h3 className="text-2xl font-bold text-midnight_text">NPA Lighter Terminal Facility</h3>
              </div>
              <p className="text-muted mb-4">
                <strong>Status:</strong> Poised for Immediate Operations
              </p>
              <p className="text-muted mb-6">
                <strong>Location:</strong> NPA Lighter Terminal, Ikorodu - 20,000 square meter lease
              </p>
              <div className="space-y-2">
                <p className="font-semibold">Key Facilities:</p>
                <ul className="list-disc list-inside text-muted space-y-1">
                  <li>EPT Terminal for Empty Container Processing</li>
                  <li>Holding Bay for Truck Staging and Cargo Movement</li>
                  <li>Logistics Services including Cargo Handling & Temporary Storage</li>
                  <li>Operational integration with ongoing port activities</li>
                </ul>
              </div>
            </div>

            {/* Project Two */}
            <div className="bg-white border border-gray-200 rounded-lg p-8">
              <div className="flex items-center mb-4">
                <div className="w-12 h-12 bg-primary rounded-lg flex items-center justify-center mr-4">
                  <span className="text-white font-bold text-xl">⚓</span>
                </div>
                <h3 className="text-2xl font-bold text-midnight_text">Ikorodu Regional Inland Port</h3>
              </div>
              <p className="text-muted mb-4">
                <strong>Status:</strong> Environmental & regulatory approvals secured, reclamation commenced
              </p>
              <p className="text-muted mb-6">
                <strong>Land Area:</strong> 150 Hectares Underway – Expandable to 667 Hectares
              </p>
              <div className="space-y-2">
                <p className="font-semibold">Port Vision Includes:</p>
                <ul className="list-disc list-inside text-muted space-y-1">
                  <li>Full Port Terminal Infrastructure (cargo, container, RoRo)</li>
                  <li>Future rail and highway interconnectivity</li>
                  <li>Industrial Cluster Zones for logistics, finance, and innovation</li>
                  <li>Warehousing and Value-Added Services</li>
                  <li>Digital Innovation & Equipment Manufacturing Hubs</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        {/* Why Partner With Us */}
        <div className="bg-primary text-white rounded-lg p-8 mb-16">
          <h2 className="text-3xl font-bold text-center mb-8 text-white">Why Partner with GK&A?</h2>
          <p className="text-xl text-center mb-8 text-white">
            We are more than developers—we are infrastructure innovators.
          </p>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div className="text-center text-white">
              <div className="text-4xl mb-3">🎯</div>
              <h4 className="font-bold mb-2 text-white">First-mover advantage</h4>
              <p className="text-sm opacity-90 text-white">in Ikorodu's port development</p>
            </div>
            <div className="text-center text-white">
              <div className="text-4xl mb-3">🧱</div>
              <h4 className="font-bold mb-2 text-white">Phased execution model</h4>
              <p className="text-sm opacity-90 text-white">de-risked and strategic</p>
            </div>
            <div className="text-center text-white">
              <div className="text-4xl mb-3">🛂</div>
              <h4 className="font-bold mb-2 text-white">Government approvals</h4>
              <p className="text-sm opacity-90 text-white">and institutional alignment</p>
            </div>
            <div className="text-center text-white">
              <div className="text-4xl mb-3">🤝</div>
              <h4 className="font-bold mb-2 text-white">Strategic partnerships</h4>
              <p className="text-sm opacity-90 text-white">with NPA, NIWA, and key agencies</p>
            </div>
          </div>
        </div>

        {/* Management Team */}
        <div className="mb-16">
          <h2 className="text-3xl font-bold text-midnight_text text-center mb-12">Management Team</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="w-32 h-32 bg-gray-200 rounded-full mx-auto mb-4 flex items-center justify-center">
                <span className="text-4xl">👤</span>
              </div>
              <h3 className="text-xl font-bold text-midnight_text mb-2">Omobola Abiru</h3>
              <p className="text-primary font-semibold mb-2">Managing Director</p>
              <p className="text-muted">Leading GK&A's vision for Nigeria's inland port development</p>
            </div>
            <div className="text-center">
              <div className="w-32 h-32 bg-gray-200 rounded-full mx-auto mb-4 flex items-center justify-center">
                <span className="text-4xl">👤</span>
              </div>
              <h3 className="text-xl font-bold text-midnight_text mb-2">Adegboriaye Moshood Abiru</h3>
              <p className="text-primary font-semibold mb-2">Key Personnel</p>
              <p className="text-muted">Supporting operational excellence and strategic initiatives</p>
            </div>
            <div className="text-center">
              <div className="w-32 h-32 bg-gray-200 rounded-full mx-auto mb-4 flex items-center justify-center">
                <span className="text-4xl">👤</span>
              </div>
              <h3 className="text-xl font-bold text-midnight_text mb-2">Bamidele Addy Abiru</h3>
              <p className="text-primary font-semibold mb-2">Company Secretary</p>
              <p className="text-muted">Ensuring regulatory compliance and corporate governance</p>
            </div>
          </div>
        </div>

        {/* Contact CTA */}
        <div className="text-center bg-gray-50 rounded-lg p-8">
          <h2 className="text-2xl font-bold text-white mb-4">Ready to Partner with Us?</h2>
          <p className="text-muted mb-6">
            Join us in building Nigeria's future in inland ports and logistics. Contact us to discuss partnership opportunities.
          </p>
          <a
            href="/contact"
            className="inline-block bg-primary text-white px-8 py-3 rounded-lg hover:bg-blue-700 transition-colors"
          >
            Request Meeting
          </a>
        </div>
      </div>
    </main>
  );
}