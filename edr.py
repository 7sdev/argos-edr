#!/usr/bin/env python3
"""
argos-edr — Endpoint Detection & Response, CLI-first (Linux).
"""

import argparse
import sys
import json
import argos_core.config
import argos_core.logger

logger = argos_core.logger.get_logger(__name__)

def get_args():
    logger.debug("Function call: get_args")
    """
    Retrieves the arguments and subarguments; returns “args” 
    """
    
    parser = argparse.ArgumentParser(prog="argos-edr",description="go to readme.md")
    parser.add_argument("-c","--config",help="path to json")
    parser.add_argument("-v","--verbose",action="store_true")
    parser.add_argument("--version", action="version", version="0.1.0")

    subparsers = parser.add_subparsers(dest="command", required=True)    
    config_parser = subparsers.add_parser("config",help="Edit the configuration")
    config_parser.add_argument("--show", action="store_true", help="View the current configuration")
    scan_parser = subparsers.add_parser("scan",help="Run a one-time scan")
    monitor_parser = subparsers.add_parser("monitor",help="Start continuous monitoring")

    args = parser.parse_args()
    
    return args


def main():
    logger.debug("Function call: main")
    args = get_args()
    logger.info(" [+] Argos EDR launch")
    try:
        data = argos_core.config.load_config(args.config)
    except (json.JSONDecodeError, UnicodeDecodeError, RuntimeError, IsADirectoryError):
        print("Invalid configuration; program terminated")
        sys.exit(1)

    
    if args.command == "config" and args.show:
            for key, value in data.items():
                if(isinstance(value, list) == False):
                    print(f"[{key}] : {value}")
                    continue
                for values in value:
                        print(f"[{key}] : {values}")
                        logger.info(f" [+] [{key}] : {values}")
    elif args.command == "scan" or args.command == "monitor":
        print(f"[+] {args.command} not implemented")
        logger.error(f"[+] {args.command} not implemented")

    return 0
  
if __name__ == "__main__":
    main()