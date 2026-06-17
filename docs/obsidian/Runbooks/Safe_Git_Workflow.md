# Safe Git Workflow

## Rules

- Always inspect status before changes.
- Use exact git add paths.
- Do not use git add .
- Do not use git clean without explicit approval.
- Do not use reset --hard without explicit approval.
- Run smokes before commit.
- Push only after clean commit.

## Standard check

    git status -sb --ignored
    git log --oneline --decorate -8
