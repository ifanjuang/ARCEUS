"""Smoke tests for the Pantheon Next Domain Layer API.

These tests intentionally cover only read-only bootstrap endpoints that should
remain stable during refactors.
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["mode"] == "hermes_backed_domain_layer"
    assert "Pantheon Next defines" in payload["doctrine"]


def test_domain_snapshot_endpoint() -> None:
    response = client.get("/domain/snapshot")

    assert response.status_code == 200
    payload = response.json()
    assert "layers" in payload
    assert "agents" in payload
    assert "skills" in payload
    assert "workflows" in payload
    assert "memory_stores" in payload
    assert "knowledge_collections" in payload
    assert "legacy_components" in payload

    assert "pantheon" in payload["layers"]
    assert any(agent["id"] == "zeus" for agent in payload["agents"])
    assert any(memory_store["id"] == "system_memory" for memory_store in payload["memory_stores"])


def test_context_pack_endpoint() -> None:
    response = client.get("/runtime/context-pack")

    assert response.status_code == 200
    payload = response.json()
    assert payload["project"] == "Pantheon Next"
    assert payload["mode"] == "hermes_backed_domain_layer"
    assert payload["route_boundary"] == "read_only_context_export_not_execution_runtime"
    assert "context_export_only" in payload["limitations"]
    assert "domains/general" in payload["domain_packages"]
    assert "domains/architecture_fr" in payload["domain_packages"]
    assert "system" in payload["memory_levels"]
