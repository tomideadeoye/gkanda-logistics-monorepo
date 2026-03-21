import React from "react";
import Link from "next/link";

const Location = () => {
  const breadcrumbLinks = [
    { href: "/", text: "Home" },
    { href: "/contact", text: "Contact" },
  ];
  return (
    <>
      <section className="bg-primary py-24">
        <div className="container mx-auto lg:max-w-(--breakpoint-xl) md:max-w-(--breakpoint-md) px-4">
            <div className="">
                <div className="grid md:grid-cols-6 lg:grid-cols-9 grid-cols-1 gap-7 border-b border-solid border-white border-opacity-50 pb-11">
                    <div className="col-span-3">
                        <h2 className="text-white max-w-56 text-40 font-bold">Head Office</h2>
                    </div>
                    <div className="col-span-3">
                        <p className="sm:text-24 text-xl text-IceBlue font-normal max-w-64 leading-10 text-white text-opacity-50">131 Obafemi Awolowo Way, Alausa, Ikeja, Lagos, Nigeria</p>
                    </div>
                    <div className="col-span-3">
                        <Link href="mailto:info@gkaports.com.ng" className="sm:text-24 text-xl text-white font-medium underline">info@gkaports.com.ng</Link>
                        <Link href="tel:+2348181927251" className="sm:text-24 text-xl text-white text-opacity-80 flex items-center gap-2 hover:text-opacity-100 w-fit"><span className="text-white text-opacity-40!">Call</span>+234 818 192 7251</Link>
                    </div>
                </div>
                <div className="grid md:grid-cols-6 lg:grid-cols-9 grid-cols-1 gap-7 pt-12">
                    <div className="col-span-3">
                        <h2 className="text-white max-w-52 text-40 font-bold">Terminal Facility</h2>
                    </div>
                    <div className="col-span-3">
                        <p className="sm:text-24 text-xl text-white text-opacity-50 font-normal max-w-64 leading-10">NPA Lighter Terminal, Ikorodu, Lagos</p>
                    </div>
                    <div className="col-span-3">
                        <Link href="mailto:info@gkaports.com.ng" className="sm:text-24 text-xl text-white font-medium underline">info@gkaports.com.ng</Link>
                        <Link href="tel:+2348181927251" className="sm:text-24 text-white text-opacity-80 text-xl text-IceBlue flex items-center gap-2 hover:text-opacity-100 w-fit"><span className="text-white text-opacity-40!">Call</span>+234 818 192 7251</Link>
                    </div>
                </div>
                
                {/* Map Section */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mt-16">
                  <div className="bg-white rounded-lg p-4 h-64">
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
                  
                  <div className="bg-white rounded-lg p-4 h-64">
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
      </section>
    </>
  );
};

export default Location;