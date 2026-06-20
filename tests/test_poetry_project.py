"""Tests for poetry_project package."""

from __future__ import annotations

from poetry_projcet import __version__


def test_version_is_string() -> None:
    assert isinstance(__version__, str)


def test_version_format() -> None:
    parts = __version__.split(".")
    assert len(parts) >= 2
    assert all(p.isdigit() for p in parts)
