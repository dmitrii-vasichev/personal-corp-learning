Реализуй задачу из GitHub Issue.

## Вход
Номер Issue: $ARGUMENTS

## Инструкции

1. Прочитай CLAUDE.md проекта
2. Прочитай Issue по номеру через `gh issue view $ARGUMENTS`
3. Прочитай связанные документы (PRD, план), если они указаны в Issue
4. Создай ветку по формату из CLAUDE.md (например: `feature/<issue-number>-<short-description>`)
5. Реализуй задачу согласно acceptance criteria из Issue
6. После каждого логического изменения — коммит с осмысленным сообщением
7. Когда все acceptance criteria выполнены:
   - Пуш ветки: `git push -u origin <branch-name>`
   - Создай PR через `gh pr create` с `Closes #<issue-number>` в теле
8. Выведи отчёт: что сделано, какие файлы изменены, ссылка на PR
