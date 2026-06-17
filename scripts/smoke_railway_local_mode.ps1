$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

Write-Output "SMOKE_RAILWAY_LOCAL_MODE_START"

$env:PYTHONPATH = "$Root\src"
$env:HOST = "127.0.0.1"

$listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Parse("127.0.0.1"), 0)
$listener.Start()
$port = $listener.LocalEndpoint.Port
$listener.Stop()

$env:PORT = [string]$port

Write-Output "USING_PORT=$port"

$psi = New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName = "python"
$psi.Arguments = "-m ai_office.http_api"
$psi.WorkingDirectory = $Root
$psi.RedirectStandardOutput = $true
$psi.RedirectStandardError = $true
$psi.UseShellExecute = $false
$psi.CreateNoWindow = $true

$psi.Environment["PYTHONPATH"] = "$Root\src"
$psi.Environment["HOST"] = "127.0.0.1"
$psi.Environment["PORT"] = [string]$port

$process = [System.Diagnostics.Process]::Start($psi)

try {
    $base = "http://127.0.0.1:$port"
    $deadline = (Get-Date).AddSeconds(8)
    $healthy = $false

    while ((Get-Date) -lt $deadline) {
        try {
            $health = Invoke-RestMethod -Uri "$base/health" -TimeoutSec 2
            if ($health.ok -eq $true -and $health.service -eq "ws-ai-office") {
                $healthy = $true
                break
            }
        } catch {
            Start-Sleep -Milliseconds 250
        }
    }

    if (-not $healthy) {
        throw "SERVER_DID_NOT_BECOME_HEALTHY"
    }

    $ready = Invoke-RestMethod -Uri "$base/ready" -TimeoutSec 3
    if ($ready.ready -ne $true) { throw "READY_FALSE" }
    if ($ready.database_enabled -ne $false) { throw "DATABASE_SHOULD_BE_DISABLED" }
    if ($ready.execution_enabled -ne $false) { throw "EXECUTION_SHOULD_BE_DISABLED" }
    if ($ready.local_runner_enabled -ne $false) { throw "LOCAL_RUNNER_SHOULD_BE_DISABLED" }

    $status = Invoke-RestMethod -Uri "$base/status" -TimeoutSec 3
    if ($status.mode -ne "readonly") { throw "STATUS_MODE_NOT_READONLY" }
    if ($status.agents_count -ne 3) { throw "AGENTS_COUNT_UNEXPECTED" }

    Write-Output "SMOKE_RAILWAY_LOCAL_MODE_OK"
} finally {
    if ($null -ne $process -and -not $process.HasExited) {
        $process.Kill()
        $process.WaitForExit(5000) | Out-Null
    }

    if ($null -ne $process) {
        $stdout = $process.StandardOutput.ReadToEnd()
        $stderr = $process.StandardError.ReadToEnd()

        if ($stdout) {
            Write-Output "SERVER_STDOUT"
            Write-Output $stdout
        }

        if ($stderr) {
            Write-Output "SERVER_STDERR"
            Write-Output $stderr
        }
    }
}

Write-Output "SMOKE_RAILWAY_LOCAL_MODE_DONE"
