from asci_codes import BOLD, RED, GREEN, YELLOW, RESET
from enum import Enum, auto
from conflict_categorizer import ConflictType, get_conflict_type
import subprocess


def format_number_of_conflicts(categorized_conflicts):
    total_conflicts = sum(len(conflicts)
                          for conflicts in categorized_conflicts.values())
    if total_conflicts == 0:
        print(f"\n> We found {BOLD}{GREEN}{total_conflicts}{RESET} conflicts.")
        return
    else:
        print(f"\n> We found {BOLD}{RED}{total_conflicts}{RESET} conflicts.")


def format_conflicts(args, categorized_conflicts):
    for conflict_type, conflicts in categorized_conflicts.items():
        if conflicts:
            header = get_conflict_type(conflict_type)
            print(f"\n{BOLD}{RED}{header}{RESET}")
            for file, state in conflicts:
                if conflict_type == ConflictType.CONTENT:
                    print(f"* {file}")
                else:
                    print(f"* {file} ({state})")

    # open files (optional)
    if args.open:
        print(f"Opening files with conflicts using command: {args.open}")
        open_files_with_conflicts(args.open, categorized_conflicts)


def open_files_with_conflicts(ide_command, conflicts):
    content_conflicts = conflicts.get(ConflictType.CONTENT, [])

    for file, _ in content_conflicts:
        print(f"Opening {file} with command: {ide_command} {file}")
        try:
            subprocess.run([ide_command, file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error opening {file}: {e}")
        except FileNotFoundError:
            print(f"IDE command '{ide_command}' not found. Please make sure it's installed and in your PATH.")
