from enum import Enum, auto


class ConflictType(Enum):
    CONTENT = auto()
    MODIFY_DELETE = auto()
    ADD_ADD = auto()
    RENAME = auto()
    MODE_CHANGE = auto()
    SUBMODULE = auto()
    UNKNOWN = auto()


def get_conflict_type(conflict_type):
    conflict_messages = {
        ConflictType.CONTENT: "Content Conflicts (these require changes within the code):",
        ConflictType.MODIFY_DELETE: "Modify/Delete Conflicts:",
        ConflictType.ADD_ADD: "Add/Add Conflicts:",
        ConflictType.RENAME: "Rename Conflicts:",
        ConflictType.MODE_CHANGE: "Mode Change Conflicts:",
        ConflictType.SUBMODULE: "Submodule Conflicts:",
        ConflictType.UNKNOWN: "Unknown Conflicts:"
    }
    return conflict_messages[conflict_type]


def categorize_conflicts(conflicts):
    categorized_conflicts = {
        ConflictType.CONTENT: [],
        ConflictType.MODIFY_DELETE: [],
        ConflictType.ADD_ADD: [],
        ConflictType.RENAME: [],
        ConflictType.MODE_CHANGE: [],
        ConflictType.SUBMODULE: [],
        ConflictType.UNKNOWN: []
    }

    for state, file in conflicts:
        conflict_type = ConflictType.UNKNOWN
        if state == 'both modified':
            conflict_type = ConflictType.CONTENT
        elif state in ['deleted by them', 'deleted by us']:
            conflict_type = ConflictType.MODIFY_DELETE
        elif state == 'both added':
            conflict_type = ConflictType.ADD_ADD
        elif 'renamed' in state:
            conflict_type = ConflictType.RENAME
        elif 'mode' in state:
            conflict_type = ConflictType.MODE_CHANGE
        elif 'submodule' in state:
            conflict_type = ConflictType.SUBMODULE

        categorized_conflicts[conflict_type].append((file, state))

    return categorized_conflicts
