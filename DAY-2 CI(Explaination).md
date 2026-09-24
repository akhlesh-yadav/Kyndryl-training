DAY-2 CI(CONTINUOUS INTREGATION)

Continuous integration (CI) is the process of using automation to build and test software each time a developer commits changes to version control in a code base. CI helps teams discover issues early in the development process and fix them quickly. You can use GitHub Actions to implement CI for code that you maintain in a GitHub repository.

Suppose you want to set up a CI pipeline for your team of developers. The team is creating a website to improve the experience your customers have when they contact product support. Multiple features are under development. You want to make sure that the team can build and test all features easily so that each feature is quickly added to the website when it's ready. Because the code for the project is stored in a GitHub repository, you decide to use GitHub Actions for your CI project.



# Basic CI Workflow

This project demonstrates a basic **CI (Continuous Integration) workflow** using **GitHub Actions**.

## CI Workflow

```text
┌──────────────┐
│  Developer   │
│ writes code  │
└──────┬───────┘
       │
       │ git push
       ▼
┌──────────────┐
│    GitHub    │
│  Repository  │
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│  GitHub Actions  │
│   CI Workflow    │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│  Ubuntu Runner   │
│   Environment    │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Install → Test   │
│       → Build    │
└──────┬───────────┘
       │
       ▼
    ┌───────┐
    │ PASS? │
    └───┬───┘
        │
       Yes
        ▼
┌────────────────┐
│ CI Successful  │
└────────────────┘
```

## Workflow Steps

1. **Developer** writes or changes the code.
2. **Git push** sends the changes to GitHub.
3. **GitHub Actions** detects the push.
4. GitHub starts an **Ubuntu runner environment**.
5. The workflow **installs dependencies**.
6. The workflow **runs tests**.
7. The workflow **builds the application**.
8. If everything passes, the **CI workflow succeeds**.

## Workflow File

The CI workflow is defined in:

```text
.github/workflows/ci.yml
```

Example:

```yaml
name: Basic CI

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install dependencies
        run: npm install

      - name: Run tests
        run: npm test

      - name: Build
        run: npm run build
```

## Purpose

The purpose of this CI workflow is to **automatically verify the code whenever changes are pushed to the `main` branch**.

```text
Code → Push → CI → Test → Build → Success
```
