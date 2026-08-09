from src.skill import JiraCreateTicketSkill


def test_critical_priority_is_preserved():

    skill = JiraCreateTicketSkill()

    data = {
        "project": "ENG",
        "summary": "Production outage",
        "issue_type": "Bug",
        "priority": "Critical",
    }

    skill.validate(data)

    assert data["priority"] == "Critical"