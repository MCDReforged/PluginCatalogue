"""
Kind of wrapper for GitHub CLI for Pull Requests

See:
- https://cli.github.com/manual
- https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-github-cli-in-workflows

Environ:
- PR_NUMBER
- GH_TOKEN or github_api_token
"""

import os
import subprocess
from typing import Optional

from common.log import logger
from utilities import COMMENT_SIGN

EXECUTABLE = "gh"
PR_NUMBER = os.environ.get("PR_NUMBER")

if 'GH_TOKEN' not in os.environ:
    os.environ['GH_TOKEN'] = os.environ.get('github_api_token', '')

os.environ['NO_COLOR'] = 'true'  # https://cli.github.com/manual/gh_help_environment

logger.info("Initializing gh-cli with PR number: %s", PR_NUMBER)


def pr_comment(body: str, edit_last: bool = False, pr_number: str = PR_NUMBER) -> None:
    """Comment on a PR

    Runs:
        `gh pr comment <pr_number> --body-file <body_file> [--edit-last]`
    """
    try:
        logger.info(f"Commenting on PR: #{pr_number}, edit_last: {edit_last}")

        body_file = 'reply.md'
        with open(body_file, 'w', encoding='utf-8') as f:
            f.write(body)

        cmd = [EXECUTABLE, "pr", "comment", pr_number, "--body-file", body_file]
        if edit_last:
            cmd.append("--edit-last")

        result = subprocess.check_output(cmd)
        logger.info(result.decode("utf-8"))
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to comment: returned {e.returncode}. Output: \n{e.output.decode('utf-8')}")
    except Exception as e:
        logger.error(f"Failed to comment: {e}")


def pr_update_or_comment(user: str, body_file: str, pr_number: str = PR_NUMBER, sign: str = COMMENT_SIGN) -> None:
    """Update last comment of given user if it contains sign, otherwise add a new one

    Checks:
        `gh pr view <pr_number> --json comments --jq <jq_query>`
        `jq_query := .comments | any(.author.login == "<user>" and (.body | contains("<sign>")))`
    """
    cmd = [
        EXECUTABLE, 'pr', 'view', pr_number, '--json', 'comments', '--jq',
        f'.comments | any(.author.login == "{user}" and (.body | contains("{sign}")))'
    ]
    try:
        result = subprocess.check_output(cmd)
        if result.decode("utf-8").startswith("true"):
            logger.info(f"Updating last comment of {user} on PR: #{pr_number}")
            pr_comment(pr_number=pr_number, body=body_file, edit_last=True)
        else:
            pr_comment(pr_number=pr_number, body=body_file)
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to check last comment: returned {e.returncode}. Output: \n{e.output.decode('utf-8')}")
    except Exception as e:
        logger.error(f"Failed to check last comment: {e}")


def pr_label(add_labels: Optional[list[str]] = None, remove_labels: Optional[list[str]] = None, pr_number: str = PR_NUMBER) -> None:
    """Add or remove labels from a PR

    Runs:
        `gh pr edit <pr_number> [--add-label <add_labels>] [--remove-label <remove_labels>]`
    """
    logger.info(f"Labeling PR: #{pr_number}, add_labels: {add_labels}, remove_labels: {remove_labels}")
    cmd = [EXECUTABLE, "pr", "edit", pr_number]
    if add_labels:
        cmd.extend(["--add-label", ",".join(add_labels)])
    elif remove_labels:
        cmd.extend(["--remove-label", ",".join(remove_labels)])
    try:
        result = subprocess.check_output(cmd)
        logger.info(result.decode("utf-8"))
    except Exception as e:
        logger.error(f"Failed to label: {e}")
