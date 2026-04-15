import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Privacy Response Platform",
  description: "Operations console for digital footprint defense",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

