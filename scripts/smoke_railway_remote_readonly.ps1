param(
    [string]$BaseUrl = "https://web-production-de25.up.railway.app"
)

$ErrorActionPreference = "Stop"

Write-Output "SMOKE_RAILWAY_REMOTE_READONLY_START"
Write-Output "BASE_URL=$BaseUrl"

function Get-Json {
    param([string]$Path)

    $url = "$BaseUrl$Path"
    Write-Output "CHECK $url"
    return Invoke-RestMethod -Uri $url -TimeoutSec 20
}

$health = Get-Json "/health"
$ready = Get-Json "/ready"
$status = Get-Json "/status"
$agents = Get-Json "/agents"
$tasks = Get-Json "/tasks"
$audit = Get-Json "/audit-events"

$agentsList = @($agents.agents)
$tasksList = @($tasks.tasks)
$auditList = @($audit.audit_events)

if ($health.ok -ne $true) { throw "HEALTH_NOT_OK" }
if ($health.service -ne "ws-ai-office") { throw "HEALTH_SERVICE_UNEXPECTED" }
if ($health.mode -ne "readonly") { throw "HEALTH_MODE_UNEXPECTED" }

if ($ready.ok -ne $true) { throw "READY_NOT_OK" }
if ($ready.ready -ne $true) { throw "READY_FALSE" }
if ($ready.database_enabled -ne $false) { throw "DATABASE_SHOULD_BE_DISABLED" }
if ($ready.execution_enabled -ne $false) { throw "EXECUTION_SHOULD_BE_DISABLED" }
if ($ready.local_runner_enabled -ne $false) { throw "LOCAL_RUNNER_SHOULD_BE_DISABLED" }

if ($status.ok -ne $true) { throw "STATUS_NOT_OK" }
if ($status.mode -ne "readonly") { throw "STATUS_MODE_NOT_READONLY" }
if ($status.agents_count -ne 3) { throw "AGENTS_COUNT_UNEXPECTED" }
if ($status.tasks_count -ne 1) { throw "TASKS_COUNT_UNEXPECTED" }

if ($agents.ok -ne $true) { throw "AGENTS_NOT_OK" }
if ($agentsList.Count -ne 3) { throw "AGENTS_LIST_COUNT_UNEXPECTED" }

if ($tasks.ok -ne $true) { throw "TASKS_NOT_OK" }
if ($tasksList.Count -ne 1) { throw "TASKS_LIST_COUNT_UNEXPECTED" }

if ($audit.ok -ne $true) { throw "AUDIT_NOT_OK" }
if ($auditList.Count -lt 4) { throw "AUDIT_COUNT_UNEXPECTED" }

Write-Output "REMOTE_SMOKE_OK"
Write-Output "ready.database_enabled=$($ready.database_enabled)"
Write-Output "ready.execution_enabled=$($ready.execution_enabled)"
Write-Output "ready.local_runner_enabled=$($ready.local_runner_enabled)"
Write-Output "agents_list_count=$($agentsList.Count)"
Write-Output "tasks_list_count=$($tasksList.Count)"
Write-Output "audit_events_count=$($auditList.Count)"
Write-Output "SMOKE_RAILWAY_REMOTE_READONLY_DONE"
