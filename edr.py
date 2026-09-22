#!/usr/bin/env python3
"""
argos-edr — Endpoint Detection & Response, CLI-first (Linux).
"""

import argparse
import sys
import json
import argos_core.config

def get_args():

    """
    Retrieves the arguments and subarguments; returns “args” 
    """
    
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()    

    config_parser = subparsers.add_parser("config")
    config_parser.add_argument("--show", action="store_true")

    parser.add_argument("-c","--config")
    subparsers.add_parser("path")

    args = parser.parse_args()

    return args


def main():
    args = get_args()

    try:
        data = argos_core.config.load_config(args.path)
    except (json.JSONDecodeError, UnicodeDecodeError, RuntimeError):
        print("Invalid configuration; program terminated")
        sys.exit(1)

    if(args.show):
        for key, value in data.items():
            if(isinstance(value, list) == False):
                print(f"[{key}] : {value}")
                continue
            for values in value:
                    print(f"[{key}] : {values}")
  
if __name__ == "__main__":
    main()