from pathlib import Path
from .._base import AgentBase


class Demeter(AgentBase):
    """Collection and data ingestion — fetches PDFs, files, web pages, notes; normalizes data."""

    agent = "DEMETER"
    role = "collector"
    layer = "analysis"
    veto = False
    _soul_dir = Path(__file__).parent / "demeter"
