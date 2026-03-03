"""Create tasks and task_categories tables with seed data

Revision ID: 001
Revises: None
Create Date: 2026-03-02

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Pre-generated UUIDs for seed categories (stable across environments)
CATEGORY_EDUCATION = "a0000000-0000-0000-0000-000000000001"
CATEGORY_STUDENTS = "a0000000-0000-0000-0000-000000000002"
CATEGORY_TECH = "a0000000-0000-0000-0000-000000000003"
CATEGORY_ADMIN = "a0000000-0000-0000-0000-000000000004"
CATEGORY_OTHER = "a0000000-0000-0000-0000-000000000005"


def upgrade() -> None:
    # 1. Create task_categories table
    op.create_table(
        "task_categories",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("name", sa.String(100), nullable=False, unique=True),
        sa.Column("color_hex", sa.String(7), nullable=False),
        sa.Column("icon", sa.String(50), nullable=True),
        sa.Column("is_default", sa.Boolean(), nullable=False, server_default="false"),
        sa.Column("is_archived", sa.Boolean(), nullable=False, server_default="false"),
        sa.Column("created_by", UUID(as_uuid=True), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )

    # 2. Seed 5 default categories
    task_categories = sa.table(
        "task_categories",
        sa.column("id", UUID(as_uuid=True)),
        sa.column("name", sa.String),
        sa.column("color_hex", sa.String),
        sa.column("icon", sa.String),
        sa.column("is_default", sa.Boolean),
    )
    op.bulk_insert(
        task_categories,
        [
            {
                "id": CATEGORY_EDUCATION,
                "name": "Образование",
                "color_hex": "#4CAF50",
                "icon": "book",
                "is_default": False,
            },
            {
                "id": CATEGORY_STUDENTS,
                "name": "Студенты",
                "color_hex": "#2196F3",
                "icon": "users",
                "is_default": False,
            },
            {
                "id": CATEGORY_TECH,
                "name": "Техника",
                "color_hex": "#FF9800",
                "icon": "settings",
                "is_default": False,
            },
            {
                "id": CATEGORY_ADMIN,
                "name": "Административное",
                "color_hex": "#9C27B0",
                "icon": "briefcase",
                "is_default": False,
            },
            {
                "id": CATEGORY_OTHER,
                "name": "Другое",
                "color_hex": "#607D8B",
                "icon": "more-horizontal",
                "is_default": True,
            },
        ],
    )

    # 3. Create tasks table with category_id FK
    op.create_table(
        "tasks",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column(
            "status",
            sa.Enum("todo", "in_progress", "done", name="taskstatus"),
            nullable=False,
            server_default="todo",
        ),
        sa.Column(
            "priority",
            sa.Enum("low", "medium", "high", name="taskpriority"),
            nullable=False,
            server_default="medium",
        ),
        sa.Column(
            "category_id",
            UUID(as_uuid=True),
            sa.ForeignKey("task_categories.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )

    # 4. Create index on tasks.category_id
    op.create_index("idx_tasks_category", "tasks", ["category_id"])


def downgrade() -> None:
    op.drop_index("idx_tasks_category", table_name="tasks")
    op.drop_table("tasks")
    sa.Enum(name="taskstatus").drop(op.get_bind(), checkfirst=True)
    sa.Enum(name="taskpriority").drop(op.get_bind(), checkfirst=True)
    op.drop_table("task_categories")
