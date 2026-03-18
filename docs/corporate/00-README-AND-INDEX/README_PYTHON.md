# gkalogistics Python Project with ReportLab

This project demonstrates how to set up a Python environment with ReportLab for generating PDFs.

## Prerequisites

- Python 3.8 or higher
- UV package manager (https://github.com/astral-sh/uv)

## Setup

1. Run the setup script (recommended):
   ```bash
   ./setup.sh
   ```

   Or manually install dependencies using UV:
   ```bash
   uv venv
   source .venv/bin/activate && uv pip install -r requirements.txt
   ```

   Or install ReportLab directly:
   ```bash
   uv venv
   source .venv/bin/activate && uv pip install reportlab
   ```

2. Run the demo script:
   ```bash
   python reportlab_demo.py
   ```

This will create a sample PDF file in the current directory.

## Task Management (TypeScript/Node.js Version)

This project includes a TypeScript/Node.js implementation of the task management system with enhanced features:

- Track pending, in-progress, completed, and cancelled tasks
- Progress percentage tracking for tasks and subtasks
- Task deadlines
- File links association
- Contact information
- Task README documentation
- Subtasks/steps tracking
- Command-line interface for managing tasks
- JSON-based storage for persistence

### Usage

```bash
# Build the TypeScript files
npm run tasks:build

# Add a new task with progress
npm run tasks add "Task Title" "Task Description" --progress 0

# Add a new task with deadline and file links
npm run tasks add "Site plan submission" "Prepare and submit site plan" --deadline "2025-10-15" --file "site-plan.pdf,docs/requirements.txt" --contact "john@example.com,jane@company.com"

# Add a new task with README
npm run tasks add "Review drawings" "Check technical drawings for accuracy" --readme "This task requires approval from the planning department"

# List all tasks
npm run tasks list

# List pending tasks
npm run tasks pending

# List in-progress tasks
npm run tasks in-progress

# List completed tasks
npm run tasks completed

# Update task fields (title, description, status, progress, deadline, readme)
npm run tasks update TASK_ID FIELD VALUE

# Update task progress
npm run tasks update TASK_ID progress 50

# Add a subtask to a task
npm run tasks add-subtask TASK_ID "Subtask Title" "Subtask Description"

# Update subtask fields (title, description, status, progress)
npm run tasks update-subtask TASK_ID SUBTASK_ID FIELD VALUE

# Update subtask progress
npm run tasks update-subtask TASK_ID SUBTASK_ID progress 75

# Delete a task
npm run tasks delete TASK_ID

# Show help
npm run tasks help
```

## Project Structure

- `main.py`: Main entry point
- `reportlab_demo.py`: Example usage of ReportLab
- `src/tasks/`: TypeScript/Node.js task management implementation
- `requirements.txt`: Dependencies list
- `pyproject.toml`: Project configuration

## ReportLab Resources

- Official Documentation: https://www.reportlab.com/docs/reportlab-userguide.pdf