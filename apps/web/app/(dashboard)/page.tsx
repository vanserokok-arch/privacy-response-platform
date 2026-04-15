import { Button } from "@/components/ui/button";

type HealthResponse = {
  status: string;
  database?: string;
  redis?: string;
};

async function getBackendHealth(): Promise<HealthResponse> {
  const baseUrl = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";
  try {
    const response = await fetch(`${baseUrl}/health`, { cache: "no-store" });
    if (!response.ok) {
      return { status: "degraded" };
    }
    return (await response.json()) as HealthResponse;
  } catch {
    return { status: "unreachable" };
  }
}

export default async function DashboardPage() {
  const health = await getBackendHealth();

  return (
    <section>
      <h1>Privacy Operations Dashboard</h1>
      <p style={{ color: "var(--muted)" }}>
        Active cases, source clusters, legal queues, and monitoring alerts.
      </p>
      <p style={{ marginTop: 8 }}>
        Backend: <strong>{health.status}</strong> | DB: <strong>{health.database ?? "n/a"}</strong> | Redis:{" "}
        <strong>{health.redis ?? "n/a"}</strong>
      </p>
      <div style={{ marginTop: 16, display: "flex", gap: 8 }}>
        <Button>New Case</Button>
        <Button variant="secondary">Run Discovery</Button>
      </div>
    </section>
  );
}
