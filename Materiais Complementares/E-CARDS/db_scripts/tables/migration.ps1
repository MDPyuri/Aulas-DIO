#Get the atual directory and set it to the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition

#Return file with all SQL scripts in the directory
$output = Join-Path -Path $scriptDir -ChildPath "migration.sql"

#Verify if the output file already exists, if so delete it
if (Test-Path $output) {
    Remove-Item $output
}

#Get all SQL scripts in the directory and sort them by name
$files = Get-ChildItem -Path $scriptDir -Filter *.sql | Sort-Object Name

#Loop through each file and append its content to the output file
foreach ($file in $files) {
    Get-Content $file.FullName | Out-File -FilePath $output -Append
    "GO" | Out-File -FilePath $output -Append
}

Write-Host "Migration script created at: $output"