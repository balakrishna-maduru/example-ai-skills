SUPPORTED_JIRA_VERSIONS = [
    "10.0",
    "10.5",
    "10.10",
    "11.0",
]


def test_supported_jira_versions():

    for version in SUPPORTED_JIRA_VERSIONS:
        major = int(version.split(".")[0])

        assert major in {10, 11}