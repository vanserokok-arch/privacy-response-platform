type Props = {
  params: Promise<{ caseId: string }>;
};

export default async function CaseDetailPage({ params }: Props) {
  const { caseId } = await params;

  return (
    <section>
      <h1>Case {caseId}</h1>
      <p style={{ color: "var(--muted)" }}>
        Identity profile, matched sources, legal actions, and evidence snapshots.
      </p>
    </section>
  );
}

