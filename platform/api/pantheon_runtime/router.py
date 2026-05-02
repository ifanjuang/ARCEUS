"""Backward-compatible shim for context export routes.

New imports must use `pantheon_context.router`.

This module remains only to avoid abrupt breakage for any legacy internal import
that still references `pantheon_runtime.router`. It must not grow new routes,
execution logic, task execution, tool calls, workflow execution or memory
promotion.
"""

from __future__ import annotations

from pantheon_context.router import get_context_pack, router

__all__ = ["get_context_pack", "router"]
