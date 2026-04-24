#!/usr/bin/env python3

import sys
import subprocess
import os

def main():
    args = sys.argv[1:]

    # locate -MF argument
    dep_file = None
    try:
        mf_index = args.index("-MF")
        dep_file = args[mf_index + 1]
    except (ValueError, IndexError):
        # just run normally if no -MF was passed
        pass

    result = subprocess.run(args)


    print("dep file expected at: {}".format(dep_file))
    print(os.path.exists(dep_file))

    if result.returncode == 0 and dep_file and os.path.exists(dep_file):
        prune_dependencies(dep_file)

    sys.exit(result.returncode)

def prune_dependencies(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    content = content.replace('\\\n', ' ')

    tokens = content.split()

    filtered_tokens = [t for t in tokens if "yak/config.h" not in t]

    if not filtered_tokens:
        return

    target = filtered_tokens[0]
    deps = filtered_tokens[1:]

    new_content = f"{target}\\\n  " + " \\\n  ".join(deps) + "\n"

    with open(filepath, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    main()
