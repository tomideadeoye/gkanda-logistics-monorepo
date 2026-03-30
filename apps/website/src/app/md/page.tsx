"use client";

import React, { useEffect } from "react";
import Image from "next/image";
import Link from "next/link";

const vCardData = `BEGIN:VCARD
VERSION:3.0
N:Abiru;Omobola;;;
FN:Omobola Abiru
TITLE:Managing Director
ORG:GK&A Logistics Services Ltd
ORG;TYPE=2:GK&A Terminal Harbour Limited
ORG;TYPE=3:GK&A Port Infrastructure PTE. LTD.
TEL;TYPE=CELL:+2347038341611
TEL;TYPE=WORK:+2348108627165
TEL;TYPE=OTHER:+2348184082911
EMAIL;TYPE=WORK:mobolaabiru@gkaports.com
URL:https://www.gkaports.com
NOTE:Your Cargo. Her Gateway. | Strategic. Connected. Trusted. | Lagos, Nigeria
END:VCARD`;

function downloadVCard() {
  const blob = new Blob([vCardData], { type: "text/vcard" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "Omobola_Abiru.vcf";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

export default function MDigitalCard() {
  useEffect(() => {
    // Hide main header/footer and set body to allow full-viewport content
    document.body.style.margin = "0";
    document.body.style.padding = "0";
    document.body.style.overflow = "auto";
    
    const header = document.querySelector("header");
    const footer = document.querySelector("footer");
    if (header) header.style.display = "none";
    if (footer) footer.style.display = "none";

    return () => {
      if (header) header.style.display = "";
      if (footer) footer.style.display = "";
    };
  }, []);

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-800 via-slate-700 to-slate-900 px-4 py-8">
      <div className="w-full max-w-2xl mx-auto">
        <div className="bg-white rounded-2xl shadow-2xl overflow-hidden">
          {/* Logo Header */}
          <div className="bg-white px-8 py-6 text-center border-b border-gray-200">
            <Link href="/">
              <Image
                src="/gk & a logo.png"
                alt="GK&A Logistics Logo"
                width={160}
                height={50}
                className="mx-auto"
              />
            </Link>
          </div>

          {/* Profile */}
          <div className="px-8 py-10">
            <div className="text-center mb-8">
              <div className="w-28 h-28 mx-auto bg-primary rounded-full flex items-center justify-center mb-4">
                <span className="text-5xl text-white font-bold">OA</span>
              </div>
              <h1 className="text-3xl font-bold text-gray-900 mb-2">
                Omobola Abiru
              </h1>
              <p className="text-xl text-primary font-semibold">
                Managing Director
              </p>
              <p className="text-gray-500 mt-1">
                GK&A Logistics Services Ltd
              </p>
            </div>

            {/* Company Info */}
            <div className="bg-slate-50 rounded-xl p-6 mb-8 text-center">
              <p className="text-gray-700 leading-relaxed">
                Nigeria&apos;s premier maritime logistics partner at{" "}
                <span className="font-semibold text-primary">NPA Lighter Terminal, Ikorodu</span>.
                Connecting Nigerian businesses to global markets through world-class port operations and strategic logistics solutions.
              </p>
            </div>

            {/* Contact Buttons */}
            <div className="space-y-4 mb-8">
              <a
                href="tel:+2347038341611"
                className="flex items-center justify-center gap-3 bg-primary text-white py-4 px-6 rounded-xl hover:bg-blue-700 transition-all font-semibold"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                </svg>
                Call: +234 703 834 1611
              </a>

              <a
                href="https://wa.me/2347038341611"
                className="flex items-center justify-center gap-3 bg-green-500 text-white py-4 px-6 rounded-xl hover:bg-green-600 transition-all font-semibold"
              >
                <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
                </svg>
                WhatsApp
              </a>

              <a
                href="mailto:mobolaabiru@gkaports.com"
                className="flex items-center justify-center gap-3 bg-slate-800 text-white py-4 px-6 rounded-xl hover:bg-slate-700 transition-all font-semibold"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                Email
              </a>

              <button
                onClick={downloadVCard}
                className="w-full flex items-center justify-center gap-3 bg-gradient-to-r from-blue-600 to-blue-800 text-white py-4 px-6 rounded-xl hover:from-blue-700 hover:to-blue-900 transition-all font-semibold"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                Save Contact (vCard)
              </button>
            </div>

            {/* QR Code */}
            <div className="border-t border-gray-200 pt-8 mb-8">
              <h3 className="text-lg font-semibold text-gray-900 mb-4 text-center">
                Scan to Save
              </h3>
              <div className="flex justify-center">
                <div className="bg-white p-4 rounded-xl shadow-md">
                  <Image
                    src="/gkaassets/md-qr-code.png"
                    alt="QR Code to save contact"
                    width={150}
                    height={150}
                    className="rounded-lg"
                  />
                </div>
              </div>
              <p className="text-center text-sm text-gray-500 mt-3">
                Scan to view this business card
              </p>
            </div>

            {/* Quick Links */}
            <div className="border-t border-gray-200 pt-8">
              <h3 className="text-lg font-semibold text-gray-900 mb-4 text-center">
                Explore GK&A
              </h3>
              <div className="grid grid-cols-2 gap-3">
                <Link href="/" className="text-center py-3 px-4 bg-slate-100 text-slate-700 rounded-lg hover:bg-slate-200 transition-colors">
                  Website
                </Link>
                <Link href="/contact" className="text-center py-3 px-4 bg-slate-100 text-slate-700 rounded-lg hover:bg-slate-200 transition-colors">
                  Contact Us
                </Link>
              </div>
            </div>

            {/* Footer */}
            <div className="mt-8 text-center text-sm text-gray-500">
              <p>GK&A Logistics Services Ltd</p>
              <p>NPA Lighter Terminal, Ikorodu, Lagos</p>
              <p className="mt-2">
                <Link href="/" className="text-primary hover:underline">
                  www.gkaports.com
                </Link>
              </p>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
