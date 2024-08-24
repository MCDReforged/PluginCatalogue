"""
Kind of wrapper for GitHub CLI for Pull Requests

See:
- https://cli.github.com/manual
- https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-github-cli-in-workflows

Environ:
- PR_NUMBER
- GH_TOKEN or github_api_token
"""

import subprocess
import os
from typing import Optional
from common.log import logger

EXECUTABLE = "gh"
PR_NUMBER = os.environ.get("PR_NUMBER")

if 'GH_TOKEN' not in os.environ:
    os.environ['GH_TOKEN'] = os.environ.get('github_api_token', '')

logger.info("Initializing gh-cli with PR number: %s", PR_NUMBER)

def pr_comment(body_file: str, edit_last: bool = False, pr_number: str = PR_NUMBER) -> None:
    try:
        logger.info(f"Commenting on PR: #{pr_number}, edit_last: {edit_last}")
        cmd = [EXECUTABLE, "pr", "comment", pr_number, "--body-file", body_file]
        if edit_last:
            cmd.append("--edit-last")
        result = subprocess.check_output(cmd)
        logger.info(result.decode("utf-8"))
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to comment: returned {e.returncode}. Output: \n{e.output.decode('utf-8')}")
    except Exception as e:
        logger.error(f"Failed to comment: {e}")


def pr_label(add_labels: Optional[list[str]] = None, remove_labels: Optional[list[str]] = None, pr_number: str = PR_NUMBER) -> None:
    try:
        logger.info(f"Labeling PR: #{pr_number}, add_labels: {
                    add_labels}, remove_labels: {remove_labels}")
        cmd = [EXECUTABLE, "pr", "edit", pr_number]
        if add_labels:
            cmd.extend(["--add-label", ",".join(add_labels)])
        if remove_labels:
            cmd.extend(["--remove-label", ",".join(remove_labels)])
        result = subprocess.check_output(cmd)
        logger.info(result.decode("utf-8"))
    except Exception as e:
        logger.error(f"Failed to label: {e}")
