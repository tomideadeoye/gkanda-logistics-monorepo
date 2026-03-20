import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Fix for workspace root detection
  outputFileTracingRoot: ".",
  // Ignore ESLint and TypeScript errors during build
  eslint: {
    ignoreDuringBuilds: true,
  },
  typescript: {
    ignoreBuildErrors: true,
  },
};

export default nextConfig;