#!/usr/bin/env python3

import argparse
import os
import platform
import sys

# For development purpose we need to use swmclient from the sources:
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from swmclient.api import SwmApi
from swmclient.generated.types import File


def print_output(header: str, io_obj: File) -> None:
    print(f"{header.upper()}: ")
    while True:
        if line := io_obj.payload.readline():
            print(line.decode("utf-8").strip())
        else:
            break
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Request stdout and stderr of specified job.")
    parser.add_argument("--job-id", help="Job ID", required=True)
    args = parser.parse_args()

    swm_api = SwmApi(
        url=f"https://{platform.node()}:8443",
        key_file="~/.swm/key.pem",
        cert_file="~/.swm/cert.pem",
        ca_file="/opt/swm/spool/secure/cluster/ca-chain-cert.pem",
    )

    stdout = swm_api.get_job_stdout(args.job_id)
    print_output("stdout", stdout)

    stderr = swm_api.get_job_stderr(args.job_id)
    print_output("stderr", stderr)


if __name__ == "__main__":
    main()
