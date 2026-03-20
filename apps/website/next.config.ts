import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Fix for workspace root detection
  outputFileTracingRoot: ".",
  // Ignore TypeScript errors during build
  typescript: {
    ignoreBuildErrors: true,
  },
  // Disable Turbopack for build (use webpack instead)
  // Turbopack is only used for dev in Next.js 16
};

export default nextConfig;