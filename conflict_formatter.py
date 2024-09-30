from asci_codes import BOLD, RED, GREEN, YELLOW, RESET
from enum import Enum, auto
from conflict_categorizer import ConflictType, get_conflict_type


def format_number_of_conflicts(categorized_conflicts):
    total_conflicts = sum(len(conflicts)
                          for conflicts in categorized_conflicts.values())
    if total_conflicts == 0:
        print(f"\n> We found {BOLD}{GREEN}{total_conflicts}{RESET} conflicts.")
        return
    else:
        print(f"\n> We found {BOLD}{RED}{total_conflicts}{RESET} conflicts.")


def format_conflicts(categorized_conflicts):
    for conflict_type, conflicts in categorized_conflicts.items():
        if conflicts:
            header = get_conflict_type(conflict_type)
            print(f"\n{BOLD}{RED}{header}{RESET}")
            for file, state in conflicts:
                if conflict_type == ConflictType.CONTENT:
                    print(f"* {file}")
                else:
                    print(f"* {file} ({state})")
