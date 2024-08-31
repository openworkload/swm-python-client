#!/usr/bin/env python3

import os
import sys
import argparse
import platform

# For development purpose we need to use swmclient from the sources:
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from swmclient.api import SwmApi
from swmclient.generated.types import File


def main() -> None:
    parser = argparse.ArgumentParser(description="Request specified job details.")
    parser.add_argument("--job-id", help="Job ID", required=True)
    args = parser.parse_args()

    swm_api = SwmApi(
        url=f"https://{platform.node()}:8443",
        key_file="~/.swm/key.pem",
        cert_file="~/.swm/cert.pem",
        ca_file="/opt/swm/spool/secure/cluster/ca-chain-cert.pem",
    )

    job = swm_api.get_job(args.job_id)
    print(f"Job: {job}")


if __name__ == "__main__":
    main()
