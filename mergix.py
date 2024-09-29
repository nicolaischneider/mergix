#!/usr/bin/env python3

from merge_output_retriever import get_merge_conflicts, get_simulated_merge_output
from conflict_categorizer import categorize_conflicts
from conflict_formatter import format_number_of_conflicts, format_conflicts

def mergix():

    # access conflicts
    conflicts = get_merge_conflicts()

    if conflicts is None:
        return

    # categorize into types
    categorized_conflicts = categorize_conflicts(conflicts)

    # number of conflicts
    format_number_of_conflicts(categorized_conflicts)

    # print conflicts
    format_conflicts(categorized_conflicts)

    print("")

if __name__ == "__main__":
    mergix()