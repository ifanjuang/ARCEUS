"""Migration 0012 — Traçabilité orchestra + agent_runs

Ajoute les colonnes nécessaires pour exploiter en production les traces
multi-agents et séparer proprement les erreurs des résultats produits.

Tables impactées :
  - orchestra_runs
      + subtasks         JSONB  — décomposition Zeus persistée (id, pattern, agents, deps)
      + subtask_results  JSONB  — résultats par sous-tâche {task_id: {agent: result}}
      + veto_agent       VARCHAR(64)  — agent ayant émis un veto (themis|hephaistos|...)
      + veto_motif       TEXT         — extrait du motif du veto
      + error_message    TEXT         — séparé de final_answer (échecs distincts du contenu)
  - agent_runs
      + error_message    TEXT         — séparé de result (erreurs distinctes du contenu)

Tous les ajouts sont nullable ou ont un DEFAULT — aucune lecture existante n'est cassée.

Revision ID: 0012
Revises: 0011
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0012"
down_revision = "0011"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ── orchestra_runs ──────────────────────────────────────────────
    op.add_column(
        "orchestra_runs",
        sa.Column(
            "subtasks",
            postgresql.JSONB,
            nullable=False,
            server_default=sa.text("'[]'::jsonb"),
        ),
    )
    op.add_column(
        "orchestra_runs",
        sa.Column(
            "subtask_results",
            postgresql.JSONB,
            nullable=False,
            server_default=sa.text("'{}'::jsonb"),
        ),
    )
    op.add_column(
        "orchestra_runs",
        sa.Column("veto_agent", sa.String(64), nullable=True),
    )
    op.add_column(
        "orchestra_runs",
        sa.Column("veto_motif", sa.Text, nullable=True),
    )
    op.add_column(
        "orchestra_runs",
        sa.Column("error_message", sa.Text, nullable=True),
    )

    # Index utile pour la supervision : retrouver les runs en erreur ou avec veto
    op.create_index(
        "ix_orchestra_runs_status",
        "orchestra_runs",
        ["status"],
    )
    op.create_index(
        "ix_orchestra_runs_veto_agent",
        "orchestra_runs",
        ["veto_agent"],
    )

    # ── agent_runs ──────────────────────────────────────────────────
    op.add_column(
        "agent_runs",
        sa.Column("error_message", sa.Text, nullable=True),
    )
    op.create_index(
        "ix_agent_runs_status",
        "agent_runs",
        ["status"],
    )


def downgrade() -> None:
    op.drop_index("ix_agent_runs_status", table_name="agent_runs")
    op.drop_column("agent_runs", "error_message")

    op.drop_index("ix_orchestra_runs_veto_agent", table_name="orchestra_runs")
    op.drop_index("ix_orchestra_runs_status", table_name="orchestra_runs")
    op.drop_column("orchestra_runs", "error_message")
    op.drop_column("orchestra_runs", "veto_motif")
    op.drop_column("orchestra_runs", "veto_agent")
    op.drop_column("orchestra_runs", "subtask_results")
    op.drop_column("orchestra_runs", "subtasks")
