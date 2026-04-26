"""Installer state persistence for Pantheon OS local installer UI."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

INSTALL_STATUS_PATH = Path("install_status.json")

StepStatus = Literal["pending", "running", "ok", "warning", "error"]

DEFAULT_STEPS = {
    "docker": {"label": "Docker", "status": "pending", "message": "Not checked"},
    "docker_compose": {"label": "Docker Compose", "status": "pending", "message": "Not checked"},
    "ollama": {"label": "Ollama", "status": "pending", "message": "Not checked"},
    "env": {"label": ".env", "status": "pending", "message": "Not checked"},
    "containers": {"label": "Containers", "status": "pending", "message": "Not started"},
    "migrations": {"label": "Alembic migrations", "status": "pending", "message": "Not run"},
    "tests": {"label": "Targeted tests", "status": "pending", "message": "Not run"},
    "health": {"label": "API health", "status": "pending", "message": "Not checked"},
    "runtime_registry": {"label": "Runtime registry", "status": "pending", "message": "Not checked"},
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def default_state() -> dict[str, Any]:
    return {
        "version": 1,
        "updated_at": now_iso(),
        "overall_status": "pending",
        "config": {
            "ollama_host": "",
            "chat_model": "qwen2.5:7b",
            "embedding_model": "nomic-embed-text",
            "api_base_url": "http://localhost:8000",
        },
        "steps": DEFAULT_STEPS,
        "logs": [],
    }


def load_state() -> dict[str, Any]:
    if not INSTALL_STATUS_PATH.exists():
        state = default_state()
        save_state(state)
        return state
    try:
        return json.loads(INSTALL_STATUS_PATH.read_text(encoding="utf-8"))
    except Exception:
        state = default_state()
        state["overall_status"] = "warning"
        state["logs"].append({"ts": now_iso(), "level": "warning", "message": "install_status.json was unreadable and has been reset"})
        save_state(state)
        return state


def save_state(state: dict[str, Any]) -> None:
    state["updated_at"] = now_iso()
    state["overall_status"] = compute_overall_status(state)
    INSTALL_STATUS_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def compute_overall_status(state: dict[str, Any]) -> str:
    statuses = [step.get("status", "pending") for step in state.get("steps", {}).values()]
    if any(status == "error" for status in statuses):
        return "blocked"
    if any(status == "warning" for status in statuses):
        return "degraded"
    if statuses and all(status == "ok" for status in statuses):
        return "ready"
    if any(status == "running" for status in statuses):
        return "running"
    return "pending"


def update_step(step_id: str, status: StepStatus, message: str, details: dict[str, Any] | None = None) -> dict[str, Any]:
    state = load_state()
    step = state.setdefault("steps", {}).setdefault(step_id, {"label": step_id})
    step["status"] = status
    step["message"] = message
    if details is not None:
        step["details"] = details
    state.setdefault("logs", []).append({"ts": now_iso(), "level": status, "step": step_id, "message": message})
    save_state(state)
    return state


def update_config(config: dict[str, Any]) -> dict[str, Any]:
    state = load_state()
    current = state.setdefault("config", {})
    for key, value in config.items():
        if value is not None:
            current[key] = value
    save_state(state)
    return state
