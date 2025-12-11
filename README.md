# Quizzettone

Small quiz runner. Usage examples:

From project root (recommended):

```bash
source .venv/bin/activate
python -m quiz_game.quizzettone.main
```

Options:

- `--format {txt,json,auto}`: choose which format to load. Default is `auto`.
  - `txt`: try to load `domande.txt` (or all `.txt` with `--all-txt`).
  - `json`: force `domande.json`.
  - `auto`: prefer `domande.txt` then fallback to `domande.json`.

- `--all-txt`: when used with `--format txt` or with `--format auto`, load all `.txt` files
  from the `quizzettone` package directory and concatenate their questions.

- `--dir PATH`: specify a custom directory to load files from instead of the package
  directory. Useful for testing or using an external question set. Example:

```bash
python -m quiz_game.quizzettone.main --format txt --all-txt --dir /path/to/questions
```

Notes:
- Logs are written to `quiz.log` in the current working directory.
- Files in the repo:
  - `quiz_game/quizzettone/domande.txt`
  - `quiz_game/quizzettone/domande.json`

Enjoy!
