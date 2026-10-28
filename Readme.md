# Automatic Git Committer

A lightweight command-line tool, available in Python and Bash, to initialize a Git repository when needed and create a dated commit after reviewing the pending changes.

## Features

- **Auto-Detection**: Checks whether the current directory is inside a Git working tree.
- **Repository Initialization**: Offers to run `git init` automatically if no repository is detected.
- **Change Review**: Displays the changed files and asks for confirmation before staging anything.
- **Safe Commit**: Cancellation leaves the index untouched; if there are no changes, no commit is attempted.
- **Explicit Errors**: Reports failures from Git rather than displaying a success message.
- **Consistent Commit Message**: Uses the current date (`YYYY / MM / DD`) and the subtitle `"this commit is automatic"` in both implementations.
- **Interactive CLI**: Simple command-line menu interface to start the process or exit.

## Requirements

- **Python 3.x** for `Automatico.py`.
- **Bash** for `Automatico.sh`.
- **Git** installed on your system and configured in your system's PATH.
- A Git user name and email configured before creating commits.

## How It Works

1. **Check**: The script verifies whether the current working directory is inside a Git repository.
2. **Initialize (Optional)**: If not found, it prompts you to create one.
3. **Review**: It displays the modified, staged, and untracked files that would be included.
4. **Confirm**: Only after confirmation, it stages all changes (`git add -A`) and creates a commit formatted as follows:
   ```bash
   git commit -m "YYYY / MM / DD" -m "this commit is automatic"
   ```

Declining the confirmation cancels the operation without staging files. Both implementations operate from the directory in which they are launched. `Automatico.py` provides a menu; `Automatico.sh` runs the workflow once and exits.
