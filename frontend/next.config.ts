import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  allowedDevOrigins: [
    "def750.dev",
    "pijesper.me",
    "*.pijesper.me",
    "*.def750.dev",
  ],
};

export default nextConfig;
