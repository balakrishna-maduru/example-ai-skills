SUPPORTED_MODEL_CAPABILITIES = {
    "tool_calling": True,
    "structured_output": True,
}


def test_model_capabilities():

    assert (
        SUPPORTED_MODEL_CAPABILITIES["tool_calling"]
        is True
    )

    assert (
        SUPPORTED_MODEL_CAPABILITIES["structured_output"]
        is True
    )