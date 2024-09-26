#!/usr/bin/env python3

#from merge_output_retriever import get_merge_message, get_simulated_merge_output
from asci_codes import BOLD, RED, GREEN, YELLOW, RESET
from conflict_formatter import process_conflicts, format_other_conflicts, format_content_conflicts

import subprocess
import re

from enum import Enum, auto

class ConflictType(Enum):
    CONTENT = auto()
    MODIFY_DELETE = auto()
    ADD_ADD = auto()
    RENAME = auto()
    MODE_CHANGE = auto()
    SUBMODULE = auto()
    UNKNOWN = auto()


def get_merge_conflicts():
    try:
        status_output = subprocess.check_output(['git', 'status'], universal_newlines=True)
        
        # Check if we're in a merge state
        if "You have unmerged paths." not in status_output:
            return None

        # Extract only the unmerged paths section
        unmerged_section = re.search(r'Unmerged paths:.*?(?=\n\n|\Z)', status_output, re.DOTALL)
        if not unmerged_section:
            return None

        unmerged_output = unmerged_section.group(0)

        # Use regex to find conflicting files and their states, excluding header lines
        conflict_pattern = re.compile(r'\t(\w+.*?):\s*(.*)')
        conflicts = conflict_pattern.findall(unmerged_output)

        return conflicts

    except subprocess.CalledProcessError:
        return None

def categorize_conflicts(conflicts):
    categorized_conflicts = {
        ConflictType.CONTENT: [],
        ConflictType.MODIFY_DELETE: [],
        ConflictType.ADD_ADD: [],
        ConflictType.RENAME: [],
        ConflictType.MODE_CHANGE: [],
        ConflictType.SUBMODULE: [],
        ConflictType.UNKNOWN: []
    }

    for state, file in conflicts:
        conflict_type = ConflictType.UNKNOWN
        if state == 'both modified':
            conflict_type = ConflictType.CONTENT
        elif state in ['deleted by them', 'deleted by us']:
            conflict_type = ConflictType.MODIFY_DELETE
        elif state == 'both added':
            conflict_type = ConflictType.ADD_ADD
        elif 'renamed' in state:
            conflict_type = ConflictType.RENAME
        elif 'mode' in state:
            conflict_type = ConflictType.MODE_CHANGE
        elif 'submodule' in state:
            conflict_type = ConflictType.SUBMODULE

        categorized_conflicts[conflict_type].append((file, state))

    return categorized_conflicts

def mergix():
    conflicts = get_merge_conflicts()

    if conflicts is None:
        print("No merge conflicts found or not in a Git repository.")
        return

    categorized_conflicts = categorize_conflicts(conflicts)

    total_conflicts = sum(len(conflicts) for conflicts in categorized_conflicts.values())
    print(f"We found {total_conflicts} unmerged conflicts.")

    conflict_messages = {
        ConflictType.CONTENT: "Content Conflicts (these require changes within the code):",
        ConflictType.MODIFY_DELETE: "Modify/Delete Conflicts:",
        ConflictType.ADD_ADD: "Add/Add Conflicts:",
        ConflictType.RENAME: "Rename Conflicts:",
        ConflictType.MODE_CHANGE: "Mode Change Conflicts:",
        ConflictType.SUBMODULE: "Submodule Conflicts:",
        ConflictType.UNKNOWN: "Unknown Conflicts:"
    }

    for conflict_type, conflicts in categorized_conflicts.items():
        if conflicts:
            print(f"\n{conflict_messages[conflict_type]}")
            for file, state in conflicts:
                print(f"* {file} ({state})")

if __name__ == "__main__":
    mergix()