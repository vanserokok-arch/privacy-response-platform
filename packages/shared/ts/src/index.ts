export const MODULES = [
  "identity-engine",
  "discovery-engine",
  "source-graph",
  "risk-engine",
  "action-orchestrator",
  "legal-engine",
  "monitoring-engine",
  "evidence-vault",
] as const;

export type PlatformModule = (typeof MODULES)[number];

