from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


class JiraConnector(Protocol):
    """
    Connector interface.

    The skill doesn't know how authentication,
    HTTP communication, retries, etc. are implemented.
    """

    def create_issue(
        self,
        *,
        project: str,
        summary: str,
        description: str | None,
        issue_type: str,
        priority: str | None,
        labels: list[str],
    ) -> dict[str, Any]:
        ...


@dataclass
class SkillContext:
    """
    Runtime context supplied by the Skill Runtime.
    """

    connector: JiraConnector

    tenant_id: str
    user_id: str
    agent_id: str
    trace_id: str


class SkillValidationError(Exception):
    pass


class JiraCreateTicketSkill:
    """
    jira.create_ticket skill.

    Version: 2.1.0
    """

    skill_id = "jira.create_ticket"
    skill_version = "2.1.0"

    def validate(self, data: dict[str, Any]) -> None:
        required_fields = [
            "project",
            "summary",
            "issue_type",
        ]

        for field in required_fields:
            if not data.get(field):
                raise SkillValidationError(
                    f"Missing required field: {field}"
                )

        if data["issue_type"] not in {
            "Bug",
            "Task",
            "Story",
        }:
            raise SkillValidationError(
                "Unsupported issue type"
            )

        if len(data["summary"]) > 255:
            raise SkillValidationError(
                "Summary exceeds 255 characters"
            )

    def execute(
        self,
        data: dict[str, Any],
        context: SkillContext,
    ) -> dict[str, Any]:

        self.validate(data)

        jira = context.connector

        result = jira.create_issue(
            project=data["project"],
            summary=data["summary"],
            description=data.get("description"),
            issue_type=data["issue_type"],
            priority=data.get("priority"),
            labels=data.get("labels", []),
        )

        return {
            "success": True,
            "issue_key": result["issue_key"],
            "issue_url": result["issue_url"],
        }