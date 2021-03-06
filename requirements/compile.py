#!/usr/bin/env python
import os
import subprocess
import sys
from pathlib import Path


if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    os.environ["CUSTOM_COMPILE_COMMAND"] = "requirements/compile.py"
    common_args = ["-m", "piptools", "compile", "--generate-hashes"] + sys.argv[1:]
    subprocess.run(
        [
            "python3.5",
            *common_args,
            "-P",
            "Django>=1.11,<2.0",
            "-o",
            "py35-django111.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.5",
            *common_args,
            "-P",
            "Django>=2.0,<2.1",
            "-o",
            "py35-django20.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.5",
            *common_args,
            "-P",
            "Django>=2.1,<2.2",
            "-o",
            "py35-django21.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.5",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-o",
            "py35-django22.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.6",
            *common_args,
            "-P",
            "Django>=1.11,<2.0",
            "-o",
            "py36-django111.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.6",
            *common_args,
            "-P",
            "Django>=2.0,<2.1",
            "-o",
            "py36-django20.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.6",
            *common_args,
            "-P",
            "Django>=2.1,<2.2",
            "-o",
            "py36-django21.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.6",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-o",
            "py36-django22.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.6",
            *common_args,
            "-P",
            "Django>=3.0a1,<3.1",
            "-o",
            "py36-django30.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.7",
            *common_args,
            "-P",
            "Django>=1.11,<2.0",
            "-o",
            "py37-django111.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.7",
            *common_args,
            "-P",
            "Django>=2.0,<2.1",
            "-o",
            "py37-django20.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.7",
            *common_args,
            "-P",
            "Django>=2.1,<2.2",
            "-o",
            "py37-django21.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.7",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-o",
            "py37-django22.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.7",
            *common_args,
            "-P",
            "Django>=3.0a1,<3.1",
            "-o",
            "py37-django30.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.8",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-o",
            "py38-django22.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.8",
            *common_args,
            "-P",
            "Django>=3.0a1,<3.1",
            "-o",
            "py38-django30.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.9",
            *common_args,
            "-P",
            "Django>=2.2,<2.3",
            "-o",
            "py39-django22.txt",
        ],
        check=True,
    )
    subprocess.run(
        [
            "python3.9",
            *common_args,
            "-P",
            "Django>=3.0a1,<3.1",
            "-o",
            "py39-django30.txt",
        ],
        check=True,
    )
