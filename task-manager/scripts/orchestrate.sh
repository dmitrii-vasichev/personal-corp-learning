#!/bin/bash
set -euo pipefail

# Проверка: переданы ли аргументы
if [ $# -eq 0 ]; then
  echo "Usage: ./orchestrate.sh <issue1> <issue2> ..."
  exit 1
fi

REPO_ROOT=$(git rev-parse --show-toplevel)
WORKTREE_DIR="${REPO_ROOT}/.claude/worktrees"
PIDS=()

for ISSUE in "$@"; do
  BRANCH="feat/${ISSUE}-auto"
  WORK_PATH="${WORKTREE_DIR}/${BRANCH}"
  
  echo "🚀 Starting agent for Issue #${ISSUE}..."
  
  # 1. Создай worktree
  git worktree add "$WORK_PATH" -b "$BRANCH" 2>/dev/null || {
    echo "⚠️  Worktree for #${ISSUE} already exists, skipping creation"
  }
  
  # 2. Запусти claude -p в фоне
  (
    cd "$WORK_PATH"
    claude -p "Read GitHub Issue #${ISSUE}. Implement the task described in the issue. Then: git add, commit, push, and create a PR with 'Closes #${ISSUE}' in the body." \
      --allowedTools "Bash(git:*)" "Bash(gh:*)" "Read" "Write" "Edit" \
      > "/tmp/agent-${ISSUE}.log" 2>&1
  ) &
  
  PIDS+=($!)
done

echo ""
echo "⏳ Waiting for ${#PIDS[@]} agents to finish..."
wait

echo ""
echo "✅ All agents finished. Check PRs:"
for ISSUE in "$@"; do
  echo "  - Issue #${ISSUE}: /tmp/agent-${ISSUE}.log"
done
