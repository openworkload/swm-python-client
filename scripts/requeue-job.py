#!/usr/bin/env python3

import argparse
import os
import platform
import sys

# For development purpose we need to use swmclient from the sources:
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from swmclient.api import SwmApi


def main() -> None:
    parser = argparse.ArgumentParser(description="Requeue specified job.")
    parser.add_argument("--job-id", help="Job ID to requeue", required=True)
    args = parser.parse_args()

    swm_api = SwmApi(
        url=f"https://{platform.node()}:8443",
        key_file="~/.swm/key.pem",
        cert_file="~/.swm/cert.pem",
        ca_file="/opt/swm/spool/secure/cluster/ca-chain-cert.pem",
    )
    output = swm_api.requeue_job(args.job_id)
    for line in output.decode("utf-8").split("\n"):
        print(line.strip())


if __name__ == "__main__":
    main()
