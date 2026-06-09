#!/usr/bin/env python3
"""
LeetCode Progress Tracker Automation Script (with Verbose Logging).

This script parses the repository's README.md file, tracks unique problem IDs
to avoid double-counting across different topic sections, and automatically
updates a dynamic visual dashboard component bounded by tracking tags.
"""

import os
import re
import logging
from typing import Dict, Set

# ==============================================================================
# 1. LOGGING CONFIGURATION
# ==============================================================================
# Setting up standard streaming logs with levels, timestamps, and message types.
logging.basicConfig(
    level=logging.INFO,  # Change to logging.DEBUG for deep internal variable tracking
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("ReadmeTracker")

# ==============================================================================
# 2. CONFIGURATION & REGEX DEFINITION
# ==============================================================================
README_PATH = "README.md"
TARGET_TOTAL_PROBLEMS = 720

# Regex breakdown:
# - \|\s* : Opening vertical border pipe with flexible spaces
# - \[(\d+-[a-zA-Z0-9-]+)\] : Group 1: Captures unique numerical prefix + problem slug identifier
# - \(.*?\)               : Non-greedy match for the hyperlink path
# - \s*\|\s* : Column separation border wall
# - \*?(Easy|Medium|Hard)\*? : Group 2: Captures difficulty names wrapped inside optional formatting asterisks
# - \s*\|                 : Closing vertical row column wall
PROBLEM_ROW_PATTERN = re.compile(
    r"\|\s*\[(\d+-[a-zA-Z0-9-]+)\]\(.*?\)\s*\|\s*\*?(Easy|Medium|Hard)\*?\s*\|"
)


def count_problems() -> Dict[str, int]:
    """
    Parses README.md line by line to extract and deduplicate solved LeetCode problems.
    """
    logger.info("Initializing LeetCode problem parsing cycle...")

    stats: Dict[str, int] = {"Easy": 0, "Medium": 0, "Hard": 0}
    seen_problems: Set[str] = set()

    if not os.path.exists(README_PATH):
        logger.error(
            f"Target execution file missing: '{README_PATH}' was not found in the root directory."
        )
        return stats

    logger.info(f"Successfully located target tracking document: '{README_PATH}'")

    with open(README_PATH, "r", encoding="utf-8") as file:
        lines = file.readlines()

    logger.info(
        f"Scanning through {len(lines)} file markdown data rows for problem matrix matches..."
    )

    # Process line-by-line to extract meaningful verbose contextual data logs
    for line_num, line in enumerate(lines, 1):
        match = PROBLEM_ROW_PATTERN.search(line)
        if match:
            problem_id, difficulty = match.groups()
            logger.debug(
                f"Row Match found on Line {line_num}: ID='{problem_id}' | Diff='{difficulty}'"
            )

            if problem_id not in seen_problems:
                seen_problems.add(problem_id)
                stats[difficulty] += 1
                logger.info(
                    f"  [NEW] Counted unique solution: {problem_id} ({difficulty})"
                )
            else:
                # This log statement flags cross-referenced entries explicitly
                logger.info(
                    f"  [SKIP] Duplicate reference detected on Line {line_num}: '{problem_id}' already indexed under another category."
                )

    logger.info("=== Aggregated Analysis Summary ===")
    logger.info(f"🟢 Easy Solved   : {stats['Easy']}")
    logger.info(f"🟡 Medium Solved : {stats['Medium']}")
    logger.info(f"🔴 Hard Solved   : {stats['Hard']}")
    logger.info(f"🏆 Total Unique  : {len(seen_problems)} / {TARGET_TOTAL_PROBLEMS}")

    return stats


def generate_markdown_table(stats: Dict[str, int]) -> str:
    """
    Assembles a styled markdown progress metric component block.
    """
    logger.info("Constructing text compilation for updated Markdown matrix...")
    total_solved = sum(stats.values())
    completion_percentage = round((total_solved / TARGET_TOTAL_PROBLEMS) * 100, 1)

    # Generate dynamic emoji matrix scale layout block (1 block per 5 problems)
    easy_progress = "🟩" * (stats["Easy"] // 5 or 1) if stats["Easy"] else "⬜"
    medium_progress = "🟨" * (stats["Medium"] // 5 or 1) if stats["Medium"] else "⬜"
    hard_progress = "🟥" * (stats["Hard"] // 5 or 1) if stats["Hard"] else "⬜"

    table_lines = [
        "### 📊 Progress Tracker\n",
        "| Difficulty | Count | Progress |",
        "| :--- | :---: | :--- |",
        f"| 🟢 **Easy** | {stats['Easy']} | {easy_progress} |",
        f"| 🟡 **Medium** | {stats['Medium']} | {medium_progress} |",
        f"| 🔴 **Hard** | {stats['Hard']} | {hard_progress} |",
        f"| 🏆 **Total Solved** | **{total_solved}** / {TARGET_TOTAL_PROBLEMS} | **{completion_percentage}% Completed** |",
    ]

    logger.info(
        f"Successfully built UI Table element with a calculation of {completion_percentage}% progress."
    )
    return "\n".join(table_lines)


def update_readme() -> None:
    """
    Reads the file system target content and injects updated data within target tags.
    """
    stats = count_problems()
    new_metrics_table = generate_markdown_table(stats)

    logger.info(
        f"Opening '{README_PATH}' to locate tracker markdown boundary comments..."
    )
    with open(README_PATH, "r", encoding="utf-8") as file:
        current_content = file.read()

    tracker_regex = r"[\s\S]*"

    # Confirm that boundary anchors exist before performing destructive write actions
    if not re.search(tracker_regex, current_content):
        logger.critical(
            "Process Failed: Could not find the structural markers inside your file!"
        )
        logger.error(
            "Please add the hidden tags to your file before executing this action."
        )
        return

    replacement_target = f"\n\n{new_metrics_table}\n\n"

    logger.info("Substituting old dashboard parameters with calculated metrics...")
    updated_content = re.sub(tracker_regex, replacement_target, current_content)

    logger.info(
        f"Writing updated payload changes back out to filesystem storage on paths: '{README_PATH}'"
    )
    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(updated_content)

    logger.info(
        "File system sync complete. GitHub Action workflow updating sequences terminated successfully."
    )


if __name__ == "__main__":
    update_readme()
