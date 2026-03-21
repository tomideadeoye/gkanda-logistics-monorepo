"use client";
import Image from "next/image";
import Link from "next/link";
import { motion } from "motion/react";
import { Icon } from "@iconify/react";
import { Heroimage } from "@/app/api/data";

const Hero = () => {
  const leftAnimation = {
    initial: { x: "-100%", opacity: 0 },
    animate: { x: 0, opacity: 1 },
    exit: { x: "-100%", opacity: 0 },
    transition: { duration: 1 },
  };

  const rightAnimation = {
    initial: { x: "100%", opacity: 0 },
    animate: { x: 0, opacity: 1 },
    exit: { x: "100%", opacity: 0 },
    transition: { duration: 1 },
  };
  return (
    <section className="relative pt-44 mb-14 bg-cover bg-center bg-heroBg dark:bg-darkmode">
      <div className="w-full h-full absolute z-0 bg-white dark:bg-midnight_text rounded-b-[119px] -left-1/4 top-0"></div>
      <div className="container mx-auto lg:max-w-(--breakpoint-xl) relative z-1 md:max-w-(--breakpoint-md) px-4">
        <div className="grid grid-cols-12 items-center">
          <motion.div {...leftAnimation} className="lg:col-span-6 col-span-12">
            <h1 className="md:text-50 sm:text-40 text-28 text-midnight_text dark:text-white lg:text-start mb-9 lg:w-full w-3/4 leading-relaxed">
              Building Nigeria's Future in
              <div className="mt-6 md:mt-8 lg:mt-6"></div>
              <span className="md:text-50 text-36 rounded-lg lg:text-start text-primary max-w-max block mt-8 md:mt-10 lg:mt-6">
                Inland Ports & Logistics
              </span>
              <div className="mt-8 md:mt-10 lg:mt-6"></div>
              Through Innovation.
            </h1>
            <p className="sm:text-19 text-16 text-muted dark:text-white dark:text-opacity-70 text-start lg:max-w-full sm:max-w-75%">
              Driving innovation in maritime infrastructure and logistics through two transformative projects in Ikorodu, Lagos. World-class port terminal facility serving Nigeria's import and export activities.
            </p>
            <div className="flex items-center mt-12 gap-11">
              <div>
                <Link
                  href="/contact"
                  className="text-17 flex gap-2 items-center bg-primary text-white py-3 px-8 rounded-lg border border-primary hover:text-primary hover:bg-transparent"
                >
                  Request Meeting
                  <Icon
                    icon="solar:alt-arrow-right-linear"
                    width="13"
                    height="13"
                    className="text-white"
                  />
                </Link>
              </div>
              <div>
                <Link
                  href="/services"
                  className="text-17 flex gap-2 items-center text-muted dark:text-white dark:text-opacity-70 hover:text-primary"
                >
                  Explore Services
                  <Icon
                    icon="solar:alt-arrow-right-linear"
                    width="13"
                    height="13"
                    className="text-white"
                  />
                </Link>
              </div>
            </div>

            <div className="lg:my-28 my-12">
              <p className="text-20 text-muted dark:text-white dark:text-opacity-70 text-start mb-7">
                Strategic maritime partners
              </p>
              <div className="flex space-x-6 justify-start w-full">
                {Heroimage.map((item, index) => (
                  <Link key={index} href="/" className="flex-shrink-0">
                    <Image
                      src={item.lightimage}
                      alt="Strategic Partner"
                      width={140}
                      height={42}
                      className="block dark:hidden h-12 w-auto object-contain"
                    />
                    <Image
                      src={item.darkimage}
                      alt="Strategic Partner"
                      width={140}
                      height={42}
                      className="hidden dark:block h-12 w-auto object-contain"
                    />
                  </Link>
                ))}
              </div>
            </div>
          </motion.div>
          <motion.div
            {...rightAnimation}
            className="lg:col-span-6 col-span-12 pl-20 lg:block hidden"
          >
            <Image
              src="/images/bernd-dittrich-LKvT6sCkuPU-unsplash-scaled.jpg"
              alt="GK&A Logistics Maritime Operations"
              width={498}
              height={651}
              style={{ width: "100%", height: "100%" }}
            />
          </motion.div>
        </div>
      </div>
    </section>
  );
};

export default Hero;