import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  // Fix for workspace root detection
  outputFileTracingRoot: "."
};

export default nextConfig;