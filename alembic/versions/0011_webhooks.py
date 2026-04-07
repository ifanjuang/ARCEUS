"""Migration 0011 — table webhook_sessions

Lie un canal externe (Telegram chat_id, etc.) à une affaire ARCEUS.
Permet de contextualiser automatiquement les messages entrants.

Revision ID: 0011
Revises: 0010
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = "0011"
down_revision = "0010"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "webhook_sessions",
        sa.Column("id", UUID(as_uuid=False), primary_key=True),
        sa.Column("platform", sa.String(20), nullable=False, server_default="telegram"),
        sa.Column("chat_id", sa.String(128), nullable=False),
        sa.Column(
            "affaire_id",
            UUID(as_uuid=False),
            sa.ForeignKey("affaires.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column(
            "user_id",
            UUID(as_uuid=False),
            sa.ForeignKey("users.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.UniqueConstraint("platform", "chat_id", name="uq_webhook_session"),
    )
    op.create_index("ix_webhook_sessions_chat_id", "webhook_sessions", ["chat_id"])


def downgrade() -> None:
    op.drop_index("ix_webhook_sessions_chat_id", table_name="webhook_sessions")
    op.drop_table("webhook_sessions")
