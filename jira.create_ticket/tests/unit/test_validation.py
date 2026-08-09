import pytest

from src.skill import (
    JiraCreateTicketSkill,
    SkillValidationError,
)


def test_valid_input():

    skill = JiraCreateTicketSkill()

    data = {
        "project": "ENG",
        "summary": "Fix login issue",
        "issue_type": "Bug",
    }

    skill.validate(data)


def test_missing_project():

    skill = JiraCreateTicketSkill()

    data = {
        "summary": "Fix login issue",
        "issue_type": "Bug",
    }

    with pytest.raises(SkillValidationError):
        skill.validate(data)


def test_invalid_issue_type():

    skill = JiraCreateTicketSkill()

    data = {
        "project": "ENG",
        "summary": "Fix login issue",
        "issue_type": "DeleteEverything",
    }

    with pytest.raises(SkillValidationError):
        skill.validate(data)


def test_summary_too_long():

    skill = JiraCreateTicketSkill()

    data = {
        "project": "ENG",
        "summary": "x" * 300,
        "issue_type": "Bug",
    }

    with pytest.raises(SkillValidationError):
        skill.validate(data)