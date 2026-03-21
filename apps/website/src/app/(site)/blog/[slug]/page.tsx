import { getAllPosts, getPostBySlug } from "@/utils/markdown";
import markdownToHtml from "@/utils/markdownToHtml";
import { format } from "date-fns";
import Image from "next/image";
import Link from "next/link";

type Props = {
  params: { slug: string };
};

export async function generateMetadata({ params }: any) {
  const data = await params;
  const posts = getAllPosts(["title", "date", "excerpt", "coverImage", "slug"]);
  const post = getPostBySlug(data.slug, [
    "title",
    "author",
    "content",
    "metadata",
    "coverImage"
  ]);

  const siteName = process.env.SITE_NAME || "GK&A Logistics";
  const authorName = process.env.AUTHOR_NAME || "GK&A Logistics Team";

  if (post) {
    const metadata = {
      title: `${post.title || "Single Post Page"} | ${siteName}`,
      description: post.excerpt || `Read more about ${post.title} on GK&A Logistics blog`,
      author: authorName,
      openGraph: {
        title: `${post.title || "Single Post Page"} | ${siteName}`,
        description: post.excerpt || `Read more about ${post.title} on GK&A Logistics blog`,
        url: `https://www.gkaports.com.ng/blog/${data.slug}`,
        siteName: siteName,
        images: [
          {
            url: post.coverImage || "/gkaassets/bernd-dittrich-LKvT6sCkuPU-unsplash-scaled.jpg",
            width: 1200,
            height: 630,
            alt: post.title || "Blog Post",
          },
        ],
        locale: "en_US",
        type: "article",
      },
      twitter: {
        card: "summary_large_image",
        title: `${post.title || "Single Post Page"} | ${siteName}`,
        description: post.excerpt || `Read more about ${post.title} on GK&A Logistics blog`,
        images: [post.coverImage || "/gkaassets/bernd-dittrich-LKvT6sCkuPU-unsplash-scaled.jpg"],
      },
      robots: {
        index: true,
        follow: true,
        nocache: true,
        googleBot: {
          index: true,
          follow: false,
          "max-video-preview": -1,
          "max-image-preview": "large",
          "max-snippet": -1,
        },
      },
    };

    return metadata;
  } else {
    return {
      title: "Not Found - GK&A Logistics",
      description: "No blog article has been found",
      author: authorName,
      openGraph: {
        title: "Not Found - GK&A Logistics",
        description: "No blog article has been found",
        url: "https://www.gkaports.com.ng/404",
        siteName: "GK&A Logistics",
        images: [
          {
            url: "/gkaassets/gk & a logo.png",
            width: 1200,
            height: 630,
            alt: "GK&A Logistics 404",
          },
        ],
        locale: "en_US",
        type: "website",
      },
      twitter: {
        card: "summary_large_image",
        title: "Not Found - GK&A Logistics",
        description: "No blog article has been found",
        images: ["/gkaassets/gk & a logo.png"],
      },
      robots: {
        index: false,
        follow: false,
        nocache: false,
        googleBot: {
          index: false,
          follow: false,
          "max-video-preview": -1,
          "max-image-preview": "large",
          "max-snippet": -1,
        },
      },
    };
  }
}

