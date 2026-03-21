import React from "react";
import { Metadata } from "next";

export const metadata: Metadata = {
  metadataBase: new URL("https://www.gkaports.com.ng"),
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

export default function Contact() {
  return (
    <main className="pt-24 pb-16">
      <div className="container mx-auto lg:max-w-(--breakpoint-xl) px-4">
        {/* Hero Section */}
        <div className="text-center mb-16 pt-16">
          <h1 className="text-4xl md:text-5xl font-bold text-midnight_text mb-6">
            Contact GK&A Logistics
          </h1>
          <p className="text-xl text-muted max-w-3xl mx-auto">
            Ready to partner with Nigeria's leading maritime infrastructure innovators? Get in touch with our team.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 mb-16">
          {/* Contact Form */}
          <div className="bg-white border border-gray-200 rounded-lg p-8">
            <h2 className="text-2xl font-bold text-grey mb-6">Send us a Message</h2>
            <form className="space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-midnight_text mb-2">Full Name *</label>
                  <input
                    type="text"
                    required
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
                    placeholder="Your full name"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-midnight_text mb-2">Phone Number</label>
                  <input
                    type="tel"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
                    placeholder="+234 xxx xxx xxxx"
                  />
                </div>
              </div>

              <div>
                <label className="block text-sm font-medium text-midnight_text mb-2">Email Address *</label>
                <input
                  type="email"
                  required
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
                  placeholder="your.email@company.com"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-midnight_text mb-2">Subject *</label>
                <select className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent">
                  <option value="">Select a service</option>
                  <option value="port-operations">Port Terminal Operations</option>
                  <option value="cargo-handling">Cargo Handling Services</option>
                  <option value="storage">Storage Solutions</option>
                  <option value="import-export">Import/Export Coordination</option>
                  <option value="customs">Customs Clearance Support</option>
                  <option value="partnership">Partnership Opportunities</option>
                  <option value="other">Other Inquiry</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-midnight_text mb-2">Message *</label>
                <textarea
                  rows={5}
                  required
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
                  placeholder="Tell us about your logistics needs..."
                ></textarea>
              </div>

              <button
                type="submit"
                className="w-full bg-primary text-white py-3 px-6 rounded-lg hover:bg-blue-700 transition-colors font-semibold"
              >
                Send Message
              </button>
            </form>
          </div>

          {/* Contact Information */}
          <div className="space-y-8">
            {/* Primary Contact */}
            <div className="bg-primary text-white rounded-lg p-6">
              <h3 className="text-xl font-bold mb-4">Primary Contact</h3>
              <div className="space-y-3">
                <div className="flex items-center">
                  <span className="text-2xl mr-3">📧</span>
                  <div>
                    <p className="font-semibold">Email</p>
                    <a href="mailto:info@gkaports.com.ng" className="hover:underline">info@gkaports.com.ng</a>
                  </div>
                </div>
                <div className="flex items-center">
                  <span className="text-2xl mr-3">📞</span>
                  <div>
                    <p className="font-semibold">Phone</p>
                    <a href="tel:+2348181927251" className="hover:underline">+234 818 192 7251</a>
                  </div>
                </div>
                <div className="flex items-center">
                  <span className="text-2xl mr-3">🏢</span>
                  <div>
                    <p className="font-semibold">Head Office</p>
                    <p>131 Obafemi Awolowo Way, Alausa, Ikeja, Lagos, Nigeria</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Terminal Facility */}
            <div className="bg-gray-50 border border-gray-200 rounded-lg p-6">
              <h3 className="text-xl font-bold text-midnight_text mb-4">Terminal Facility</h3>
              <div className="space-y-3">
                <div className="flex items-start">
                  <span className="text-2xl mr-3">⚓</span>
                  <div>
                    <p className="font-semibold">NPA Lighter Terminal, Ikorodu</p>
                    <p className="text-muted">20,000 SQM operational facility</p>
                  </div>
                </div>
                <div className="flex items-start">
                  <span className="text-2xl mr-3">🕒</span>
                  <div>
                    <p className="font-semibold">Operating Hours</p>
                    <p className="text-muted">24/7 operations for all cargo types</p>
                  </div>
                </div>
              </div>
            </div>


            {/* Service Addresses */}
            <div className="bg-gray-50 border border-gray-200 rounded-lg p-6">
              <h3 className="text-xl font-bold text-midnight_text mb-4">Service Addresses</h3>
              <div className="space-y-3">
                <div>
                  <p className="font-semibold">Head Office</p>
                  <p className="text-muted">131 Obafemi Awolowo Way, Alausa, Ikeja, Lagos, Nigeria</p>
                </div>
                <div>
                  <p className="font-semibold">Terminal Facility</p>
                  <p className="text-muted">NPA Lighter Terminal, Ikorodu, Lagos</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Map Section */}
        <div className="bg-gray-50 rounded-lg p-8 mb-16">
          <h2 className="text-3xl font-bold text-midnight_text text-center mb-8">Our Locations</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div>
              <h3 className="text-xl font-bold text-midnight_text mb-4">NPA Lighter Terminal, Ikorodu</h3>
              <p className="text-muted mb-4">
                Our operational maritime logistics facility serving Nigeria's import and export activities.
              </p>
              <div className="bg-white border border-gray-200 rounded-lg p-4 h-64">
                <iframe 
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3964.000705206442!2d3.481389!3d6.6!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNsKwMzYnMDAuMCJOIDPCsDI4JzUzLjAiRQ!5e0!3m2!1sen!2sng!4v1650000000000!5m2!1sen!2sng" 
                  width="100%" 
                  height="100%" 
                  style={{ border: 0 }} 
                  allowFullScreen={true} 
                  loading="lazy" 
                  referrerPolicy="no-referrer-when-downgrade"
                  title="NPA Lighter Terminal, Ikorodu Map"
                  className="rounded-lg"
                ></iframe>
              </div>
            </div>

            <div>
              <h3 className="text-xl font-bold text-midnight_text mb-4">Head Office, Ikeja</h3>
              <p className="text-muted mb-4">
                Our corporate headquarters and business development center.
              </p>
              <div className="bg-white border border-gray-200 rounded-lg p-4 h-64">
                <iframe 
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3963.983145340555!2d3.344945314770496!3d6.599961799999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x103b923b3d7d7d7d%3A0x1234567890abcdef!2s131%20Obafemi%20Awolowo%20Way%2C%20Alausa%2C%20Ikeja%2C%20Lagos%2C%20Nigeria!5e0!3m2!1sen!2sng!4v1650000000000!5m2!1sen!2sng" 
                  width="100%" 
                  height="100%" 
                  style={{ border: 0 }} 
                  allowFullScreen={true} 
                  loading="lazy" 
                  referrerPolicy="no-referrer-when-downgrade"
                  title="Head Office, Ikeja Map"
                  className="rounded-lg"
                ></iframe>
              </div>
            </div>
          </div>
        </div>

        {/* Partnership CTA */}
        <div className="text-center bg-primary text-white rounded-lg p-8">
          <h2 className="text-2xl font-bold text-white mb-4">Ready to Partner with GK&A?</h2>
          <p className="mb-6 opacity-90">
            Join us in building Nigeria's future in inland ports and logistics. Whether you're a port operator, investor, or logistics partner, GK&A offers an opportunity to be part of a future-facing logistics solution at scale.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a
              href="mailto:info@gkaports.com.ng"
              className="inline-block bg-white text-primary px-8 py-3 rounded-lg hover:bg-gray-100 transition-colors font-semibold"
            >
              Email Us Directly
            </a>
            <a
              href="tel:+2348181927251"
              className="inline-block border border-white text-white px-8 py-3 rounded-lg hover:bg-white hover:text-primary transition-colors font-semibold"
            >
              Call Now
            </a>
          </div>
        </div>
      </div>
    </main>
  );
}