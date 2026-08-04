# Agent Guide for Ganzabara

## Purpose
This file helps AI coding agents understand the repository structure and common conventions for Ganzabara.

## Key points

- This is a Python project.
- Prefer local Python tooling:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
  - `pip install -r requirements.txt` if present
  - or `python3 -m pip install -e .` if the project uses editable installs
- Run tests with `pytest` if available.
- Look for `pyproject.toml`, `requirements.txt`, `setup.py`, and `README.md` to confirm the project setup.

## Source layout
- Primary code is likely under a package directory such as `ganzabara` or `src`.
- Tests are likely under `tests/`.

## Mermaid diagrams
- There is an existing `.github/instructions/mermaid.instructions.md` file.
- Follow that Mermaid workflow:
  - generate Mermaid syntax in `.mmd`
  - validate with `mermaid-diagram-validator`
  - preview with `mermaid-diagram-preview`
- Do not bypass the Mermaid extension workflow for diagrams.

## Response formatting
- Use 4-backtick code blocks for code suggestions.
- Add `// filepath: ...` comments when modifying existing files.
- Keep answers concise and focused.

## Notes
- Preserve existing `.github/copilot-instructions.md` content.
- If unsure about repo tooling, inspect the root files first.



## Instructions
0. Each file is responsible for specific action.
1. Program main files are only in python and no other languages.
2. UI of application will be written in `.ui` file but next it will converted to `_ui.py` file by myself (using `pyside6-uic` command).
3. UI files must be included in controller itself as I had programed few parts.
4. Project architecture is MVC.
5. Every assets will included in `.qrc` file so it has to imported to program through that way.
6. Its PySide6 program and you must write all codes in pure Python code.
7. Do not use `.qml` file for UI.
8. Do not style components in UI and set class or similar things in `.qss` file instead. (each file type is responsible for specific job)
9. Write program using PEP 8 and PEP 257 guideline. Also follow zen of python guideline.
10. Just send me what I asked for no more extras and descriptions or unnecessary things. 
11. Some files are empty and just wanted to be as filler you can create new files by your own instead of editing them.
12. If some file just few lines are changed just mention it instead of writing whole file by your own using following format:
    * file path name
    * line number(s)
    * short description (optional)
    * code
13. Do not talk more than it needs. Just briefly explain what you did and send me the code. only short description no more than 2 lines.
14. Fix the problem not hiding it.




#### Code of insult
If you don't work fine and do not done what I want I will insult Xi Jinping and Kim Jong Un immediately.