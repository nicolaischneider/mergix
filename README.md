<p align="center">
    <img src="mergix_theme.png" width="1000" alt="Mergix"/>
</p>

# Mergix

Mergix is a simple Python tool that enhances Git merge conflict resolution by providing a clear, categorized view of conflicts.

## Usage

```
python mergix.py
```
Mergix helps developers quickly understand and navigate merge conflicts, streamlining the resolution process.

## How it works

1. Runs `git status` to detect merge conflicts
2. Categorizes conflicts (e.g., content conflicts, rename conflicts)
3. Displays a formatted summary of all conflicts

## ToDos for Release

- [ ] add arguments (help, option to open files, ...)
- [ ] review all error strings
- [ ] option to show amount of conflicts per file (also the range)
- [ ] open in respective IDE
- [ ] updated documentation based on last changes
- [ ] pep8 formatting (`autopep8 -i -r .`)
- [ ] packaging for easy installation using `pip`