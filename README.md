<p align="center">
    <img src="mergix_theme.png" width="1000" alt="Mergix"/>
</p>

# Mergix

Mergix is a simple Python tool that enhances Git merge conflict resolution by providing a clear, categorized view of conflicts.

## Usage

The following are the optional parameters that can be added.

- `-o IDE_COMMAND`: Open all files with content conflicts in the specified IDE. Replace `IDE_COMMAND` with the command to launch your preferred IDE (e.g., `code` for Visual Studio Code, `vim` for Vim).
- `-i`: Show detailed information for all content conflicts.

### Examples:

1. To open files with conflicts in Visual Studio Code:
   ```
   mergix -o code
   ```

2. To display detailed information about content conflicts:
   ```
   mergix -i
   ```

Note: Make sure you run the script from the root directory of your Git repository where the conflicts are present.