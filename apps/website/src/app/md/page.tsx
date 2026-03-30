"use client";

import React, { useEffect } from "react";

export default function MQrCodeDetails() {
  useEffect(() => {
    // Hide main header/footer
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
    <div className="min-h-screen bg-white p-8 md:p-16 font-sans text-black">
      <div className="max-w-2xl">
        <h1 className="text-[40px] font-bold mb-10 tracking-tight">QR Code details</h1>
        
        <div className="space-y-8">
          {/* Identity Section */}
          <div className="space-y-1">
            <p className="text-[28px] font-bold">Omobola Litan Abiru</p>
            <p className="text-[28px] font-bold italic">Managing Director</p>
          </div>

          {/* Company Section */}
          <div className="space-y-1 text-xl font-bold">
            <p>GK&A LOGISTICS SERVICES LIMITED</p>
            <p>GK&A Terminal Harbour Limited</p>
            <p>GK&A Port Infrastructure PTE. LTD.</p>
          </div>

          {/* Contact Section */}
          <div className="space-y-3 text-xl">
            <div className="flex gap-2">
              <span className="font-bold min-w-[30px]">T:</span>
              <a href="tel:+2348108627165" className="text-[#BA9132] underline hover:text-[#9A7A2A] transition-colors">+234 810 862 7165</a>
            </div>
            <div className="flex gap-2">
              <span className="font-bold min-w-[30px]">W:</span>
              <a href="https://wa.me/2347038341611" className="text-[#BA9132] underline hover:text-[#9A7A2A] transition-colors">+234 703 834 1611 (WhatsApp)</a>
            </div>
            <div className="flex gap-2">
              <span className="font-bold min-w-[30px]">M:</span>
              <a href="tel:+2348184082911" className="text-[#BA9132] underline hover:text-[#9A7A2A] transition-colors">+234 818 408 2911</a>
            </div>
            <div className="flex gap-2">
              <span className="font-bold min-w-[30px]">E:</span>
              <a href="mailto:mobolaabiru@gkaports.com" className="text-[#BA9132] underline hover:text-[#9A7A2A] transition-colors">mobolaabiru@gkaports.com</a>
            </div>
            <div className="flex gap-2">
              <span className="font-bold min-w-[30px]">W:</span>
              <a href="https://www.gkaports.com" target="_blank" rel="noopener noreferrer" className="text-[#BA9132] underline hover:text-[#9A7A2A] transition-colors">www.gkaports.com</a>
            </div>
            <p className="pt-2 font-medium">Lagos, Nigeria</p>
          </div>
        </div>
      </div>
    </div>
  );
}
