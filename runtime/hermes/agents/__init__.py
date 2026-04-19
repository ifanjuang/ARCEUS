"""Hermes Runtime — all agents organized by layer."""

from .meta import Zeus, Athena, Themis, Hera, Apollo
from .analysis import Hermes, Demeter, Argos, Prometheus, Artemis, Hecate, Metis
from .memory import Hestia, Mnemosyne, Hades
from .output import Kairos, Daedalus, Iris, Aphrodite, Hephaestus
from .system import Ares, Poseidon

ALL_AGENTS = [
    Zeus, Athena, Themis, Hera, Apollo,
    Hermes, Demeter, Argos, Prometheus, Artemis, Hecate, Metis,
    Hestia, Mnemosyne, Hades,
    Kairos, Daedalus, Iris, Aphrodite, Hephaestus,
    Ares, Poseidon,
]

# Core MVP agents — enabled by default at startup
MVP_AGENTS = [Zeus, Athena, Hermes, Hecate, Argos, Prometheus, Apollo, Kairos, Daedalus, Iris, Hestia, Hades]

__all__ = [a.__name__ for a in ALL_AGENTS] + ["ALL_AGENTS", "MVP_AGENTS"]
