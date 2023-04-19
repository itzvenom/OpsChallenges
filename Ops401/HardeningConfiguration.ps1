# Script : HardeningConfiguration.ps1
# Purpose: Write a PowerShell script that automates the configuration of the settings: 1.1.5 (L1) and 18.3.2 (L1) from CIS Benchmarks
# Why    : Automating the process will save a lot of time in the long run.

# Ensure 'Configure SMB v1 server' is set to 'Disabled'
Set-SmbServerConfiguration -EnableSMB1Protocol $false

#########################################################################

# Set 'Password must meet complexity requirements' to 'Enabled'

# Export the current security configuration to a file for modification
secedit /export /cfg C:\securityconfig.cfg

# Specify the path to the exported security configuration file
$seceditfile = "C:\securityconfig.cfg"

# Check if the Password Complexity policy is already enabled in the configuration file
$PasswordPolicy = Get-Content $seceditfile | Select-String "PasswordComplexity ="
if($PasswordPolicy -eq $null){
    # If the policy is not found, exit the script with an error message
    Write-Output "Password Complexity policy not found"
    exit
}

if($PasswordPolicy.ToString().Contains("1")){
    # If the policy is already enabled, output a message indicating that
    Write-Output "Password complexity policy is already enabled"
}
else{
    # If the policy is not enabled, modify the security configuration file to enable it
    Write-Output "Enabling password complexity policy"
    (Get-Content $seceditfile).Replace("PasswordComplexity = 0","PasswordComplexity = 1") | Set-Content $seceditfile
    
    # Apply the modified security configuration file to the local security policy database
    secedit /configure /db C:\Windows\security\local.sdb /cfg $seceditfile /areas SECURITYPOLICY
    
    # Output a message indicating that the policy has been enabled
    Write-Output "Password complexity policy has been enabled"
}
