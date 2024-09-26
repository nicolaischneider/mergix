#!/usr/bin/env python3
import os
import subprocess

def get_git_root():
    try:
        return subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], 
                                       universal_newlines=True).strip()
    except subprocess.CalledProcessError:
        return None

def get_merge_message():
    git_root = get_git_root()
    if not git_root:
        return None

    merge_msg_path = os.path.join(git_root, '.git', 'MERGE_MSG')
    if not os.path.exists(merge_msg_path):
        return None

    with open(merge_msg_path, 'r') as file:
        return file.read()

# simulated output

def get_simulated_merge_output(case=0):
    outputs = {
        0: """
Auto-merging src/main.py
CONFLICT (content): Merge conflict in src/main.py
Auto-merging lib/utils.py
CONFLICT (content): Merge conflict in lib/utils.py
Auto-merging tests/test_api.py
CONFLICT (content): Merge conflict in tests/test_api.py
CONFLICT (modify/delete): config.ini deleted in HEAD and modified in feature-branch. Version feature-branch of config.ini left in tree.
CONFLICT (modify/delete): docs/README.md deleted in feature-branch and modified in HEAD. Version HEAD of docs/README.md left in tree.
CONFLICT (content): Merge conflict in lib/test.py
Automatic merge failed; fix conflicts and then commit the result.
""",
        1: """
Auto-merging README.md
Auto-merging tests/test_api.py
""",
        2: "Some Output"
    }
    
    return outputs.get(case, "Invalid case specified. Please use 0, 1 or 2.")