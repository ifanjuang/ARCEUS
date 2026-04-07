"""Migration 0010 — index GIN full-text sur chunks.contenu (hybrid search)

Ajoute un index GIN sur to_tsvector('french', contenu) pour permettre
la recherche full-text PostgreSQL en parallèle de la recherche sémantique pgvector.
Les deux sont fusionnés via RRF (Reciprocal Rank Fusion) dans rag_service.py.

Revision ID: 0010
Revises: 0009
"""
from alembic import op

revision = "0010"
down_revision = "0009"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Index GIN pour la recherche full-text française sur le contenu des chunks
    op.execute("""
        CREATE INDEX IF NOT EXISTS ix_chunks_contenu_fts
        ON chunks
        USING gin(to_tsvector('french', contenu))
    """)

    # Index GIN pg_trgm en complément (pour similarity() et fuzzy matching)
    op.execute("""
        CREATE INDEX IF NOT EXISTS ix_chunks_contenu_trgm
        ON chunks
        USING gin(contenu gin_trgm_ops)
    """)


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS ix_chunks_contenu_trgm")
    op.execute("DROP INDEX IF EXISTS ix_chunks_contenu_fts")
