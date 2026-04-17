"""
Compatibilité : re-exporte tout depuis le package core.services.rag.

L'implémentation est découpée en sous-modules :
  rag/_embed.py   : singleton modèle d'embedding
  rag/_rerank.py  : Reranker cross-encoder
  rag/_ingest.py  : IngestPipeline
  rag/_search.py  : HybridSearcher + _rrf_fusion

Tous les imports existants continuent de fonctionner :
  from core.services.rag_service import RagService
  from core.services.rag_service import _rerank, _rrf_fusion, CHUNK_CONFIG, …
"""
from core.services.rag import (  # noqa: F401
    CHUNK_CONFIG,
    DEFAULT_CHUNK,
    HybridSearcher,
    IngestPipeline,
    RagService,
    _WINDOW_TYPES,
    _rerank,
    _rrf_fusion,
    reranker,
)
