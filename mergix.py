#!/usr/bin/env python3

#from merge_output_retriever import get_merge_message, get_simulated_merge_output
from asci_codes import BOLD, RED, GREEN, YELLOW, RESET
from conflict_formatter import process_conflicts, format_other_conflicts, format_content_conflicts

import subprocess
import re

def get_merge_conflicts():
    try:
        # Run 'git status' command
        status_output = subprocess.check_output(['git', 'status'], universal_newlines=True)
        
        # Check if we're in a merge state
        if "You have unmerged paths." not in status_output:
            return None

        # Use regex to find conflicting files and their states
        conflict_pattern = re.compile(r'\t(.*?):\s*(.*)')
        conflicts = conflict_pattern.findall(status_output)

        return conflicts

    except subprocess.CalledProcessError:
        return None

def categorize_conflicts(conflicts):
    content_conflicts = []
    modify_delete_conflicts = []
    other_conflicts = []

    for file, state in conflicts:

        if 'both modified' in file:
            content_conflicts.append(state)
        elif state in ['deleted by them', 'deleted by us']:
            modify_delete_conflicts.append(file)
        else:
            other_conflicts.append((file, state))

    return content_conflicts, modify_delete_conflicts, other_conflicts

def mergix():
    conflicts = get_merge_conflicts()

    if conflicts is None:
        print("No merge conflicts found or not in a Git repository.")
        return

    content_conflicts, modify_delete_conflicts, other_conflicts = categorize_conflicts(conflicts)

    total_conflicts = len(content_conflicts) + len(modify_delete_conflicts) + len(other_conflicts)
    print(f"We found {total_conflicts} conflicts.")

    print("\nContent Conflicts: (these require changes within the code)")
    for conflict in content_conflicts:
        print(f"* {conflict}")

    print("\nModify/Delete Conflicts:")
    for conflict in modify_delete_conflicts:
        print(f"* {conflict}")

    if other_conflicts:
        print("\nOther Conflicts:")
        for file, state in other_conflicts:
            print(f"* {file} ({state})")

if __name__ == "__main__":
    mergix()