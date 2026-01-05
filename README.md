

# Project 4: Advanced API (Integration Testing)

## The Challenge
This project connects to a PostgreSQL database. If you try to run `npm test` locally without a database, it will fail.

## Your Goal
Create a GitHub Actions workflow (`.github/workflows/integration.yml`) that:
1.  Checks out the code.
2.  Installs dependencies.
3.  **Spins up a PostgreSQL Service Container**.
4.  Runs the integration tests (`npm test`) successfully connecting to that container.

## Hints for the Workflow
- Look up "GitHub Actions Service Containers".
- You will need to define a `services:` section in your job.
- You must ensure the environment variable `DATABASE_URL` is set correctly for the `npm test` step (e.g., `postgres://user:password@localhost:5432/dbname`).
