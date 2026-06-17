# Railway Smokes

## Local smoke

    powershell -NoProfile -ExecutionPolicy Bypass -File scripts\smoke_railway_local_mode.ps1

## Remote smoke

    powershell -NoProfile -ExecutionPolicy Bypass -File scripts\smoke_railway_remote_readonly.ps1

## Expected remote flags

- database_enabled=false
- execution_enabled=false
- local_runner_enabled=false
