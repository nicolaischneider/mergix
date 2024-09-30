import argparse
import sys


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Manage and display information about content conflicts in files.",
        epilog="Example usage: mergix    # Shows all conflicts in a more structured way"
    )

    # Argument to open files in IDE
    parser.add_argument("-o", "--open", metavar="IDE_COMMAND",
                       help="Open all files with content conflicts in the specified IDE")

    # Argument to show more info
    parser.add_argument("-i", "--info", action="store_true",
                       help="Show detailed information for all content conflicts")
    return parser.parse_args()
