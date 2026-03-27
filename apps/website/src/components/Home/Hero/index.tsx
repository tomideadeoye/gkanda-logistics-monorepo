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
      <div className="container mx-auto lg:max-w-[73.125rem] relative z-1 md:max-w-[48rem] px-4">
        <div className="grid grid-cols-12 items-center gap-8">
          <motion.div {...leftAnimation} className="lg:col-span-7 col-span-12">
            <h1 className="md:text-5xl sm:text-4xl text-3xl text-midnight_text dark:text-white lg:text-start font-bold mb-6 leading-tight">
              Building Nigeria's Future in{" "}
              <span className="text-primary">Inland Ports & Logistics</span>
              <br />
              <span className="text-midnight_text dark:text-white">Through Innovation.</span>
            </h1>
            <p className="text-lg text-muted dark:text-white dark:text-opacity-70 text-start mb-8 max-w-xl">
              Driving innovation in maritime infrastructure and logistics through two transformative projects in Ikorodu, Lagos. World-class port terminal facility serving Nigeria's import and export activities.
            </p>
            <div className="flex flex-wrap items-center gap-4">
              <Link
                href="/contact"
                className="inline-flex items-center gap-2 bg-primary text-white px-6 py-3 rounded-lg font-medium hover:bg-orange-600 transition-colors"
              >
                Request Meeting
                <Icon icon="solar:arrow-right-linear" width="18" height="18" />
              </Link>
              <Link
                href="/services"
                className="inline-flex items-center gap-2 text-midnight_text dark:text-white font-medium hover:text-primary transition-colors"
              >
                Explore Services
                <Icon icon="solar:arrow-right-linear" width="18" height="18" />
              </Link>
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
            className="lg:col-span-5 col-span-12"
          >
            <div className="relative">
              <Image
                src="/images/bernd-dittrich-LKvT6sCkuPU-unsplash-scaled.jpg"
                alt="GK&A Logistics Maritime Operations"
                width={600}
                height={700}
                className="w-full h-auto rounded-2xl shadow-2xl"
                priority
              />
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
};

export default Hero;