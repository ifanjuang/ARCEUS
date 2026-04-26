param(
    [string]$ChatModel = "qwen2.5:7b",
    [string]$EmbeddingModel = "nomic-embed-text"
)

Write-Host "Pantheon OS - Ollama Windows setup"
Write-Host "Chat model: $ChatModel"
Write-Host "Embedding model: $EmbeddingModel"

Write-Host "Configuring Ollama LAN binding..."
setx OLLAMA_HOST "0.0.0.0:11434" | Out-Null

Write-Host "Pulling chat model..."
ollama pull $ChatModel

Write-Host "Pulling embedding model..."
ollama pull $EmbeddingModel

Write-Host "Opening Windows firewall port 11434 for private network..."
$ruleName = "Ollama 11434 LAN"
$existingRule = Get-NetFirewallRule -DisplayName $ruleName -ErrorAction SilentlyContinue
if ($null -eq $existingRule) {
    New-NetFirewallRule `
        -DisplayName $ruleName `
        -Direction Inbound `
        -LocalPort 11434 `
        -Protocol TCP `
        -Action Allow `
        -Profile Private | Out-Null
    Write-Host "Firewall rule created."
} else {
    Write-Host "Firewall rule already exists."
}

Write-Host "Done. Restart Ollama or reboot Windows before testing from the NAS."
Write-Host "Test locally: curl http://localhost:11434/api/tags"
