# 101: warm-up scripts for the five practices

Tiny Python files that show one mechanism at a time, with invented values and no pipeline.
Run each folder just before its section in `DEMO_SCRIPT.md`. Nothing here touches `work` or `checkpoints`

| Run before | Folder | Shows |
| --- | --- | --- |
| 2.1 Error handling | `01_error_handling` | An error stops the code, `raise`, `try`/`except`, exit codes |
| 2.2 Code quality | None | The demo itself is the illustration: `flake8` lists, `black` rewrites |
| 2.3 Configuration | `02_configuration` | Dictionaries, `config.yaml`, `yaml.safe_load`, missing settings |
| 2.4 Logging | `03_logging` | Levels, format, screen and file, logging errors |
| 2.5 Security | `04_security` | `os.getenv`, `.env`, `load_dotenv`, `.env.example`, `.gitignore` |

Each folder has a `STEPS.md` (what to run, what to expect, what to say) and one `stepN_*.py` file per step

Files the scripts create (`logs/`) and the `.env` you create by hand are already excluded by the root `.gitignore`
