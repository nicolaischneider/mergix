#!/usr/bin/env python3
import os
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
# simulated output

def get_simulated_merge_output(case=0):
    outputs = {
        0: """
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:
	renamed:    dir1/file4.txt -> file3_renamed.txt

Unmerged paths:
  (use "git add/rm <file>..." as appropriate to mark resolution)
	both modified:   file1.txt
	deleted by them: file2.txt
	deleted by them: file3.txt
	both added:      new_file.txt
""",
        1: """
Auto-merging README.md
Auto-merging tests/test_api.py
""",
        2: "Some Output"
    }
    
    return outputs.get(case, "Invalid case specified. Please use 0, 1 or 2.")