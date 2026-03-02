# Task Manager

Простой менеджер задач на основе Markdown-файлов. Учебный проект для практики агентной разработки в рамках Personal Corp Learning.

## Описание

Task Manager хранит задачи как обычные `.md`-файлы в папке `tasks/`. Каждый файл задачи содержит заголовок, описание и статус. Никакой базы данных — только файловая система и Git.

## Структура

```
task-manager/
├── CLAUDE.md       — инструкции для агента
├── README.md       — описание проекта (этот файл)
└── tasks/          — папка с задачами (markdown-файлы)
```

## Формат файла задачи

Каждый файл в `tasks/` называется `<id>-<slug>.md` и имеет структуру:

```markdown
## Title
Название задачи

## Description
Подробное описание задачи.

## Status
todo | in-progress | done
```

## Quick Start

Создать новую задачу вручную:

1. Создай файл в папке `tasks/`:

```bash
touch tasks/1-my-first-task.md
```

2. Добавь содержимое:

```markdown
## Title
Моя первая задача

## Description
Описание того, что нужно сделать.

## Status
todo
```

3. Сохрани и закоммить:

```bash
git add tasks/1-my-first-task.md
git commit -m "feat: add task 1 — my first task"
```
