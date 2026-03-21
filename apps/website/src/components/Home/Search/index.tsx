"use client";
import React from "react";
import { Icon } from "@iconify/react";
import { motion, useInView } from "motion/react";
import { useRef } from "react";
import Image from "next/image";
import Link from "next/link";
import { review } from "@/app/api/data";

const Search = () => {
  const ref = useRef(null);
  const inView = useInView(ref);

  const TopAnimation = {
    initial: { y: "-100%", opacity: 0 },
    animate: inView ? { y: 0, opacity: 1 } : { y: "-100%", opacity: 0 },
    transition: { duration: 1, delay: 0.4 },
  };

  const bottomAnimation = {
    initial: { y: "100%", opacity: 0 },
    animate: inView ? { y: 0, opacity: 1 } : { y: "100%", opacity: 0 },
    transition: { duration: 1, delay: 0.4 },
  };

  const renderStars = (rating: number) => {
    const fullStars = Math.floor(rating);
    const halfStars = rating % 1 >= 0.5 ? 1 : 0;
    const emptyStars = 5 - fullStars - halfStars;

    const stars = [];

    for (let i = 0; i < fullStars; i++) {
      stars.push(
        <Icon
          key={`full-${i}`}
          icon="ph:star-fill"
          className="w-5 h-5 text-yellow-500"
        />
      );
    }

    if (halfStars) {
      stars.push(
        <Icon
          key="half"
          icon="ph:star-half-fill"
          className="w-5 h-5 text-yellow-500"
        />
      );
    }

    for (let i = 0; i < emptyStars; i++) {
      stars.push(
        <Icon
          key={`empty-${i}`}
          icon="ph:star-bold"
          className="w-5 h-5 text-yellow-500"
        />
      );
    }

    return stars;
  };

  return (
    <section className="bg-white dark:bg-darkmode overflow-hidden py-14">
      <div className="container mx-auto lg:max-w-(--breakpoint-xl) md:max-w-(--breakpoint-md) px-4">
        <div
          ref={ref}
          className="bg-white dark:bg-midnight_text bg-heroBg rounded-3xl p-2"
        >
          <motion.div
            {...TopAnimation}
            className="text-center lg:px-20 px-4 pt-20"
          >
            <div className="flex justify-center">
              <Image
                src="/images/search/free.png"
                alt="image"
                width={67}
                height={38}
              />
            </div>
            <h2 className="text-midnight_text font-bold dark:text-white md:text-35 sm:text-28 text-24">
              Streamline your
              <span className="lg:text-35 text-primary text-24">
                maritime logistics
              </span>
            </h2>
            <div className="md:max-w-75% mx-auto mt-6">
              <div className="flex lg:items-center md:items-start bg-white dark:bg-darkHeroBg shadow-md rounded-2xl overflow-hidden">
                <input
                  type="email"
                  placeholder="Enter your email address."
                  className="grow px-4 py-5 pl-6 text-white dark:text-heroBg text-17 focus:outline-hidden bg-white dark:bg-darkHeroBg hidden md:block"
                />
                <div className="flex lg:items-center lg:justify-start justify-center mr-4">
                  <Link
                    href="#"
                    className="text-17 flex items-center bg-primary text-white py-3 px-8 rounded-lg w-36  my-2 border border-primary hover:text-primary hover:bg-transparent"
                  >
                    Request Quote
                  </Link>
                </div>
              </div>
              <div className="flex items-center justify-center my-7">
                <div className="w-5 h-5 bg-blue-500 rounded-full flex items-center justify-center">
                  <Icon
                    icon="solar:unread-outline"
                    width="24"
                    height="24"
                    className="text-white"
                  />
                </div>
                <p className="ml-4 text-17 text-muted dark:text-white dark:text-opacity-50">
                  World-class maritime logistics with comprehensive security and 24/7 terminal operations
                </p>
              </div>
            </div>
          </motion.div>
          <motion.div {...bottomAnimation}>
            <div className="grid grid-cols-1 gap-6 px-4">
              {review.map((item, index) => (
                <div
                  key={index}
                  className="bg-white rounded-3xl lg:py-16 sm:py-10 py-5 lg:px-24 sm:px-12 px-6 dark:bg-darkmode"
                >
                  <div className="text-center">
                    <div className="mb-6">
                      <Image
                        src="/images/search/double.png"
                        alt="quotation mark"
                        width={52}
                        height={39}
                      />
                    </div>
                    <p className="text-midnight_text dark:text-white text-base mb-6 whitespace-pre-line">
                      {item.text}
                    </p>
                    <div className="text-center">
                      <h3 className="font-medium text-base text-midnight_text dark:text-white mb-2">
                        — {item.name}
                      </h3>
                      <h5 className="text-muted dark:text-muted text-base whitespace-pre-line">
                        {item.post}
                      </h5>
                    </div>
                  </div>
                </div>
                ))}
              </div>
            </motion.div>
        </div>
      </div>
    </section>
  );
};

export default Search;