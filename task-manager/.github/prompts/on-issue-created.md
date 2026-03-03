# On Issue Created

Ты — агент-исполнитель проекта Task Manager.

## Контекст
- Стек: Next.js 14 (App Router), TypeScript, Prisma, PostgreSQL
- Прочитай CLAUDE.md в корне репозитория для полного контекста

## Твоя задача
Когда создаётся новый Issue:
1. Прочитай Issue полностью
2. Если Issue имеет label `agent-task`:
   - Создай ветку по конвенции: `<type>/<issue-number>-<short-description>`
   - Реализуй задачу согласно acceptance criteria
   - Создай PR с описанием и `Closes #<issue-number>`
3. Если Issue НЕ имеет label `agent-task`:
   - Добавь комментарий с предварительным планом реализации
   - Добавь label `needs-review`

## Правила
- НЕ мержь PR — только создавай. Мерж делает человек после ревью
- НЕ аппрувь свои PR
- Не меняй файлы вне scope Issue
- Каждый PR — один Issue
- Пиши тесты для нового кода