export default async function Post({ params }: any) {
  const data = await params;
  const posts = getAllPosts(["title", "date", "excerpt", "coverImage", "slug"]);
  const post = getPostBySlug(data.slug, [
    "title",
    "author",
    "authorImage",
    "content",
    "coverImage",
    "date",
  ]);

  const content = await markdownToHtml(post.content || "");

  return (
    <>
      <section className="relative pt-44 z-1 pb-20 bg-white">
        <div className="w-full h-full absolute -z-1 bg-heroBg rounded-b-[119px] -left-1/4 top-0"></div>
        <div className="container mx-auto">
          <div className="flex flex-wrap justify-center">
            <div className="w-full md:w-8/12 lg:w-6/12">
              <div className="text-center">
                <div className="flex flex-wrap justify-center gap-4 mb-8">
                  <div>
                    <span className="text-base text-midnight_text font-medium pr-7 border-r border-solid border-grey w-fit">
                      {format(new Date(post.date), "dd MMMM yyyy")}
                    </span>
                  </div>
                  <div>
                    <span className="text-base text-midnight_text font-medium sm:pl-7 pl-0 w-fit">
                      {post.author.name}
                    </span>
                  </div>
                </div>
                <h2 className="text-midnight_text text-[40px] leading-tight font-bold pt-7">
                  {post.title}
                </h2>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section className="pb-10 pt-20 lg:pb-20 bg-white">
        <div className="container mx-auto">
          <div className="-mx-4 flex flex-wrap justify-center">
            <div className="w-full px-4">
              <div className="z-20 mb-16 h-150 overflow-hidden rounded-sm md:h-45">
                <Image
                  src={post.coverImage}
                  alt="image"
                  width={1170}
                  height={766}
                  quality={100}
                  className="h-full w-full object-cover object-center rounded-3xl"
                />
              </div>
              <div className="-mx-4 flex flex-wrap">
                <div className="w-full px-4 lg:w-8/12">
                  <div className="blog-details markdown xl:pr-10">
                    <div dangerouslySetInnerHTML={{ __html: content }}></div>
                  </div>
                </div>
                <div className="w-full px-4 lg:w-4/12">
                  <div>
                    <div className="-mx-4 mb-8 flex flex-col">
                      <div className="w-full py-12 px-11 bg-white shadow-lg border-b-2 border-border rounded-t-lg">
                        <h2
                          className="wow fadeInUp relative mb-5 text-2xl text-black  sm:text-3xl"
                          data-wow-delay=".1s"
                        >
                          Share
                        </h2>
                        <div className="flex gap-4 flex-col">
                          <Link
                            href="#"
                            className="bg-[#526fa3] py-4 px-6 text-20 rounded-lg flex items-center text-white"
                          >
                            <svg
                              className="svg-inline--fa fa-facebook-f me-3"
                              aria-hidden="true"
                              focusable="false"
                              data-prefix="fab"
                              data-icon="facebook-f"
                              role="img"
                              xmlns="http://www.w3.org/2000/svg"
                              viewBox="0 0 320 512"
                              width="12.5px"
                              height="20px"
                            >
                              <path
                                fill="white"
                                d="M80 299.3V512H196V299.3h86.5l18-97.8H196V166.9c0-51.7 20.3-71.5 72.7-71.5 16.3 0 29.4 .4 37 1.2V7.9C291.4 4 256.4 0 236.2 0 129.3 0 80 50.5 80 159.4v42.1H14v97.8H80z"
                              />
                            </svg>
                            Facebook
                          </Link>
                          <Link
                            href="#"
                            className="bg-[#46C4FF] py-4 px-6 text-20 rounded-lg flex items-center text-white"
                          >
                            <svg
                              className="svg-inline--fa fa-twitter me-3"
                              aria-hidden="true"
                              focusable="false"
                              data-prefix="fab"
                              data-icon="twitter"
                              role="img"
                              xmlns="http://www.w3.org/2000/svg"
                              viewBox="0 0 512 512"
                              height="21.5px"
                              width="25px"
                            >
                              <path
                                fill="currentColor"
                                d="M459.4 151.7c.325 4.548.325 9.097.325 13.745 0 140.966-107.416 303.213-303.213 303.213-60.452 0-116.426-17.781-163.725-48.265 8.447.974 16.568 1.299 25.34 1.299 50.236 0 96.56-17.206 133.26-46.258-46.832-.975-86.185-31.188-99.675-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.828-9.797-85.417-52.628-85.417-103.766v-1.299c14.33 7.92 30.748 12.67 48.364 13.32-28.264-18.843-46.832-51.014-46.832-87.391 0-19.492 5.197-37.36 14.33-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.794-2.599-15.91-2.599-24.029 0-57.502 46.833-104.335 104.334-104.335 30.137 0 57.502 12.67 76.67 33.137 23.715-4.548 46.182-13.32 66.599-25.34-7.793 24.366-24.366 44.833-46.182 57.502 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z"
                              />
                            </svg>
                            twitter
                          </Link>
                          <Link
                            href="#"
                            className="bg-[#3C86AD] py-4 px-6 flex items-center text-20 rounded-lg text-white"
                          >
                            <svg
                              className="svg-inline--fa fa-linkedin-in me-3"
                              aria-hidden="true"
                              focusable="false"
                              data-prefix="fab"
                              data-icon="linkedin-in"
                              role="img"
                              xmlns="http://www.w3.org/2000/svg"
                              viewBox="0 0 448 512"
                              width="21.5px"
                              height="25px"
                            >
                              <path
                                fill="currentColor"
                                d="M100.28 448H7.4V148.9h92.78zM53.79 108.1C24.09 108.1 0 83.79 0 54.14 0 24.37 24.09 0 53.79 0 83.3 0 107.6 24.37 107.6 54.14c.1 29.64-24.2 53.96-53.81 53.96zM447.4 448h-92.68V302.4c0-34.7-.7-79.29-48.32-79.29-48.32 0-55.7 37.72-55.7 76.79V448H157.3V148.9h88.94v40.8h1.28c12.4-23.41 42.62-48.32 87.76-48.32 93.9 0 111.18 61.81 111.18 142.3V448z"
                              />
                            </svg>
                            linkedin
                          </Link>
                        </div>
                      </div>
                      <div className="w-full py-12 px-11 bg-white shadow-lg rounded-b-lg">
                        <p className="text-24 mb-4">Join our Newsletter</p>
                        <input
                          placeholder="Email address"
                          className="p-3 bg-white border border-border rounded-lg mb-2 w-full focus:outline-0 focus:border-primary"
                        />
                        <button className="bg-primary w-full px-7 border text-base text-white border-primary py-4 rounded-sm hover:bg-transparent hover:text-primary">
                          Subscribe
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}