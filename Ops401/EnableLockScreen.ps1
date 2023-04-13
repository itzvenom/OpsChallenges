# Script : EnableLockScreen.ps1
# Purpose: This scripts gets an user input, saves it as a variable, converters it to seconds and then changes the registry value of InactivityTimeoutSecs.
# Why    : This can help prevent unauthorized access to the system when a user is away from their computer, for example, if they forget to lock the screen before leaving their desk.

$path = "Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
$name = 'InactivityTimeoutSecs'

$validInput = $false

Write-Host "This script will log you out after completion. Please save all your work!"

while (!$validInput) {
    $userTimeout = Read-Host "Enter the number of minutes before the screen locks out: "
    if ($userTimeout -as [uint16]) {
        $validInput = $true
    } else {
        Write-Host "Invalid input. Please enter a valid integer."
    }
}

$screenTimeout = [int]$userTimeout * 60

try { 
     $property = Get-ItemProperty -Path $path  -Name $name -ErrorAction SilentlyContinue
    
     if ($property) {
        Set-ItemProperty -Path $path -Name $name -Value $screenTimeout 
        Start-Sleep -Seconds 5
        Write-Host "Screen Timeout Updated! You will be logged out in 5 seconds."
        # Usually registry changes are applied right away, except if the process only reads the registry when starting. So just for good measure log out user.
        shutdown.exe -l
     } else {
        New-ItemProperty -Path $path -Name $name -Value $screenTimeout -PropertyType DWord
         Write-Host "Screen Timeout Updated! You will be logged out in 5 seconds."
        Start-Sleep -Seconds 5
        # Usually registry changes are applied right away, except if the process only reads the registry when starting. So just for good measure log out user.
        shutdown.exe -l
     }
} catch { 
     Write-Output $_.Exception.Message 
}
