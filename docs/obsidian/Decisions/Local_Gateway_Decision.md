# Local Gateway Decision

## Correct decision

Use:

    D:\dev\autocode\ai-bridge

Do not use as base:

    D:\dev\autocode\ai-bridge-local

## Reason

The ai-bridge repository already contains the local gateway that communicates with the Railway API.

The ai-bridge-local folder has a different architecture and should not drive WS AI Office implementation decisions.

## Safety rule

No execution integration until the ai-bridge gateway contract is mapped and approval gates exist.
