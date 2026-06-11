import argparse
import csv
import logging
from datetime import datetime
from sources import active_directory, azure_ad, aws_iam, github_org

logger = logging.getLogger(__name__)

SOURCES = {
    "ad":     active_directory.discover,
    "azure":  azure_ad.discover,
    "aws":    aws_iam.discover,
    "github": github_org.discover,
}

def main():
    parser = argparse.ArgumentParser(description="NHI Discovery Tool")
    parser.add_argument("--sources", default="ad,azure,aws,github",
                        help="Comma-separated list of sources to scan")
    parser.add_argument("--output", default="reports/",
                        help="Output directory for inventory CSV")
    args = parser.parse_args()

    all_identities = []
    for source in args.sources.split(","):
        source = source.strip()
        if source in SOURCES:
            logger.info(f"Scanning {source}...")
            identities = SOURCES[source]()
            all_identities.extend(identities)
            logger.info(f"  Found {len(identities)} NHIs in {source}")

    timestamp = datetime.utcnow().strftime("%Y-%m-%d")
    outfile = f"{args.output}nhi-inventory-{timestamp}.csv"

    with open(outfile, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "id", "name", "type", "source", "owner", "last_used",
            "created_date", "privileged", "risk_score"
        ])
        writer.writeheader()
        writer.writerows(all_identities)

    print(f"\n✅ Inventory written to {outfile} ({len(all_identities)} total NHIs)")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
