from src.skill import (
    JiraCreateTicketSkill,
    SkillContext,
)


class FakeJiraConnector:

    def create_issue(
        self,
        *,
        project,
        summary,
        description,
        issue_type,
        priority,
        labels,
    ):

        return {
            "issue_key": "ENG-123",
            "issue_url": (
                "https://jira.example.com/browse/ENG-123"
            ),
        }


def test_create_jira_ticket():

    skill = JiraCreateTicketSkill()

    context = SkillContext(
        connector=FakeJiraConnector(),
        tenant_id="tenant-a",
        user_id="user-123",
        agent_id="engineering-agent",
        trace_id="trace-123",
    )

    result = skill.execute(
        {
            "project": "ENG",
            "summary": "Fix login",
            "issue_type": "Bug",
        },
        context,
    )

    assert result["success"] is True
    assert result["issue_key"] == "ENG-123"