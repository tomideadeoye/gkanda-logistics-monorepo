"use client";

import React, { useState, useRef } from "react";
import Image from "next/image";

export default function SignatureGenerator() {
  const [name, setName] = useState("John Doe");
  const [title, setTitle] = useState("Operations Manager");
  const [phone, setPhone] = useState("+234 xxx xxx xxxx");
  const [showPhone, setShowPhone] = useState(true);
  const [whatsapp, setWhatsapp] = useState("+234 xxx xxx xxxx");
  const [showWhatsapp, setShowWhatsapp] = useState(true);
  const [mobile, setMobile] = useState("");
  const [showMobile, setShowMobile] = useState(false);
  const [email, setEmail] = useState("john.doe@gkaports.com");
  const [copied, setCopied] = useState(false);
  const signatureRef = useRef<HTMLDivElement>(null);

  const handleCopy = () => {
    if (signatureRef.current) {
      const range = document.createRange();
      range.selectNode(signatureRef.current);
      window.getSelection()?.removeAllRanges();
      window.getSelection()?.addRange(range);
      document.execCommand("copy");
      window.getSelection()?.removeAllRanges();
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  return (
    <main className="min-h-screen bg-gray-50 pt-24 pb-16">
      <div className="container mx-auto lg:max-w-4xl px-4">
        <div className="text-center mb-12">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Email Signature Generator</h1>
          <p className="text-gray-500">Create your GK&A email signature for Zoho Mail</p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Form */}
          <div className="bg-white rounded-2xl shadow-lg p-6">
            <h2 className="text-xl font-semibold text-gray-900 mb-6">Your Details</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Job Title</label>
                <input
                  type="text"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Telephone</label>
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                    className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
                  />
                  <label className="flex items-center gap-2 text-sm">
                    <input
                      type="checkbox"
                      checked={showPhone}
                      onChange={(e) => setShowPhone(e.target.checked)}
                      className="w-4 h-4"
                    />
                    Show
                  </label>
                </div>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">WhatsApp</label>
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={whatsapp}
                    onChange={(e) => setWhatsapp(e.target.value)}
                    className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
                  />
                  <label className="flex items-center gap-2 text-sm">
                    <input
                      type="checkbox"
                      checked={showWhatsapp}
                      onChange={(e) => setShowWhatsapp(e.target.checked)}
                      className="w-4 h-4"
                    />
                    Show
                  </label>
                </div>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Mobile (optional)</label>
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={mobile}
                    onChange={(e) => setMobile(e.target.value)}
                    placeholder="+234 xxx xxx xxxx"
                    className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
                  />
                  <label className="flex items-center gap-2 text-sm">
                    <input
                      type="checkbox"
                      checked={showMobile}
                      onChange={(e) => setShowMobile(e.target.checked)}
                      className="w-4 h-4"
                    />
                    Show
                  </label>
                </div>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
                <input
                  type="text"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
                />
              </div>
            </div>
          </div>

          {/* Preview & Copy */}
          <div className="space-y-6">
            <div className="bg-white rounded-2xl shadow-lg p-6">
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-xl font-semibold text-gray-900">Preview</h2>
                <button
                  onClick={handleCopy}
                  className={`px-4 py-2 rounded-lg font-semibold transition-all ${
                    copied
                      ? "bg-green-500 text-white"
                      : "bg-primary text-white hover:bg-blue-700"
                  }`}
                >
                  {copied ? "Copied!" : "Copy Signature"}
                </button>
              </div>

              <div className="border border-gray-200 rounded-lg p-6 overflow-x-auto min-w-[600px]">
                <div ref={signatureRef} id="signature">
                  <div style={{ fontFamily: "'Inter', sans-serif", color: "#1a1a1a", lineHeight: "1.5" }}>
                    <table cellPadding={0} cellSpacing={0} border={0} style={{ width: "100%", maxWidth: "650px" }}>
                      <tbody>
                        <tr>
                          <td style={{ verticalAlign: "top", paddingRight: "20px", borderRight: "2px solid #003366" }}>
                            <img
                              src="/gk & a logo.png"
                              alt="GK&A Logistics Logo"
                              width={140}
                              style={{ display: "block", width: "140px", height: "auto" }}
                            />
                          </td>
                          <td style={{ verticalAlign: "top", paddingLeft: "20px", whiteSpace: "nowrap" }}>
                            <p style={{ margin: "0", fontSize: "18px", fontWeight: 700, color: "#003366", whiteSpace: "nowrap" }}>
                              {name}
                            </p>
                            <p style={{ margin: "2px 0 10px 0", fontSize: "13px", color: "#666", fontStyle: "italic", whiteSpace: "nowrap" }}>
                              {title}
                            </p>

                            <p style={{ margin: "10px 0 0 0", fontSize: "12px", fontWeight: 600, color: "#003366", textTransform: "uppercase", whiteSpace: "nowrap" }}>
                              GK&A Logistics Services Limited
                            </p>
                            <p style={{ margin: "0", fontSize: "11px", color: "#444", whiteSpace: "nowrap" }}>
                              GK&A Terminal Harbour Limited
                            </p>
                            <p style={{ margin: "0 0 10px 0", fontSize: "11px", color: "#444", whiteSpace: "nowrap" }}>
                              GK&A Port Infrastructure PTE. LTD.
                            </p>

                            <div style={{ fontSize: "12px", color: "#333" }}>
                              {showPhone && phone && (
                                <p style={{ margin: "2px 0" }}>
                                  <strong>T:</strong> {phone}
                                </p>
                              )}
                              {showWhatsapp && whatsapp && (
                                <p style={{ margin: "2px 0" }}>
                                  <strong>W:</strong> {whatsapp} (WhatsApp)
                                </p>
                              )}
                              {showMobile && mobile && (
                                <p style={{ margin: "2px 0" }}>
                                  <strong>M:</strong> {mobile}
                                </p>
                              )}
                              <p style={{ margin: "2px 0" }}>
                                <strong>E:</strong>{" "}
                                <a href={`mailto:${email}`} style={{ color: "#003366", textDecoration: "none" }}>
                                  {email}
                                </a>
                              </p>
                              <p style={{ margin: "2px 0" }}>
                                <strong>W:</strong>{" "}
                                <a href="https://www.gkaports.com" style={{ color: "#003366", textDecoration: "none" }}>
                                  www.gkaports.com
                                </a>
                              </p>
                              <p style={{ margin: "10px 0 0 0", fontSize: "11px", color: "#888" }}>
                                Lagos, Nigeria
                              </p>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>

            {/* Instructions */}
            <div className="bg-blue-50 border border-blue-200 rounded-2xl p-6">
              <h3 className="font-semibold text-blue-900 mb-2">How to use:</h3>
              <ol className="text-sm text-blue-800 space-y-1 list-decimal list-inside">
                <li>Fill in your details on the left</li>
                <li>Click &quot;Copy Signature&quot;</li>
                <li>Open Zoho Mail Settings</li>
                <li>Go to Signatures and paste</li>
                <li>Save and you&apos;re done!</li>
              </ol>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
