#!/usr/bin/env python3

##############################
# gitmassclone.py #
# =============== #
# Clone multiple Github repositories with a single command in terminal.
# Copyright (c)2025 Ivaylo Vasilev. Released under the MIT License; see LICENSE for details.
# Author: Ivaylo Vasilev
##############################

import argparse
import shutil
import subprocess
import sys
import os

parser = argparse.ArgumentParser(prog="gitmassclone", description="Clone multiple github repositories using git", epilog="(c)Ivaylo Vasilev")
parser.add_argument("-l", "--list", metavar="TXT", required=True, help="specify list file with repositories (.txt)")
args = parser.parse_args()

git_installed = shutil.which("git")
if git_installed == None:
    print("warning: git is not installed on the system")
    sys.exit(1)

repos_file = args.list
if not os.path.exists(repos_file):
    print(f"error: '{repos_file}' does not exist")
    sys.exit(2)

with open(repos_file, "r") as file:
    repos = file.readlines()

for repo in repos:
    url = repo.rstrip("\n")
    clonedir = url.split("/")[-1].rstrip(".git")
    
    if os.path.exists(clonedir):
        print(f"* {url} already cloned")
    else:
        command = f"git clone {url}"
        subprocess.run(command, shell=True, stdout=None, stderr=None)
