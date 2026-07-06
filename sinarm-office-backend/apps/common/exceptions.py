"""Application and domain exception hierarchy."""

from __future__ import annotations


class DomainException(Exception):
    """Base exception for domain-level failures."""


class BusinessRuleViolation(DomainException):
    """Raised when an operation violates a business rule."""


class ValidationException(DomainException):
    """Raised when domain input is invalid."""


class AuthorizationException(DomainException):
    """Raised when an actor is not allowed to perform an operation."""


class NotFoundException(DomainException):
    """Raised when a required resource cannot be found."""
