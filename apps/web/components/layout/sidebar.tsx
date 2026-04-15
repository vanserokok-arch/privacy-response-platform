import Link from "next/link";

const navItems = [
  { href: "/", label: "Dashboard" },
  { href: "/cases", label: "Cases" },
  { href: "/sources", label: "Sources" },
  { href: "/monitoring", label: "Monitoring" },
  { href: "/legal", label: "Legal Workspace" },
];

export function Sidebar() {
  return (
    <aside
      style={{
        width: 240,
        background: "var(--panel)",
        borderRight: "1px solid var(--border)",
        padding: 20,
      }}
    >
      <h2 style={{ marginTop: 0 }}>Privacy Response</h2>
      <nav style={{ display: "grid", gap: 12 }}>
        {navItems.map((item) => (
          <Link key={item.href} href={item.href} style={{ color: "var(--muted)" }}>
            {item.label}
          </Link>
        ))}
      </nav>
    </aside>
  );
}

