#!/bin/bash

# Hook: Stop — перевести Issue в "In Review" после завершения агента
# Требует: переменную окружения ISSUE_NUMBER

if [ -z "$ISSUE_NUMBER" ]; then
  exit 0  # нет номера Issue — ничего не делаем
fi

# Обновляем статус Issue на Project Board
gh issue edit "$ISSUE_NUMBER" --add-label "status: in-review" 2>/dev/null

echo "Hook: Issue #$ISSUE_NUMBER marked for review"
