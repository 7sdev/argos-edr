#!/usr/bin/env python3
"""
argos-edr — Endpoint Detection & Response, CLI-first (Linux).
"""

import argparse
import sys
import json
import argos_core.logger
import argos_core.config


def get_args():
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
    args = get_args() # Calling "args" to retrieve arguments and subarguments

    logger = argos_core.logger.level_logger(verbose=args.verbose) # We define and configure the logger so we can use it from anywhere afterward

    logger.debug("Function call: main")
    try:
        data = argos_core.config.load_config(args.config) # We read the data from the configuration file
    except (json.JSONDecodeError, UnicodeDecodeError, RuntimeError, IsADirectoryError): 
        logger.error("Invalid configuration; program terminated") # If an error occurs, the program terminates with code 1
        sys.exit(1)

    if args.command == "config" and args.show: 
            for key, value in data.items(): # If the "config --show" argument is used, all JSON values and keys are listed
                if(isinstance(value, list) == False):
                    logger.info(f"[{key}] : {value}")
                    continue
                for values in value:
                        logger.info(f"[{key}] : {values}")
    elif args.command == "scan" or args.command == "monitor":
        logger.info(f"[+] {args.command} not implemented")

    return 0
  
if __name__ == "__main__":
    main()