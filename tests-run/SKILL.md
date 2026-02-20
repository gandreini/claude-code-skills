---
name: tests-run
description: Detect and run all available tests
allowed-tools: Bash(cat:*), Bash(ls:*), Bash(test:*), Bash(python:*), Bash(pytest:*), Bash(npm:*), Bash(yarn:*), Bash(pnpm:*), Bash(npx:*), Bash(cargo:*), Bash(go:*), Bash(make:*)
---

# Context
- Package.json exists: !`test -f package.json && echo "yes" || echo "no"`
- Package.json scripts: !`test -f package.json && cat package.json | grep -A 30 '"scripts"' || echo "n/a"`
- Cypress installed: !`test -d node_modules/cypress || test -f cypress.config.js || test -f cypress.config.ts && echo "yes" || echo "no"`
- Cypress folder: !`test -d cypress && echo "yes" || echo "no"`
- Pyproject.toml exists: !`test -f pyproject.toml && echo "yes" || echo "no"`
- Pytest available: !`test -d tests || test -d test || ls *_test.py test_*.py 2>/dev/null && echo "yes" || echo "no"`
- Cargo.toml exists: !`test -f Cargo.toml && echo "yes" || echo "no"`
- Go.mod exists: !`test -f go.mod && echo "yes" || echo "no"`
- Makefile test target: !`test -f Makefile && grep -E "^test:" Makefile && echo "yes" || echo "no"`

# Task
Based on the context above, detect which test framework(s) are available and run the tests.

Priority order:
1. `Makefile` with test target → `make test`
2. `package.json` with test script → `npm test`
3. Cypress detected → `npx cypress run` (or use script like `cy:run`, `e2e`, `cypress:run` if present)
4. `pyproject.toml` or pytest files → `pytest`
5. `Cargo.toml` → `cargo test`
6. `go.mod` → `go test ./...`

If multiple test types exist (e.g., unit tests AND Cypress e2e), run both and report results separately.

If no tests are detected, say so clearly and suggest how to set them up for this project type.

Run the appropriate test command(s) and report the results.
