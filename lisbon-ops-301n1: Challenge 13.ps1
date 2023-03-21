# Connect to Active Directory
Import-Module ActiveDirectory

# Create new user
New-ADUser -Name "Franz Ferdinand" `
    -GivenName "Franz" `
    -Surname "Ferdinand" `
    -SamAccountName "FranzFerdinand" `
    -Path "CN=Users,DC=corp,DC=globexpower,DC=com" `
    -AccountPassword (ConvertTo-SecureString "P@ssw0rd1" -AsPlainText -Force) `
    -Title "TPS Reporting Lead" `
    -Department "TPS Department" `
    -Company "GlobeX USA" `
    -EmailAddress "ferdi@globexpower.com" `
    -City "Springfield, OR"

# Create new group
New-ADGroup -Name "TPS Department" `
    -Path "OU=GlobeX USA,DC=corp,DC=globexpower,DC=com" `
    -GroupScope Global `
    -GroupCategory Security `
    -Description "Group for TPS Department"

# Create new OU
New-ADOrganizationalUnit -Name "GlobeX USA" `
    -Path "OU=Company,DC=corp,DC=globexpower,DC=com"

