import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Page Not Found",
  robots: { index: false, follow: true },
};

export default function NotFound() {
  return (
    <section style={{ textAlign: "center", padding: "48px 0" }}>
      <h1>Page not found</h1>
      <p className="muted">That page doesn&apos;t exist or has moved. Pick your vehicle to see what fits it.</p>
      <p>
        <Link className="btn" href="/vehicles">Browse vehicles</Link>{" "}
        <Link className="btn" href="/guides">Browse guides</Link>
      </p>
    </section>
  );
}
