"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import logify


def test_version_is_set() -> None:
    assert logify.__version__
