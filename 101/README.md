# 101: warm-up scripts for the five practices

Tiny Python files, run just before each section of `DEMO_SCRIPT.md`. Nothing here touches `work` or `checkpoints`

Every folder uses the same example: a customer used the product 8.0 hours; below 10.0 hours we predict churn.
Each step adds one small change to the previous step, marked `# new`

| Run before | Folder | The example grows from |
| --- | --- | --- |
| 2.1 Error handling | `01_error_handling` | A bad value runs silently > a clear error > a planned stop > exit code 1 |
| 2.2 Code quality | None | The demo itself is the illustration: `flake8` lists, `black` rewrites |
| 2.3 Configuration | `02_configuration` | Threshold in the code > in a dictionary > in `config.yaml` > checked |
| 2.4 Logging | `03_logging` | `print` > levels > time and source > screen and file > an error |
| 2.5 Security | `04_security` | Key in the code > asked by name > loaded from `.env` > ignored by Git |

Each folder has a `STEPS.md` (what to run, what to expect, what to say)
