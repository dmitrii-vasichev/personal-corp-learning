# Task Entity Schema

This document defines the data model for the `Task` entity used in the task-manager project.

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `string` | Required | Unique identifier for the task (UUID v4) |
| `title` | `string` | Required | Short human-readable title of the task |
| `description` | `string` | Optional | Detailed description of the task |
| `status` | `enum` | Required | Current state of the task (see values below) |
| `priority` | `enum` | Required | Importance level of the task (see values below) |
| `createdAt` | `string (ISO 8601)` | Required | Timestamp when the task was created |
| `updatedAt` | `string (ISO 8601)` | Required | Timestamp when the task was last updated |

## Enum Values

### Status

| Value | Description |
|-------|-------------|
| `todo` | Task has not been started yet |
| `in_progress` | Task is currently being worked on |
| `done` | Task has been completed |

### Priority

| Value | Description |
|-------|-------------|
| `low` | Task can be addressed when time permits |
| `medium` | Task should be addressed in the normal course of work |
| `high` | Task requires urgent attention |

## Example

```json
{
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "title": "Implement user authentication",
  "description": "Add JWT-based authentication with login and registration endpoints.",
  "status": "in_progress",
  "priority": "high",
  "createdAt": "2026-03-01T10:00:00.000Z",
  "updatedAt": "2026-03-02T08:30:00.000Z"
}
```

## Notes

- `id` is generated server-side and should not be set by the client on creation.
- `createdAt` and `updatedAt` are managed automatically by the database layer.
- This schema will be used as the source of truth for generating the Prisma data model.
