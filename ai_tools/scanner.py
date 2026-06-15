#!/usr/bin/env python3
"""Small authorized TCP port checker for Termux/Linux."""

from __future__ import annotations

import argparse
import socket
import sys
from typing import Iterable

MAX_PORTS = 100


def parse_ports(values: Iterable[str]) -> list[int]:
    ports: list[int] = []
    for value in values:
        try:
            port = int(value)
        except ValueError as exc:
            raise argparse.ArgumentTypeError(f"Invalid port: {value}") from exc
        if not 1 <= port <= 65535:
            raise argparse.ArgumentTypeError(f"Port out of range: {port}")
        ports.append(port)

    unique_ports = sorted(set(ports))
    if len(unique_ports) > MAX_PORTS:
        raise argparse.ArgumentTypeError(
            f"Too many ports. Maximum per run is {MAX_PORTS}."
        )
    return unique_ports


def check_port(host: str, port: int, timeout: float) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check selected TCP ports on an authorized host."
    )
    parser.add_argument("host", help="Hostname or IP address you are authorized to test")
    parser.add_argument("ports", nargs="+", help="One or more TCP ports")
    parser.add_argument(
        "--timeout",
        type=float,
        default=1.0,
        help="Connection timeout in seconds (default: 1.0)",
    )
    args = parser.parse_args()

    if args.timeout <= 0 or args.timeout > 10:
        parser.error("--timeout must be greater than 0 and no more than 10 seconds")

    try:
        ports = parse_ports(args.ports)
        resolved = socket.gethostbyname(args.host)
    except (argparse.ArgumentTypeError, socket.gaierror) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2

    print(f"[*] Authorized TCP check: {args.host} ({resolved})")
    print(f"[*] Ports: {', '.join(map(str, ports))}")

    open_count = 0
    for port in ports:
        if check_port(args.host, port, args.timeout):
            print(f"[OPEN]   {port}/tcp")
            open_count += 1
        else:
            print(f"[CLOSED] {port}/tcp")

    print(f"[*] Completed. Open ports: {open_count}/{len(ports)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
