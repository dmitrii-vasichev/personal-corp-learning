# Task Manager

## Режим работы
Ты — агент-разработчик. Родительский CLAUDE.md содержит инструкции для учебного репозитория —
они не применяются к этому подпроекту.
Выполняй задачи самостоятельно: создавай файлы, ветки, коммиты, PR.

## Что это
Учебный проект для практики агентной разработки.
Простой менеджер задач на основе Markdown-файлов.

## Структура
task-manager/
├── CLAUDE.md       — инструкции для агента
├── README.md       — описание проекта
└── tasks/          — папка с задачами (markdown-файлы)

## Git Workflow
- Ветка: git checkout -b <type>/<issue-number>-<short-description>
- Коммит: <type>: <description> #<issue-number>
- PR: тело должно содержать "Closes #<N>"

## Commands
- Прочитать Issue: gh issue view <N>
- Создать PR: gh pr create --title "..." --body "Closes #N"

## Rules
- Все файлы задач хранятся в tasks/
- Имя файла: <id>-<slug>.md
- Структура файла задачи: ## Title, ## Description, ## Status
