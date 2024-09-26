#!/usr/bin/env python3

from merge_output_retriever import get_merge_message, get_simulated_merge_output
from asci_codes import BOLD, RED, GREEN, YELLOW, RESET
from conflict_formatter import process_conflicts, format_other_conflicts, format_content_conflicts

def mergix():
    merge_output = get_simulated_merge_output(2)

    if merge_output is None:
        return

    content_conflicts, other_conflicts = process_conflicts(merge_output)

    if content_conflicts is None:
        print("We couldn't find a merge output.")
        return

    # number of conflicts
    conflict_count = len(content_conflicts) + len(other_conflicts)
    if conflict_count == 0:
        print(f"\nWe found {BOLD}{GREEN}{conflict_count}{RESET} conflicts.")
        return
    else:
        print(f"\nWe found {BOLD}{RED}{conflict_count}{RESET} conflicts.")

    # list of content conflicts
    format_content_conflicts(content_conflicts)

    # other conflicts
    format_other_conflicts(other_conflicts)

if __name__ == "__main__":
    mergix()