"""initial schema

Revision ID: 0001_initial_schema
Revises:
Create Date: 2026-04-15
"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision = "0001_initial_schema"
down_revision = None
branch_labels = None
depends_on = None

case_status_enum = sa.Enum("open", "in_review", "closed", name="casestatus")
removal_action_status_enum = sa.Enum("queued", "submitted", "complete", "failed", name="removalactionstatus")


def upgrade() -> None:
    case_status_enum.create(op.get_bind(), checkfirst=True)
    removal_action_status_enum.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "users",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("email", sa.String(length=320), nullable=False, unique=True),
        sa.Column("full_name", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_table(
        "cases",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("owner_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("status", case_status_enum, nullable=False),
        sa.Column("jurisdiction", sa.String(length=128), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_table(
        "person_profiles",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("case_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("cases.id"), nullable=False),
        sa.Column("canonical_name", sa.String(length=255), nullable=False),
        sa.Column("aliases", sa.JSON(), nullable=False),
        sa.Column("meta", sa.JSON(), nullable=False),
    )
    op.create_table(
        "identifiers",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("case_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("cases.id"), nullable=False),
        sa.Column("kind", sa.String(length=64), nullable=False),
        sa.Column("value", sa.String(length=512), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_table(
        "search_tasks",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("case_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("cases.id"), nullable=False),
        sa.Column("provider", sa.String(length=64), nullable=False),
        sa.Column("query", sa.Text(), nullable=False),
        sa.Column("status", sa.String(length=32), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_table(
        "source_records",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("domain", sa.String(length=255), nullable=False),
        sa.Column("url", sa.String(length=1024), nullable=False, unique=True),
        sa.Column("source_type", sa.String(length=64), nullable=False),
        sa.Column("mirror_cluster_key", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_table(
        "source_matches",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("case_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("cases.id"), nullable=False),
        sa.Column(
            "source_record_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("source_records.id"),
            nullable=False,
        ),
        sa.Column("match_score", sa.Float(), nullable=False),
        sa.Column("evidence", sa.JSON(), nullable=False),
    )
    op.create_table(
        "risk_assessments",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("case_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("cases.id"), nullable=False),
        sa.Column("score", sa.Integer(), nullable=False),
        sa.Column("factors", sa.JSON(), nullable=False),
        sa.Column("computed_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_table(
        "removal_actions",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("case_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("cases.id"), nullable=False),
        sa.Column("source_match_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("source_matches.id"), nullable=False),
        sa.Column("status", removal_action_status_enum, nullable=False),
        sa.Column("channel", sa.String(length=64), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
    )
    op.create_table(
        "legal_documents",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("case_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("cases.id"), nullable=False),
        sa.Column("doc_type", sa.String(length=64), nullable=False),
        sa.Column("storage_key", sa.String(length=1024), nullable=False),
        sa.Column("meta", sa.JSON(), nullable=False),
    )
    op.create_table(
        "evidence_snapshots",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("source_match_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("source_matches.id"), nullable=False),
        sa.Column("storage_key", sa.String(length=1024), nullable=False),
        sa.Column("hash_sha256", sa.String(length=128), nullable=False),
        sa.Column("captured_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_table(
        "monitor_rules",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("case_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("cases.id"), nullable=False),
        sa.Column("schedule_cron", sa.String(length=64), nullable=False),
        sa.Column("enabled", sa.Boolean(), nullable=False),
        sa.Column("criteria", sa.JSON(), nullable=False),
    )
    op.create_table(
        "alerts",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("case_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("cases.id"), nullable=False),
        sa.Column("severity", sa.String(length=32), nullable=False),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    for table in [
        "alerts",
        "monitor_rules",
        "evidence_snapshots",
        "legal_documents",
        "removal_actions",
        "risk_assessments",
        "source_matches",
        "source_records",
        "search_tasks",
        "identifiers",
        "person_profiles",
        "cases",
        "users",
    ]:
        op.drop_table(table)
    removal_action_status_enum.drop(op.get_bind(), checkfirst=True)
    case_status_enum.drop(op.get_bind(), checkfirst=True)
