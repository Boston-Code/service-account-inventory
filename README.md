# Service Account Inventory

Tooling for discovering, cataloging, and reporting on **Non-Human Identities (NHI)**
across the enterprise — including service accounts, API keys, OAuth clients, and machine credentials.

Feeds into **Saviynt ISPM** for ongoing NHI governance and risk scoring.

## Why This Exists
Unmanaged service accounts are one of the top attack vectors in enterprise environments.
This repo provides automated discovery to ensure every NHI is:
- ✅ Documented with a business owner
- ✅ Scoped to least privilege
- ✅ Rotated on schedule
- ✅ Decommissioned when no longer needed

## Data Sources
| Source | Method |
|---|---|
| Active Directory | LDAP query |
| Azure AD | Microsoft Graph API |
| AWS IAM | Boto3 / AWS SDK |
| GitHub | GitHub API (org-level) |
| Saviynt EIC | REST API |

## Output
Inventory is exported to `reports/nhi-inventory-YYYY-MM-DD.csv` and synced to Saviynt ISPM.

## Run
```bash
pip install -r requirements.txt
python discover.py --sources ad,azure,aws --output reports/
```
