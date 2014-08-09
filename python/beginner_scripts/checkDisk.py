#!/usr/bin/env python


import subprocess

path_dir = "/home/gawaine_ogilvie/python_scripts"

subprocess.call(["df", "-vh", "."])

subprocess.call(["du", "-hs", path_dir])


