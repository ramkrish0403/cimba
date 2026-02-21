# 0001 - FastAPI Server Infrastructure

**Status:** accepted
**Date:** 2026-02-21

## Context
The project needed a foundational server setup to build features on. We chose FastAPI with uvicorn, pydantic-settings for configuration, and a vertical slice architecture for feature organization.

## Decision
Structure the server as: `main.py` (uvicorn entry) → `src/app.py` (FastAPI app with lifespan) → `src/router.py` (central router aggregating feature routers). Settings loaded from env via pydantic-settings in `src/settings.py`. Each feature lives under `src/features/<name>/` with its own router.

## Consequences
- New features add a router in `src/features/<name>/` and register it in `src/router.py`
- Configuration is centralized and type-safe via `src/settings.py`
- Startup/shutdown hooks live in the lifespan context manager in `src/app.py`
