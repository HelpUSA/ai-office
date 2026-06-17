# WS AI Office - Local Gateway Decision Correction

Status: corrected architectural decision.

## Correction

The WS AI Office project will not use `D:\dev\autocode\ai-bridge-local` as its local execution base.

The correct local gateway reference is inside:

    D:\dev\autocode\ai-bridge

Reason:

- the `ai-bridge` repository already contains the local gateway;
- that local gateway communicates with the Railway API;
- this keeps the architecture unified around the existing `ai-bridge` cloud/API + local gateway flow;
- the separate `ai-bridge-local` folder should not be treated as the official base for WS AI Office.

## Correct role assignment

### `D:\dev\autocode\ai-bridge`

Role: official AI Bridge reference for both:

- Railway/API side;
- local gateway side.

### `D:\dev\autocode\ai-bridge-local`

Role: not used as WS AI Office base.

It may remain as historical/reference material only if needed, but should not drive implementation decisions.

## Impact on WS AI Office

WS AI Office should evolve toward:

    WS AI Office Railway API
        -> AI Bridge-compatible command/gateway contract
        -> local gateway from ai-bridge
        -> local execution only after approval gates

## Safety rule

No command execution integration should be implemented until:

- the exact local gateway files inside `ai-bridge` are inventoried;
- their Railway communication contract is mapped;
- approval gates are implemented in WS AI Office;
- readonly smokes exist;
- rollback and audit records are defined.
