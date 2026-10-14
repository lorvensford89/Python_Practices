"""
Practices of libraries
    - A library is code someone else already wrote that you 'import' in your program 
"""


from el_library import lines
from el_library import bar

from pathlib import Path
import json
import requests
import argparse
import subprocess
from collections import Counter
import logging

def main():
    lines(2)
    bar("-")
    practices()
    bar("-")
    lines(1)



def practices():
    # 1) pathlib: work with files and folders
    # TODO: Print every file in a folder with its size 
    for f in Path(".").iterdir():
        if f.is_file():
            print(f"{f.name:<20} -> {f.stat().st_size} bytes")
    # to show only .py files(f.suffix == ".py")
    lines(2)

    # 2) json: save and load data
    # TODO: store a config in a file and read it
    config = {
        "host": "localhost",
        "port": 8080,
        "debug": True
    }
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)
    with open("config.json") as f:
        loaded = json.load(f)
    print(loaded["port"])
    # if the files does not exist, create it with defaults
    lines(2)

    # 3) requests: talk to websites
    # TODO: write a mini health checker that tells you if a site is up
    urls = ["https://example.com", "https://python.org"]
    for url in urls:
        try:
            r = requests.get(url, timeout=5)
            print(f"{url:<20} -> {r.status_code}")
        except requests.RequestException as e:
            print(f"{url:<20} -> DOWN: {e}")
    # measure how long each request takes (r.elapsed.total_second())
    lines(2)

    # 4) argparse: make your script a real command-line tool
    # TODO: a script that greets a name, N times
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("--times", type=int, default=1)
    args = parser.parse_args()
    for i in range(args.times):
        print(f"Hello, {args.name}")
    # run it with: python file.py EL --times 3
    lines(2)

    # 5) subprocess: run system commands from python
    # TODO: check disk usage and print it
    result = subprocess.run(["df", "-h"], capture_output=True, text=True)
    print(result.stdout)
    print(f"exit code: {result.returncode}")
    # run a command that fails(like ls /nope) and handle returncode != 0
    lines(2)

    # 6) collections.Counter + logging: analyze logs
    # TODO: count log lines INFO, WARNING and ERROR
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    LINES = [
        "INFO started",
        "ERROR db failed",
        "INFO request ok",
        "WARNING slow",
        "ERROR db failed"
    ]
    counts = Counter(line.split()[0] for line in LINES)
    logging.info("Counts: %s", dict(counts))
    # read lines from a real file instead of the list
    lines(2)



if __name__ == "__main__":
    main()