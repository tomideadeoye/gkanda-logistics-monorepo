import React from "react";
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

export default function Services() {
  return (
    <main className="pt-24 pb-16">
      <div className="container mx-auto lg:max-w-(--breakpoint-xl) px-4">
        {/* Hero Section */}
        <div className="text-center mb-16 pt-16">
          <h1 className="text-4xl md:text-5xl font-bold text-midnight_text mb-6">
            Maritime Logistics Services
          </h1>
          <p className="text-xl text-muted max-w-3xl mx-auto">
            World-class port terminal operations and comprehensive logistics solutions at NPA Lighter Terminal, Ikorodu
          </p>
        </div>

        {/* Core Services */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
          <div className="bg-white border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow">
            <div className="w-16 h-16 bg-primary rounded-lg flex items-center justify-center mb-4">
              <span className="text-white text-2xl">🏗</span>
            </div>
            <h3 className="text-xl font-bold text-midnight_text mb-3">Port Terminal Operations</h3>
            <p className="text-muted">
              World-class maritime logistics facility at NPA Lighter Terminal with comprehensive cargo handling and processing capabilities.
            </p>
          </div>

          <div className="bg-white border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow">
            <div className="w-16 h-16 bg-primary rounded-lg flex items-center justify-center mb-4">
              <span className="text-white text-2xl">📦</span>
            </div>
            <h3 className="text-xl font-bold text-midnight_text mb-3">Maritime Cargo Handling</h3>
            <p className="text-muted">
              Efficient cargo processing and handling for all types of maritime goods, including containerized and bulk cargo.
            </p>
          </div>

          <div className="bg-white border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow">
            <div className="w-16 h-16 bg-primary rounded-lg flex items-center justify-center mb-4">
              <span className="text-white text-2xl">🏢</span>
            </div>
            <h3 className="text-xl font-bold text-midnight_text mb-3">Secure Storage Solutions</h3>
            <p className="text-muted">
              Climate-controlled warehouse and open stacking areas with comprehensive security infrastructure.
            </p>
          </div>

          <div className="bg-white border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow">
            <div className="w-16 h-16 bg-primary rounded-lg flex items-center justify-center mb-4">
              <span className="text-white text-2xl">🚚</span>
            </div>
            <h3 className="text-xl font-bold text-midnight_text mb-3">Import/Export Coordination</h3>
            <p className="text-muted">
              Comprehensive logistics support for both import and export operations with full documentation assistance.
            </p>
          </div>

          <div className="bg-white border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow">
            <div className="w-16 h-16 bg-primary rounded-lg flex items-center justify-center mb-4">
              <span className="text-white text-2xl">📋</span>
            </div>
            <h3 className="text-xl font-bold text-midnight_text mb-3">Customs Clearance Support</h3>
            <p className="text-muted">
              Documentation and clearance assistance to ensure smooth customs processing for all shipments.
            </p>
          </div>

          <div className="bg-white border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow">
            <div className="w-16 h-16 bg-primary rounded-lg flex items-center justify-center mb-4">
              <span className="text-white text-2xl">🚛</span>
            </div>
            <h3 className="text-xl font-bold text-midnight_text mb-3">Last-Mile Delivery</h3>
            <p className="text-muted">
              Ground transportation services connecting our terminal to final destinations across Lagos and beyond.
            </p>
          </div>
        </div>

        {/* Facility Specifications */}
        <div className="bg-gray-50 rounded-lg p-8 mb-16">
          <h2 className="text-3xl font-bold text-midnight_text text-center mb-8">Terminal Specifications</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div className="text-center">
              <div className="text-3xl font-bold text-primary mb-2">1,232.2m</div>
              <p className="text-muted">Quay Length</p>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-primary mb-2">37,305.84 m²</div>
              <p className="text-muted">Quay Apron Area</p>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-primary mb-2">6,040.83 m²</div>
              <p className="text-muted">Climate-Controlled Warehouse</p>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-primary mb-2">8,871.10 m²</div>
              <p className="text-muted">Paved Stacking Area</p>
            </div>
          </div>
        </div>

        {/* Strategic Advantages */}
        <div className="mb-16">
          <h2 className="text-3xl font-bold text-midnight_text text-center mb-12">Strategic Advantages</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="space-y-6">
              <div className="flex items-start">
                <div className="w-12 h-12 bg-primary rounded-lg flex items-center justify-center mr-4 flex-shrink-0">
                  <span className="text-white text-xl">🚢</span>
                </div>
                <div>
                  <h3 className="text-xl font-bold text-midnight_text mb-2">Direct Maritime Access</h3>
                  <p className="text-muted">Strategic location providing direct access to maritime shipping routes and connectivity to Lagos' extensive road network.</p>
                </div>
              </div>

              <div className="flex items-start">
                <div className="w-12 h-12 bg-primary rounded-lg flex items-center justify-center mr-4 flex-shrink-0">
                  <span className="text-white text-xl">🏭</span>
                </div>
                <div>
                  <h3 className="text-xl font-bold text-midnight_text mb-2">Industrial Proximity</h3>
                  <p className="text-muted">Proximity to major commercial and industrial centers, enabling efficient last-mile delivery and supply chain integration.</p>
                </div>
              </div>
            </div>

            <div className="space-y-6">
              <div className="flex items-start">
                <div className="w-12 h-12 bg-primary rounded-lg flex items-center justify-center mr-4 flex-shrink-0">
                  <span className="text-white text-xl">🛡️</span>
                </div>
                <div>
                  <h3 className="text-xl font-bold text-midnight_text mb-2">Comprehensive Security</h3>
                  <p className="text-muted">784.85 meters of perimeter fencing with multiple access control gates and round-the-clock monitoring systems.</p>
                </div>
              </div>

              <div className="flex items-start">
                <div className="w-12 h-12 bg-primary rounded-lg flex items-center justify-center mr-4 flex-shrink-0">
                  <span className="text-white text-xl">✅</span>
                </div>
                <div>
                  <h3 className="text-xl font-bold text-midnight_text mb-2">International Standards</h3>
                  <p className="text-muted">Compliance with international standards (BS EN, ISO) and Nigerian Building Code requirements.</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Service Process */}
        <div className="bg-primary text-white rounded-lg p-8 mb-16">
          <h2 className="text-3xl font-bold text-center mb-8 text-white">Our Service Process</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="w-16 h-16 bg-white bg-opacity-20 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-2xl">1️⃣</span>
              </div>
              <h3 className="text-xl font-bold mb-3">Booking & Documentation</h3>
              <p className="opacity-90">Secure your shipment slot and complete all necessary documentation for smooth processing.</p>
            </div>
            <div className="text-center">
              <div className="w-16 h-16 bg-white bg-opacity-20 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-2xl">2️⃣</span>
              </div>
              <h3 className="text-xl font-bold mb-3">Cargo Handling & Storage</h3>
              <p className="opacity-90">Professional cargo handling with secure storage solutions tailored to your cargo type.</p>
            </div>
            <div className="text-center">
              <div className="w-16 h-16 bg-white bg-opacity-20 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-2xl">3️⃣</span>
              </div>
              <h3 className="text-xl font-bold mb-3">Delivery & Tracking</h3>
              <p className="opacity-90">Real-time tracking and efficient last-mile delivery to your final destination.</p>
            </div>
          </div>
        </div>

        {/* Contact CTA */}
        <div className="text-center bg-gray-50 rounded-lg p-8">
          <h2 className="text-2xl font-bold text-midnight_text mb-4">Ready to Ship with Us?</h2>
          <p className="text-muted mb-6">
            Experience world-class maritime logistics services at NPA Lighter Terminal, Ikorodu. Contact us for a customized logistics solution.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a
              href="/contact"
              className="inline-block bg-primary text-white px-8 py-3 rounded-lg hover:bg-blue-700 transition-colors"
            >
              Request Quote
            </a>
            <a
              href="/track-trace"
              className="inline-block border border-primary text-primary px-8 py-3 rounded-lg hover:bg-primary hover:text-white transition-colors"
            >
              Track Shipment
            </a>
          </div>
        </div>
      </div>
    </main>
  );
}