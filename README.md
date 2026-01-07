# Project 7: Taskmaster API (Intermediate CI/CD)

## 🎯 The Mission
You are building a Task Management API using **FastAPI** and **PostgreSQL**.
Your goal is to create a robust CI pipeline that tests the application against a *real* database and publishes a Docker image.

## 📂 Project Structure
- `app/main.py`: The FastAPI application source code.
- `app/test_main.py`: Integration tests that require a database connection.
- `Dockerfile`: Instructions to containerize the app.

## ⚔️ The Challenge Requirements

### 1. Matrix Testing Strategy
- **Objective:** Ensure compatibility.
- **Task:** Configure the workflow to run tests in parallel across **Python 3.10** and **Python 3.11**.

### 2. Service Containers (The Critical Part)
- **Objective:** Test with real infrastructure, not mocks.
- **Task:**
    - The tests fail without a database.
    - Configure a **PostgreSQL service container** inside your GitHub Actions workflow.
    - Ensure the database is healthy (`health-cmd`) before running tests.
    - *Hint: Map port 5432 and set POSTGRES_PASSWORD.*

### 3. Dependency Caching
- **Objective:** Speed up the build.
- **Task:** Use `actions/cache` (or the built-in setup-python caching) to cache `pip` dependencies so they aren't downloaded on every run.

### 4. Build & Push to Registry
- **Objective:** Deliver the artifact.
- **Task:**
    - If the tests pass on the `main` branch:
    - Login to **GitHub Container Registry (GHCR)**.
    - Build the Docker image.
    - Push it as `ghcr.io/<your-username>/taskmaster-api:latest`.

### 5. Artifacts
- **Objective:** Debugging data.
- **Task:** Generate a coverage report (using `pytest-cov`) and upload it as a workflow artifact.

---

## 🛠 Useful Commands
- Run tests locally: `pytest`
- Run app: `uvicorn app.main:app --reload`
