export function Topbar() {
  return (
    <header
      style={{
        height: 64,
        borderBottom: "1px solid var(--border)",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        padding: "0 20px",
        background: "var(--panel)",
      }}
    >
      <strong>Operations Console</strong>
      <span style={{ color: "var(--muted)" }}>RU / CIS Yandex-first mode</span>
    </header>
  );
}

