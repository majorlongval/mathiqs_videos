# setup.py
import os
import sys
import subprocess
import venv

# Create a virtual environment in the "venv" directory
venv_dir = os.path.join(os.getcwd(), "venv")
venv.create(venv_dir, with_pip=True)

# Add library to PYTHONPATH
lib_path = os.path.abspath(os.path.join(os.getcwd(), "lib"))
bashrc_path = os.path.expanduser("~/.bashrc")
zshrc_path = os.path.expanduser("~/.zshrc")
fishrc_path = os.path.expanduser("~/.config/fish/config.fish")

# The export command for bash and zsh
export_line = f'\nexport PYTHONPATH="${{PYTHONPATH}}:{lib_path}"\n'

# The set command for fish shell
set_fish_line = f'\nset -x PYTHONPATH "${{PYTHONPATH}} {lib_path}"\n'

# Append the export command to the bashrc file if it exists
if os.path.exists(bashrc_path):
    with open(bashrc_path, "a") as bashrc_file:
        bashrc_file.write(export_line)

# Append the export command to the zshrc file if it exists
if os.path.exists(zshrc_path):
    with open(zshrc_path, "a") as zshrc_file:
        zshrc_file.write(export_line)

# Append the set command to the fish config file if it exists
if os.path.exists(fishrc_path):
    with open(fishrc_path, "a") as fishrc_file:
        fishrc_file.write(set_fish_line)

# Install dependencies from requirements.txt in the virtual environment
pip_path = os.path.join(venv_dir, "bin", "pip")
subprocess.run([pip_path, "install", "-r", "requirements.txt"])
