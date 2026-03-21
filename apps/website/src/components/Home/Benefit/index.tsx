"use client";
import Link from "next/link";
import Image from "next/image";
import { motion, useInView } from "motion/react";
import { useRef } from "react";
import { Icon } from "@iconify/react";
import { BuildingStorefrontIcon, ShieldCheckIcon, GlobeAltIcon, ClockIcon, UserGroupIcon } from "@heroicons/react/24/solid";
import { BeneifitImage } from "@/app/api/data";

const Benefit = () => {
  const ref = useRef(null);
  const inView = useInView(ref);

  const TopAnimation = {
    initial: { y: "-100%", opacity: 0 },
    animate: inView ? { y: 0, opacity: 1 } : { y: "-100%", opacity: 0 },
    transition: { duration: 1, delay: 0.4 },
  };

  const leftAnimation = {
    initial: { x: "-100%", opacity: 0 },
    animate: inView ? { x: 0, opacity: 1 } : { x: "-100%", opacity: 0 },
    transition: { duration: 1, delay: 0.4 },
  };

  const rightAnimation = {
    initial: { x: "100%", opacity: 0 },
    animate: inView ? { x: 0, opacity: 1 } : { x: "100%", opacity: 0 },
    transition: { duration: 1, delay: 0.4 },
  };

  return (
    <section className="bg-white dark:bg-darkmode py-14 overflow-x-hidden">
      <div className="container lg:max-w-(--breakpoint-xl) md:max-w-(--breakpoint-md) px-4 mx-auto">
        <div
          ref={ref}
          className="bg-white dark:bg-midnight_text bg-heroBg rounded-3xl md:py-20 py-10 2xl:pr-14 2xl:pl-20 sm:px-14 px-6"
        >
          <motion.div {...TopAnimation} className="items-start">
            <h2 className="font-bold md:text-35 sm:text-28 text-24 text-midnight_text dark:text-white leading-loose">
              Why choose
              <span className="bg-border dark:bg-darkHeroBg rounded-lg text-primary max-w-max ml-2">
                GK&A Logistics
              </span>
              <br />
              for your maritime needs.
            </h2>
          </motion.div>
          <div className="grid grid-cols-12 items-center mt-16 md:gap-12 sm:gap-8">
            <motion.div
              {...leftAnimation}
              className="xl:col-span-6 col-span-12 sm:block hidden"
            >
              <div className="xl:px-0 lg:px-20">
                <Image
                  src="/gkaassets/bernd-dittrich-Xk1IfNnEhRA-unsplash-scaled.jpg"
                  alt="GKA Logistics Benefit Image"
                  width={435}
                  height={304}
                  style={{ width: "100%", height: "100%" }}
                />
              </div>
            </motion.div>
            <motion.div
              {...rightAnimation}
              className="xl:col-span-6 col-span-12"
            >
              <p className="sm:text-25 text-18 text-midnight_text font-medium dark:text-white">
                Experience world-class maritime logistics with comprehensive
                port operations and secure cargo handling.
              </p>
              {BeneifitImage.map((item, index) => (
                <div key={index} className="sm:flex items-center mt-8">
                  <div className="w-8 h-8 sm:mr-4 sm:mb-0 mb-3 flex items-center justify-center">
                    {(() => {
                      switch(item.image) {
                        case "building-storefront":
                          return <BuildingStorefrontIcon className="w-6 h-6 text-primary" />;
                        case "shield-check":
                          return <ShieldCheckIcon className="w-6 h-6 text-primary" />;
                        case "globe-alt":
                          return <GlobeAltIcon className="w-6 h-6 text-primary" />;
                        case "clock":
                          return <ClockIcon className="w-6 h-6 text-primary" />;
                        case "user-group":
                          return <UserGroupIcon className="w-6 h-6 text-primary" />;
                        default:
                          return null;
                      }
                    })()}
                  </div>
                  <p className="text-17 text-midnight_text dark:text-white dark:text-opacity-50">
                    {item.details}
                  </p>
                </div>
              ))}
              <div className="flex items-center lg:justify-start justify-center">
                <Link
                  href="#"
                  className="text-17 flex gap-3 items-center bg-primary text-white py-3 px-8 rounded-lg  mt-12 border border-primary hover:text-primary hover:bg-transparent"
                >
                  Get Started
                  <Icon
                    icon="solar:alt-arrow-right-linear"
                    width="13"
                    height="13"
                  />
                </Link>
              </div>
            </motion.div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Benefit;