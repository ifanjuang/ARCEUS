import pytest
from pydantic import ValidationError

from core.contracts.manifest import (
    ComponentManifest,
    ManifestType,
    SideEffectProfile,
    normalize_manifest,
)


def test_normalize_legacy_api_manifest_merges_depends_on():
    manifest = normalize_manifest(
        {
            "name": "agent",
            "version": "1.0.0",
            "description": "Agent API",
            "prefix": "/agent",
            "depends_on": ["auth", "documents"],
        },
        fallback_id="agent",
        default_type="api_app",
    )

    assert manifest.id == "agent"
    assert manifest.name == "agent"
    assert manifest.type == ManifestType.API_APP
    assert manifest.dependencies == ["auth", "documents"]
    assert manifest.depends_on == ["auth", "documents"]
    assert manifest.prefix == "/agent"


def test_normalize_runtime_manifest_defaults_to_requested_type():
    manifest = normalize_manifest(
        {
            "id": "extract_facts",
            "description": "Extract factual constraints",
            "side_effect_profile": "read_only",
        },
        fallback_id="extract_facts",
        default_type="skill",
    )

    assert manifest.id == "extract_facts"
    assert manifest.type == ManifestType.SKILL
    assert manifest.side_effect_profile == SideEffectProfile.READ_ONLY


def test_manifest_rejects_invalid_prefix():
    with pytest.raises(ValidationError):
        ComponentManifest(id="auth", type="api_app", prefix="auth")


def test_manifest_reports_quality_issues_without_blocking():
    manifest = ComponentManifest(id="browser", type="tool")
    issues = manifest.issues()

    fields = {issue.field for issue in issues}
    assert "description" in fields
    assert "side_effect_profile" in fields
    assert "outputs" in fields
