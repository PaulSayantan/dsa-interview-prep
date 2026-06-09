#!/usr/bin/env python3
"""
LeetCode Progress Tracker Automation Script.
Parses unique problem rows from markdown tables and manages the tracker dashboard.
"""

import os
import re
import logging
from typing import Dict, Set

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("ReadmeTracker")

README_PATH = "README.md"
TARGET_TOTAL_PROBLEMS = 720

# Strict regex to capture uniquely formatted problem IDs and difficulties from tables
PROBLEM_ROW_PATTERN = re.compile(
    r"\|\s*\[(\d+-[a-zA-Z0-9-]+)\]\(.*?\)\s*\|\s*\*?(Easy|Medium|Hard)\*?\s*\|"
)


def count_problems() -> Dict[str, int]:
    """Parses README.md to extract and deduplicate solved LeetCode problems."""
    logger.info("Scanning repository documentation for problem entries...")
    stats: Dict[str, int] = {"Easy": 0, "Medium": 0, "Hard": 0}
    seen_problems: Set[str] = set()

    if not os.path.exists(README_PATH):
        return stats

    with open(README_PATH, "r", encoding="utf-8") as file:
        content = file.read()

    matches = PROBLEM_ROW_PATTERN.findall(content)
    for problem_id, difficulty in matches:
        if problem_id not in seen_problems:
            seen_problems.add(problem_id)
            stats[difficulty] += 1

    logger.info(
        f"Deduplication finished. Found {len(seen_problems)} unique solved problems."
    )
    return stats


def generate_markdown_table(stats: Dict[str, int]) -> str:
    """Assembles the clean, styled markdown progress metrics component."""
    total_solved = sum(stats.values())
    completion_percentage = round((total_solved / TARGET_TOTAL_PROBLEMS) * 100, 1)

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
    return "\n".join(table_lines)


def update_readme() -> None:
    """Safely replaces content exclusively within the designated tracking tags."""
    if not os.path.exists(README_PATH):
        logger.error(f"File {README_PATH} not found.")
        return

    stats = count_problems()
    new_metrics_table = generate_markdown_table(stats)

    with open(README_PATH, "r", encoding="utf-8") as file:
        content = file.read()

    start_tag = "<!-- START_METRICS_TRACKER -->"
    end_tag = "<!-- END_METRICS_TRACKER -->"

    # String partitioning prevents any possibility of regex greediness erasing files
    if start_tag not in content or end_tag not in content:
        logger.critical(
            "Aborting update: Could not find the structural tracker markers inside README.md!"
        )
        return

    # Isolate everything before the start tag, and everything after the end tag
    before_tracker = content.split(start_tag)[0]
    after_tracker = content.split(end_tag)[1]

    # Rebuild the file injecting the new stats strictly inside the markers
    updated_content = f"{before_tracker}{start_tag}\n\n{new_metrics_table}\n\n{end_tag}{after_tracker}"

    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(updated_content)

    logger.info(
        "README.md system sync finalized successfully without touching external text."
    )


if __name__ == "__main__":
    update_readme()
