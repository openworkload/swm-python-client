#!/usr/bin/env python3

import os
import platform
import sys
import io

# For development purpose we need to use swmclient from the sources:
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from swmclient.api import SwmApi
from swmclient.generated.types import File


def main() -> None:
    swm_api = SwmApi(
        url=f"https://{platform.node()}:8443",
        key_file="~/.swm/key.pem",
        cert_file="~/.swm/cert.pem",
        ca_file="/opt/swm/spool/secure/cluster/ca-chain-cert.pem",
    )

    job_script_bytes = bytes("#!/bin/bash\n#SWM image ubuntu:18.04\ndate\nhostname\n", "utf-8")
    io_bytes = io.BytesIO(job_script_bytes)
    io_obj: File = swm_api.submit_job(io_bytes)
    while True:
        if line := io_obj.payload.readline():
            print(line.decode("utf-8").strip())
        else:
            break
    print()


if __name__ == "__main__":
    main()
