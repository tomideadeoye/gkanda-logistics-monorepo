# GK and A Logistics Services Ltd Task Management (TypeScript)

This directory contains the TypeScript implementation of the task management system for GK and A Logistics Services Ltd.

## Features

- Track general tasks with status (pending, in-progress, completed, cancelled)
- Progress percentage tracking for tasks and subtasks
- JSON-based storage for persistence
- Command-line interface for managing tasks
- TypeScript type safety
- Task deadlines
- File links association
- Contact information
- Task README documentation
- Subtasks/steps tracking

## Usage

```bash
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

## Architecture

- [task.model.ts](task.model.ts) - TypeScript interfaces and types
- [json-task-db.ts](json-task-db.ts) - JSON-based implementation of the task database
- [cli.ts](cli.ts) - Command-line interface

## Data Storage

Tasks are stored in a JSON file (`tasks.json`) in the root directory of the project.

## Task Structure

Each task contains the following information:
- ID: Unique identifier
- Title: Task title
- Description: Detailed task description
- Status: Current status (pending, in-progress, completed, cancelled)
- Progress: Completion percentage (0-100)
- Created/Updated timestamps
- Deadline (optional): Due date for the task
- File Links (optional): Relevant file paths or URLs
- Contacts (optional): Relevant contact information
- README (optional): Task documentation
- Subtasks (optional): Steps or subtasks associated with the main task

Each subtask contains:
- ID: Unique identifier
- Title: Subtask title
- Description: Detailed subtask description
- Status: Current status (pending, in-progress, completed)
- Progress: Completion percentage (0-100)
- Created/Updated timestamps