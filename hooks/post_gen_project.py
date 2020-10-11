"""Post-Generate Hooks.

Cookiecutter will automatically run these after the project is created.
The current working directory is the newly created directory by default.
"""
import os
import sys
import glob


try:
    for filename in glob.glob("**/.keep", recursive=True):
        os.remove(filename)
except:
    sys.exit(1)
