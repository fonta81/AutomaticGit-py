# Automatic Git Committer (`Automatico.py`)

A simple and lightweight Python automation script to automatically initialize a Git repository (if one doesn't exist) and stage and commit all changes using the current date as the commit message.

## Features

- **Auto-Detection**: Checks if a `.git` repository already exists in the current working directory.
- **Repository Initialization**: Offers to run `git init` automatically if no repository is detected.
- **Automated Staging & Committing**: Stages all files (`git add -A`) and commits them with the current date (format: `YYYY / MM / DD`) and a default subtitle message (`"this commit is automatic"`).
- **Interactive CLI**: Simple command-line menu interface to start the process or exit.

## Requirements

- **Python 3.x**
- **Git** installed on your system and configured in your system's PATH.

## How It Works

1. **Check**: The script verifies if there is a `.git` directory in the folder where it is executed.
2. **Initialize (Optional)**: If not found, it prompts you to create one.
3. **Commit**: If found (or created), it stages all modified/new files and creates a commit formatted as follows:
   ```bash
   git commit -m "YYYY / MM / DD" -m "this commit is automatic"
