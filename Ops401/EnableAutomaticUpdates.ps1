# Script : EnableAutomaticUpdates.ps1
# Purpose: This scripts checks if Windows Automatic Updates are enabled and if they are not enables it as well as starting the Windows Update service.
# Why    : As a security control, automatic updates are important for maintaining the security and stability of a system, as they help to keep your system up-to-date with the latest security patches and bug fixes.

# This script will enable automatic updates on Windows 10 if not already enabled

# Check if automatic updates are already enabled
if ((Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update").AUOptions -ne 4) {
  # Set the automatic update settings in the registry
  Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update" -Name AUOptions -Value 4

  # Set the frequency of automatic updates
  Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update" -Name ScheduledInstallDay -Value 0
  Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update" -Name ScheduledInstallTime -Value 3

  # Start the Windows Update service
  Start-Service -Name wuauserv

  Write-Host "Automatic updates have been enabled."
} else {
  Write-Host "Automatic updates are already enabled."
}
