"use client";

import React, { useEffect } from "react";

interface ContactPageProps {
  name: string;
  title: string;
  companies?: string[];
  phone?: string;
  whatsapp?: string;
  mobile?: string;
  email?: string;
  website?: string;
  location?: string;
}

export default function ContactPage({
  name,
  title,
  companies = [
    "GK&A TERMINAL - NPA IKORODU LIGHTER TERMINAL (ILT) LAGOS, NIGERIA",
    "GK&A Logistics Services Limited",
    "GK&A Terminal Harbour Limited",
    "GK&A Port Infrastructure PTE. LTD.",
  ],
  phone,
  whatsapp,
  mobile,
  email,
  website = "www.gkaports.com",
  location = "Lagos, Nigeria",
}: ContactPageProps) {
  useEffect(() => {
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
          <div className="space-y-1">
            <p className="text-[28px] font-bold">{name}</p>
            <p className="text-[28px] font-bold italic">{title}</p>
          </div>

          <div className="space-y-1 text-xl font-bold">
            {companies.map((c) => (
              <p key={c}>{c}</p>
            ))}
          </div>

          <div className="space-y-3 text-xl">
            {phone && (
              <div className="flex gap-2">
                <span className="font-bold min-w-[30px]">T:</span>
                <a href={`tel:${phone.replace(/\s/g, "")}`} className="text-[#BA9132] underline hover:text-[#9A7A2A] transition-colors">{phone}</a>
              </div>
            )}
            {whatsapp && (
              <div className="flex gap-2">
                <span className="font-bold min-w-[30px]">W:</span>
                <a href={`https://wa.me/${whatsapp.replace(/[^0-9]/g, "")}`} className="text-[#BA9132] underline hover:text-[#9A7A2A] transition-colors">{whatsapp} (WhatsApp)</a>
              </div>
            )}
            {mobile && (
              <div className="flex gap-2">
                <span className="font-bold min-w-[30px]">M:</span>
                <a href={`tel:${mobile.replace(/\s/g, "")}`} className="text-[#BA9132] underline hover:text-[#9A7A2A] transition-colors">{mobile}</a>
              </div>
            )}
            {email && (
              <div className="flex gap-2">
                <span className="font-bold min-w-[30px]">E:</span>
                <a href={`mailto:${email}`} className="text-[#BA9132] underline hover:text-[#9A7A2A] transition-colors">{email}</a>
              </div>
            )}
            {website && (
              <div className="flex gap-2">
                <span className="font-bold min-w-[30px]">W:</span>
                <a href={`https://${website}`} target="_blank" rel="noopener noreferrer" className="text-[#BA9132] underline hover:text-[#9A7A2A] transition-colors">{website}</a>
              </div>
            )}
            {location && <p className="pt-2 font-medium">{location}</p>}
          </div>
        </div>
      </div>
    </div>
  );
}
