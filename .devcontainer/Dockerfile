FROM mcr.microsoft.com/devcontainers/base:bookworm

# Install build essentials
RUN apt-get update --fix-missing && apt-get install -y --fix-missing build-essential


USER vscode

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc

# Install Claude Code
RUN curl -fsSL https://claude.ai/install.sh | bash