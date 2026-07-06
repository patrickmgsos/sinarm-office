"""Tests for shared exception hierarchy."""

from __future__ import annotations

from apps.common.exceptions import BusinessRuleViolation, DomainException


def test_business_rule_violation_is_domain_exception() -> None:
    """Business rule violations must be part of the domain exception tree."""
    assert issubclass(BusinessRuleViolation, DomainException)
