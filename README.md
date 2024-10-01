<p align="center">
    <img src="mergix_theme.png" width="1000" alt="Mergix"/>
</p>

# Mergix

Mergix is a simple Python tool that enhances Git merge conflict resolution by providing a clear, categorized view of conflicts.

## Usage

After calling `git merge <your_branch>` (which may have caused some merge conflict), simply call the following command to get a better view of your conflicts:
```
mergix
```

The following are optional parameters that can be added for more info:

- `-o IDE_COMMAND`: Open all files with content conflicts in the specified IDE. Replace `IDE_COMMAND` with the command to launch your preferred IDE (e.g., `code` for Visual Studio Code, `vim` for Vim).
- `-i`: Show detailed information for all content conflicts.

> **Note**: Make sure you run the script from the root directory of your Git repository where the conflicts are present.

## Example:

This:
```
Auto-merging file1.txt
CONFLICT (content): Merge conflict in file1.txt
Auto-merging file2.txt
CONFLICT (content): Merge conflict in file2.txt
Auto-merging file3.txt
CONFLICT (content): Merge conflict in file3.txt
CONFLICT (modify/delete): dir1/file4.txt deleted in feature-branch and modified in HEAD. Version HEAD of dir1/file4.txt left in tree.
CONFLICT (add/add): Merge conflict in new_file.txt
Automatic merge failed; fix conflicts and then commit the result.
```
...turns into this:
```
> We found 5 conflicts.

Content Conflicts (these require changes within the code):
* file1.txt
* file2.txt
* file3.txt

Modify/Delete Conflicts:
* dir1/file4.txt (deleted by them)

Add/Add Conflicts:
* new_file.txt (both added)
```