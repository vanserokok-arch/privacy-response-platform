import Link from "next/link";

const cases = [
  { id: "c-001", title: "Executive profile cleanup", status: "in_review" },
  { id: "c-002", title: "Family doxxing exposure", status: "open" },
];

export default function CasesPage() {
  return (
    <section>
      <h1>Cases</h1>
      <div style={{ display: "grid", gap: 12 }}>
        {cases.map((item) => (
          <Link
            key={item.id}
            href={`/cases/${item.id}`}
            style={{
              padding: 12,
              background: "var(--panel)",
              border: "1px solid var(--border)",
              borderRadius: 8,
            }}
          >
            <strong>{item.title}</strong>
            <div style={{ color: "var(--muted)" }}>{item.status}</div>
          </Link>
        ))}
      </div>
    </section>
  );
}

