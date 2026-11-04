# One pipeline, five practices

A guided VS Code exercise for MLOps Engineering, Sessions 7-8. Improve one small customer-churn pipeline through error handling, code quality, configuration, logging and security

The data is synthetic. The model is a fixed rule: predict churn below 10 h of usage. Tracking is simulated and sends no network requests. Earlier checkpoints deliberately contain flawed code and a synthetic key that has never been valid

## Start here

Install VS Code with its Python extension, Miniconda and Git. Clone the repository or download and extract its ZIP file

1. Open this whole folder in VS Code
2. Right-click `work` in Explorer > **Open in Integrated Terminal**
3. On your first setup, create the environment:

```text
conda env create -f environment.yml
```

If `best-practices` already exists, reuse it. If its packages need updating, use `conda env update -f environment.yml`

4. Activate the environment:

```text
conda activate best-practices
```

5. Press `Ctrl+Shift+P` > **Python: Select Interpreter** > **best-practices**
6. Run the starting pipeline:

```text
python -m src.main
```

Expect accuracy `0.9090909090909091` and `quality gate met`. The other messages expose problems that the exercise will fix

## Use the folders

| Folder or file | Purpose |
| --- | --- |
| `work/` | Your editable project; run all lesson commands here |
| `checkpoints/00-start/` | Starting version and recovery copy |
| `checkpoints/01-error-handling/` | Reject bad inputs with clear errors |
| `checkpoints/02-code-quality/` | Format code and fix lint findings |
| `checkpoints/03-configuration/` | Read settings from `config.yaml` |
| `checkpoints/04-logging/` | Record progress and failures |
| `checkpoints/05-security/` | Load local values without exposing them |

Follow the instructor and edit only `work`. Checkpoints are complete reference versions for comparison and recovery. The final checkpoint includes all five practices

Local `.env` files and logs are excluded by `.gitignore`

## If stuck

Check three things first: save the file, keep the terminal in `work`, and select the `best-practices` interpreter

For one mistaken edit, use `Ctrl+Z` or compare your file with the matching checkpoint: right-click the work file > **Select for Compare**, then the checkpoint file > **Compare with Selected**

For full recovery, stop commands and close the terminal. Create `tmp` in the demo root, move `work` into it with a unique name such as `work-before-recovery-01`, then copy the required checkpoint into the demo root and rename the copy `work`. Reopen its terminal and activate `best-practices`. Use `00-start` to restart the exercise. Keep any existing Git repository at the demo root

The security exercise scans `work/src` specifically because earlier checkpoints intentionally retain the insecure example. A full-repository secret scan can therefore report those teaching examples

References: [VS Code source control](https://code.visualstudio.com/docs/sourcecontrol/overview), [adding local code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
