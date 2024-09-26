from asci_codes import BOLD, RED, GREEN, YELLOW, RESET

def process_conflicts(merge_output):
    lines = merge_output.split('\n')

    # Check if it's a merge operation
    if not any(line.strip().startswith("Auto-merging") for line in lines):
        return None, None  # Indicate that this wasn't a merge operation

    content_conflicts = []
    other_conflicts = []

    # iterate through lines and filter out conflict messages
    for line in lines:
        if line.startswith("CONFLICT"):
            if "(content):" in line:
                content_conflicts.append(line)
            else:
                other_conflicts.append(line.strip())

    return content_conflicts, other_conflicts

def format_content_conflicts(content_conflicts):
    print(f"\n{BOLD}{RED}Content Conflicts:{RESET}")
    for conflict in content_conflicts:
        file_path = conflict.split("in ")[-1].strip()
        print(f"* {file_path}")

def format_other_conflicts(other_conflicts):
    print(f"\n{BOLD}{RED}Other Conflicts:{RESET}")
    for conflict in other_conflicts:
        # Extract the conflict type from within parentheses
        conflict_type = conflict.split('(')[1].split(')')[0]
        
        # Remove the "CONFLICT (type): " prefix from the message
        conflict_message = conflict.split(': ', 1)[1]
        
        # Print the formatted conflict line
        print(f"- {BOLD}{conflict_type}{RESET}: {conflict_message}")