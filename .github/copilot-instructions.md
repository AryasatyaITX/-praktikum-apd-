### Repository overview

This repository is a set of small Python exercise submissions (student lab/homework files). Files are organized under `Post-Test-Apd/post-test-apd-*` and `Kelas B1'25/Pertemuan2`.

Key files:
- `post-test-apd-8/i.py` — current active file in editor.
- Other `2509106066-*.py` files are individual exercise solutions; many are independent scripts.

Primary purpose for AI agents:
- Assist with small Python edits, bug fixes, refactors, and lightweight documentation for standalone exercise scripts.

What the agent should assume
- These are single-file Python scripts (often procedural). Keep changes minimal and backwards compatible.
- Python version is not specified; prefer Python 3.9+ syntax but avoid very new features unless requested.

Conventions and patterns discovered
- Files are named with student id and exercise number (e.g., `2509106066-...-PT-3.py`). Treat each as an independent script.
- Many scripts include straightforward input/output or simple computations — avoid adding heavy dependencies.

When editing code
- Prefer minimal, local fixes (small functions, clear variable names). If extracting helpers, add them near the top of the same file.
- Add one small unit test file per edited script only if the user asks for testing; do not introduce test frameworks without permission.

Build/test/debug workflows
- There is no project-level build system or test runner present. Run scripts directly with Python:

```powershell
python "post-test-apd-8/i.py"
```

Integration points / external deps
- No external services or nonstandard libraries were found. Do not add network calls or new packages unless the user requests.

Examples to follow
- For a fix in `post-test-apd-8/i.py`, keep changes localized, add helpful inline comments, and show an example run output in the PR description.

What not to do
- Don't reorganize the repo into packages or change filenames unless the user asks.
- Avoid adding CI, packaging, or dependency files; this repo appears to be a collection of standalone submissions.

If you need more context
- Ask which specific file(s) to modify and whether to run or add tests. If the user wants repository-wide cleanup, request permission first.

End of file — keep this short and actionable.
