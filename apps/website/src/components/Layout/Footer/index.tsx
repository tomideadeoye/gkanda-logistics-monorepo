import Image from "next/image";
import Link from "next/link";
import { Icon } from "@iconify/react";
import { footerLinks } from "@/app/api/data";

const Footer = () => {
  return (
    <footer className="pt-8 mt-14 bg-primary relative after:content-[''] after:absolute after:bg-[url('/images/footer/bgline.png')] after:bg-no-repeat after:w-52 after:h-24 after:right-0 after:top-28 xl:after:block after:hidden before:content-[''] before:absolute before:inset-0 before:bg-[url('/gkaassets/bernd-dittrich-Xk1IfNnEhRA-unsplash-scaled.jpg')] before:bg-cover before:bg-center before:opacity-30">
      <div className="container mx-auto lg:max-w-(--breakpoint-xl) md:max-w-(--breakpoint-md) px-2">
        <div className="flex lg:items-center justify-between lg:flex-row flex-col border-b border-dark_border pb-14 mb-16 ">
          <div className="flex sm:flex-nowrap flex-wrap gap-6">
            <div className="flex items-center text-white text-16">
              <Icon icon="weui:location-outlined" className="w-7 h-7 mr-3 text-white" />
              <div className="flex flex-col">
                <span>NPA Lighter Terminal, Ikorodu</span>
                <span>Lagos State, Nigeria</span>
              </div>
            </div>
            <div className="flex items-center gap-2 text-white">
              <Icon icon="majesticons:phone-retro-line" className="w-7 h-7 text-white" />
              <Link href="tel:+2348181927251" className="text-16 hover:text-white">
                <span> +234 818 192 7251</span>
              </Link>
            </div>
            <div className="flex items-center text-white gap-2">
              <Icon icon="clarity:email-line" className="w-7 h-7 text-white" />
              <Link
                href="mailto:info@gkaports.com.ng"
                className="inline-flex items-center text-16 hover:text-white"
              >
                <span>info@gkaports.com.ng</span>
              </Link>
            </div>
          </div>
          <div className="flex gap-4 mt-4 lg:mt-0">
            <Link href="https://web.facebook.com/people/GK-A-Logistics-Services/61581721094109/" className="text-muted hover:text-primary">
              <Icon icon="fe:facebook" width="32" height="32" className="text-white" />
            </Link>
            <Link href="#" className="text-muted hover:text-primary">
              <Icon icon="fa6-brands:square-twitter" width="32" height="32" className="text-white" />
            </Link>
            <Link href="https://www.linkedin.com/company/gk-a-logistics-services-ltd/" className="text-muted hover:text-primary">
              <Icon icon="fa6-brands:linkedin" width="32" height="32" className="text-white" />
            </Link>
          </div>
        </div>
        <div className="grid grid-cols-12 sm:mb-16 mb-8 pt-8 gap-4 relative before:content-[''] before:absolute before:w-20 before:h-20 before:bg-[url('/images/footer/bgcir.png')] before:bg-no-repeat before:-left-36 before:bottom-9 lg:before:block before:hidden">
          <div className="md:col-span-2 col-span-6 mb-4 md:mb-0">
            <h4 className="text-18 text-white mb-3">
              Services
            </h4>
            <ul>
              {footerLinks.slice(0, 4).map((item, index) => (
                <li key={index} className="pb-3">
                  <Link
                    href="#"
                    className="text-white text-16 hover:text-white"
                  >
                    {item.link}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div className="md:col-span-2 col-span-6 mb-4 md:mb-0">
            <h4 className="text-18 text-white mb-3">
              Operations
            </h4>
            <ul>
              {footerLinks.slice(4, 9).map((item, index) => (
                <li key={index} className="pb-3">
                  <Link
                    href="#"
                    className="text-white text-16 hover:text-white"
                  >
                    {item.link}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div className="md:col-span-3 col-span-6 mb-4 md:mb-0">
            <h4 className="text-18 text-white mb-3">
              Company
            </h4>
            <ul>
              {footerLinks.slice(9, 14).map((item, index) => (
                <li key={index} className="pb-3">
                  <Link
                    href="#"
                    className="text-white text-16 hover:text-white"
                  >
                    {item.link}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div className="md:col-span-5 col-span-12">
            <p className="text-18 text-white font-bold">Subscribe for Updates</p>
            <form className="mt-8">
              <div className="relative">
                <input
                  type="email"
                  name="email"
                  id="email"
                  placeholder="Enter your email address"
                  className="bg-white placeholder:text-gray-500 text-black py-3 pl-5"
                />
                <Icon
                  icon="solar:plain-2-linear"
                  className="text-22 text-gray-500 absolute right-5 top-4"
                />
              </div>
            </form>
            <div className="mt-8">
              <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3963.952912260551!2d3.5044!3d6.6018!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x103b8c6c6c6c6c6c%3A0x1234567890abcdef!2sNPA%20Lighter%20Terminal%2C%20Ikorodu!5e0!3m2!1sen!2sng!4v1234567890!5m2!1sen!2sng"
                width="100%"
                height="200"
                style={{ border: 0 }}
                allowFullScreen
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
                className="rounded-lg"
              ></iframe>
            </div>
          </div>
        </div>
        <div className="flex items-center sm:flex-row flex-col justify-between py-10 mt-8">
          <p className="text-16 text-white sm:mb-0 mb-4">
            © Copyright 2025. All rights reserved by GK&A Logistics Services Ltd.
          </p>
          <div className="flex gap-4">
            {footerLinks.slice(14, 17).map((item, index) => (
              <div key={index} className="">
                <Link href="#" className="text-white hover:text-white">
                  {item.link}
                </Link>
              </div>
            ))}
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;