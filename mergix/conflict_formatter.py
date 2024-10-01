from .asci_codes import BOLD, RED, GREEN, YELLOW, RESET
from .conflict_categorizer import ConflictType, get_conflict_type
from enum import Enum, auto
import subprocess
import re


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
                    show_conflict_info(file, args.info)
                else:
                    print(f"* {file} ({state})")

    # open files (optional)
    if args.open:
        print("")
        print(f"Opening files with conflicts using command: {args.open}")
        open_files_with_conflicts(args.open, categorized_conflicts)

# Open Conflicts


def open_files_with_conflicts(ide_command, conflicts):
    content_conflicts = conflicts.get(ConflictType.CONTENT, [])

    for file, _ in content_conflicts:
        try:
            subprocess.run([ide_command, file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error opening {file}: {e}")
        except FileNotFoundError:
            print(
                f"IDE command '{ide_command}' not found. Please make sure it's installed and in your PATH.")

# Show Conflict Detail Info


def analyze_file_conflicts(filename):
    try:
        with open(filename, 'r') as file:
            content = file.readlines()

        conflicts = []
        current_conflict_start = None
        for i, line in enumerate(content, start=1):
            if line.startswith('<<<<<<<'):
                current_conflict_start = i
            elif line.startswith('>>>>>>>') and current_conflict_start is not None:
                conflicts.append((current_conflict_start, i))
                current_conflict_start = None

        return len(conflicts), conflicts
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return 0, []
    except Exception as e:
        print(f"Error analyzing {filename}: {e}")
        return 0, []


def show_conflict_info(file, show_info):
    if show_info:
        num_conflicts, ranges = analyze_file_conflicts(file)
        print(
            f"* {file} ({RED}{num_conflicts}{RESET} conflict{'s' if num_conflicts != 1 else ''})")
        for start, end in ranges:
            print(f"   > lines {start}-{end}")
    else:
        print(f"* {file}")
