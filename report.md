# Lab 10 Jenkins Report

Christophe El Chabab

The `Python-CI-CD` job uses **Pipeline script from SCM**, the repository `https://github.com/chrs-005/Lab10-ChristopheElChabab.git`, branch `*/main`, and script path `Jenkinsfile_Christophe_ElChabab`.

Jenkins 2.580.2 runs locally in Docker with Python 3.13.5 and Bash as the shell executable. The suggested plugins and the required Git, Pipeline, and SSH Agent plugins are installed. Workspace Cleanup supplies the handout's `cleanWs()` step.

## Changes made

- The greeting includes my full name to match the required test: `Hello, World from Christophe El Chabab!`.
- `pytest` was added to the dependencies because the supplied pipeline calls it. The Test stage uses `python -m pytest` to resolve the `app` import error encountered with the standalone `pytest` command.
- The new Coverage stage runs `coverage run --source=app -m pytest` followed by `coverage report -m`.
- The new Security Scan stage runs `bandit app.py deploy.py`. Both tools are listed in `requirements.txt`.
- `deploy.py` copies `app.py` to `${WORKSPACE}@deployment`. The Deploy stage runs the copied application. This sibling directory remains after `cleanWs()` removes the build workspace.

## Jenkins results

Part 3 build **#2** passed Setup, Lint, Test, and Deploy. Part 4 build **#3**, using code commit `0a753917bc0ae8ff231f4e4a83ed0c15b37f4b43`, finished with **SUCCESS**.

| Stage | Result | Output |
| --- | --- | --- |
| Setup | SUCCESS | Created the virtual environment and installed the dependencies. |
| Lint | SUCCESS | `flake8 app.py` completed without errors. |
| Test | SUCCESS | One test passed in 0.02 seconds. |
| Coverage | SUCCESS | The test passed under coverage; `app.py` coverage was 75%. |
| Security Scan | SUCCESS | Bandit reported no issues; zero lines or issues were skipped. |
| Deploy | SUCCESS | Copied and ran the application, producing the required greeting. |

Coverage measured four statements, with only line 6 missing. That line prints the greeting when `app.py` is run directly; the supplied unit test calls `greet` through an import. The greeting function is covered.

Selected console output from build #3:

```text
============================== 1 passed in 0.02s ===============================

Name     Stmts   Miss  Cover   Missing
--------------------------------------
app.py       4      1    75%   6
--------------------------------------
TOTAL        4      1    75%

Test results:
    No issues identified.

Deployed app.py to /var/jenkins_home/workspace/Python-CI-CD@deployment
Hello, World from Christophe El Chabab!

[WS-CLEANUP] done
Finished: SUCCESS
```

The deployed `app.py` matches the repository file byte for byte. The local build and its complete console output are available at [Jenkins build #3](http://localhost:8080/job/Python-CI-CD/3/).
