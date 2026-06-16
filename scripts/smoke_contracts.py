from ai_office.contracts import CommandContract, build_local_run_command


def test_local_command_shape() -> None:
    command = build_local_run_command(
        command_id="smoke_contracts_001",
        source_chat_id="test-source",
        cwd="D:/dev/autocode/ai-office",
        command=["python", "--version"],
        timeout_seconds=30,
    )

    assert command.action == "run-command"
    assert command.delivery_kind == "local_capability"
    assert command.target_chat_id == "gateway-brain-supervisor"
    assert command.payload_json["cwd"].endswith("ai-office")
    assert command.payload_json["timeout_seconds"] == 30
    assert command.is_local_capability()
    assert not command.requires_approval()


def test_risky_command_requires_approval() -> None:
    command = CommandContract(
        id="danger_001",
        command_id="danger_001",
        action="run-command",
        delivery_kind="local_capability",
        payload_json={
            "cwd": "D:/dev/autocode/ai-office",
            "command": ["powershell", "-Command", "git reset --hard"],
        },
    )

    assert command.requires_approval()


if __name__ == "__main__":
    test_local_command_shape()
    test_risky_command_requires_approval()
    print("SMOKE_CONTRACTS_OK")
