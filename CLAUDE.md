## Package Manager

This project uses **uv** as the Python package manager. Use `uv` for all dependency management (e.g., `uv add`, `uv run`, `uv sync`). Do not use `pip` or `poetry`.

## Principles

See `.claude/rules/best-practices/principles.md` for SOLID, DRY, KISS, YAGNI guidelines.

**NOTE: After making a plan, check the plan against these principles before finalizing it.**

## Meta-Learning

When a decision is made or a pattern is established, add a lean rule (1-2 lines) to `.claude/rules/meta-learning/`. Rules should point to code files/folders as reference — **code is the documentation**. See `.claude/rules/meta-learning/README.md` for format guidelines.

## ADRs

Architecture Decision Records live in `docs/adrs/`. When a significant architectural decision is made during a conversation, **automatically create an ADR** following the template in `docs/adrs/README.md`. Don't wait to be asked — if a decision is made, record it.