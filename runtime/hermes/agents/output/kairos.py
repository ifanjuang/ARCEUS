from pathlib import Path
from .._base import AgentBase


class Kairos(AgentBase):
    """Contextual synthesis — selects the essential, hierarchizes information, adapts synthesis to situation."""

    agent = "KAIROS"
    role = "synthesizer"
    layer = "output"
    veto = False
    _soul_dir = Path(__file__).parent / "kairos"
