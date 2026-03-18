#!/usr/bin/env node
/**
 * Command Line Interface for GK and A Logistics Services Ltd Task Database (TypeScript Version)
 */
import { JsonTaskDatabase } from './json-task-db';
import { TaskStatus, SubtaskStatus } from './task.model';

function printHelp(): void {
  console.log(`
GK and A Logistics Services Ltd Task Manager (TypeScript Version)
Usage: npm run tasks [command] [arguments]

Commands:
  add "title" "description" [options]          Add a new task
    Options:
      --deadline "YYYY-MM-DD"                   Set task deadline
      --file "file1,file2"                      Add file links
      --contact "contact1,contact2"             Add contacts
      --readme "readme content"                 Add task README
      --progress NUMBER                         Set initial progress (0-100)
  list                                         List all tasks
  pending                                      List pending tasks
  in-progress                                  List in-progress tasks
  completed                                    List completed tasks
  update ID field value                        Update a specific field of a task
    Fields: title, description, status, progress, deadline, readme
  delete ID                                    Delete a task
  add-subtask ID "title" "description"         Add a subtask to a task
  update-subtask ID SUBTASK_ID field value     Update a specific field of a subtask
    Fields: title, description, status, progress
  help                                         Show this help message

Examples:
  npm run tasks add "Review drawings" "Check technical drawings for accuracy" --deadline "2025-10-15" --progress 0
  npm run tasks add "Site plan submission" "Prepare and submit site plan" --file "site-plan.pdf,docs/requirements.txt" --contact "john@example.com,jane@company.com"
  npm run tasks list
  npm run tasks update 1 status in-progress
  npm run tasks update 1 progress 50
  npm run tasks update 1 readme "This task requires approval from the planning department"
  npm run tasks add-subtask 1 "Check dimensions" "Verify all dimensions in the drawings"
  npm run tasks update-subtask 1 1 progress 100
  npm run tasks delete 2
`);
}

function printTasks(tasks: any[], title: string): void {
  console.log(`\n${title}:`);
  console.log('-'.repeat(100));
  
  if (tasks.length === 0) {
    console.log('No tasks found.');
  } else {
    tasks.forEach(task => {
      console.log(`ID: ${task.id}`);
      console.log(`Title: ${task.title}`);
      console.log(`Description: ${task.description}`);
      console.log(`Status: ${task.status}`);
      console.log(`Progress: ${task.progress !== undefined ? task.progress : 0}%`);
      if (task.deadline) {
        console.log(`Deadline: ${task.deadline}`);
      }
      if (task.fileLinks && task.fileLinks.length > 0) {
        console.log(`File Links: ${task.fileLinks.join(', ')}`);
      }
      if (task.contacts && task.contacts.length > 0) {
        console.log(`Contacts: ${task.contacts.join(', ')}`);
      }
      if (task.readme) {
        console.log(`README: ${task.readme}`);
      }
      if (task.subtasks && task.subtasks.length > 0) {
        console.log(`Subtasks:`);
        task.subtasks.forEach((subtask: any) => {
          console.log(`  ${subtask.id}. ${subtask.title} [${subtask.status}] ${subtask.progress !== undefined ? subtask.progress : 0}%`);
          if (subtask.description) {
            console.log(`     ${subtask.description}`);
          }
        });
      }
      console.log(`Created: ${task.createdAt}`);
      console.log(`Updated: ${task.updatedAt}`);
      console.log('-'.repeat(100));
    });
  }
}

function parseOptions(args: string[]): { options: any; remainingArgs: string[] } {
  const options: any = {};
  const remainingArgs: string[] = [];
  
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--deadline' && i + 1 < args.length) {
      const dateStr = args[i + 1];
      const date = new Date(dateStr);
      if (!isNaN(date.getTime())) {
        options.deadline = date;
      } else {
        console.log(`Warning: Invalid date format "${dateStr}". Expected YYYY-MM-DD.`);
      }
      i++; // Skip the next argument
    } else if (args[i] === '--file' && i + 1 < args.length) {
      options.fileLinks = args[i + 1].split(',').map(f => f.trim()).filter(f => f.length > 0);
      i++; // Skip the next argument
    } else if (args[i] === '--contact' && i + 1 < args.length) {
      options.contacts = args[i + 1].split(',').map(c => c.trim()).filter(c => c.length > 0);
      i++; // Skip the next argument
    } else if (args[i] === '--readme' && i + 1 < args.length) {
      options.readme = args[i + 1];
      i++; // Skip the next argument
    } else if (args[i] === '--progress' && i + 1 < args.length) {
      const progress = parseInt(args[i + 1]);
      if (!isNaN(progress)) {
        options.progress = Math.max(0, Math.min(100, progress));
      } else {
        console.log(`Warning: Invalid progress value "${args[i + 1]}". Expected a number between 0 and 100.`);
      }
      i++; // Skip the next argument
    } else {
      remainingArgs.push(args[i]);
    }
  }
  
  return { options, remainingArgs };
}

function main(): void {
  const args = process.argv.slice(2);
  
  if (args.length < 1) {
    printHelp();
    return;
  }

  const db = new JsonTaskDatabase('./tasks.json');
  const command = args[0].toLowerCase();

  switch (command) {
    case 'help':
      printHelp();
      break;
    
    case 'add':
      if (args.length < 2) {
        console.log('Error: Title is required for add command');
        console.log('Usage: npm run tasks add "title" ["description"] [options]');
        return;
      }
      
      const { options, remainingArgs } = parseOptions(args.slice(1));
      const title = remainingArgs[0] || '';
      const description = remainingArgs[1] || '';
      
      const taskId = db.addTask(title, description, options);
      console.log(`Task added with ID: ${taskId}`);
      break;
    
    case 'list':
      const allTasks = db.getAllTasks();
      printTasks(allTasks, 'All Tasks');
      break;
    
    case 'pending':
      const pendingTasks = db.getPendingTasks();
      printTasks(pendingTasks, 'Pending Tasks');
      break;
    
    case 'in-progress':
      const inProgressTasks = db.getInProgressTasks();
      printTasks(inProgressTasks, 'In-Progress Tasks');
      break;
    
    case 'completed':
      const completedTasks = db.getCompletedTasks();
      printTasks(completedTasks, 'Completed Tasks');
      break;
    
    case 'update':
      if (args.length < 4) {
        console.log('Error: Task ID, field, and value are required for update command');
        console.log('Usage: npm run tasks update ID field value');
        return;
      }
      
      const taskIdToUpdate = parseInt(args[1]);
      if (isNaN(taskIdToUpdate)) {
        console.log('Error: Task ID must be a number');
        return;
      }
      
      const field = args[2];
      const value = args[3];
      
      const updates: any = {};
      if (field === 'title') {
        updates.title = value;
      } else if (field === 'description') {
        updates.description = value;
      } else if (field === 'status') {
        if (!['pending', 'in-progress', 'completed', 'cancelled'].includes(value)) {
          console.log('Error: Status must be pending, in-progress, completed, or cancelled');
          return;
        }
        updates.status = value as TaskStatus;
      } else if (field === 'progress') {
        const progress = parseInt(value);
        if (isNaN(progress)) {
          console.log('Error: Progress must be a number');
          return;
        }
        updates.progress = Math.max(0, Math.min(100, progress));
      } else if (field === 'deadline') {
        const date = new Date(value);
        if (!isNaN(date.getTime())) {
          updates.deadline = date;
        } else {
          console.log(`Error: Invalid date format "${value}". Expected YYYY-MM-DD.`);
          return;
        }
      } else if (field === 'readme') {
        updates.readme = value;
      } else {
        console.log(`Error: Field "${field}" is not supported for update.`);
        return;
      }
      
      if (db.updateTask(taskIdToUpdate, updates)) {
        console.log(`Task ${taskIdToUpdate} ${field} updated`);
      } else {
        console.log(`Error: Task ${taskIdToUpdate} not found`);
      }
      break;
    
    case 'delete':
      if (args.length < 2) {
        console.log('Error: Task ID is required for delete command');
        console.log('Usage: npm run tasks delete ID');
        return;
      }
      
      const taskIdToDelete = parseInt(args[1]);
      if (isNaN(taskIdToDelete)) {
        console.log('Error: Task ID must be a number');
        return;
      }
      
      if (db.deleteTask(taskIdToDelete)) {
        console.log(`Task ${taskIdToDelete} deleted`);
      } else {
        console.log(`Error: Task ${taskIdToDelete} not found`);
      }
      break;
    
    case 'add-subtask':
      if (args.length < 3) {
        console.log('Error: Task ID, subtask title are required for add-subtask command');
        console.log('Usage: npm run tasks add-subtask ID "title" ["description"]');
        return;
      }
      
      const taskIdForSubtask = parseInt(args[1]);
      if (isNaN(taskIdForSubtask)) {
        console.log('Error: Task ID must be a number');
        return;
      }
      
      const subtaskTitle = args[2];
      const subtaskDescription = args[3] || '';
      
      if (db.addSubtask(taskIdForSubtask, subtaskTitle, subtaskDescription)) {
        console.log(`Subtask added to task ${taskIdForSubtask}`);
      } else {
        console.log(`Error: Task ${taskIdForSubtask} not found`);
      }
      break;
    
    case 'update-subtask':
      if (args.length < 5) {
        console.log('Error: Task ID, subtask ID, field, and value are required for update-subtask command');
        console.log('Usage: npm run tasks update-subtask ID SUBTASK_ID field value');
        return;
      }
      
      const taskIdForSubtaskUpdate = parseInt(args[1]);
      const subtaskIdToUpdate = parseInt(args[2]);
      const subtaskField = args[3];
      const subtaskValue = args[4];
      
      if (isNaN(taskIdForSubtaskUpdate) || isNaN(subtaskIdToUpdate)) {
        console.log('Error: Task ID and subtask ID must be numbers');
        return;
      }
      
      const subtaskUpdates: any = {};
      if (subtaskField === 'title') {
        subtaskUpdates.title = subtaskValue;
      } else if (subtaskField === 'description') {
        subtaskUpdates.description = subtaskValue;
      } else if (subtaskField === 'status') {
        if (!['pending', 'in-progress', 'completed'].includes(subtaskValue)) {
          console.log('Error: Subtask status must be pending, in-progress, or completed');
          return;
        }
        subtaskUpdates.status = subtaskValue as SubtaskStatus;
      } else if (subtaskField === 'progress') {
        const progress = parseInt(subtaskValue);
        if (isNaN(progress)) {
          console.log('Error: Progress must be a number');
          return;
        }
        subtaskUpdates.progress = Math.max(0, Math.min(100, progress));
      } else {
        console.log(`Error: Field "${subtaskField}" is not supported for subtask update.`);
        return;
      }
      
      if (db.updateSubtask(taskIdForSubtaskUpdate, subtaskIdToUpdate, subtaskUpdates)) {
        console.log(`Subtask ${subtaskIdToUpdate} of task ${taskIdForSubtaskUpdate} ${subtaskField} updated`);
      } else {
        console.log(`Error: Task ${taskIdForSubtaskUpdate} or subtask ${subtaskIdToUpdate} not found`);
      }
      break;
    
    default:
      console.log(`Error: Unknown command '${command}'`);
      printHelp();
  }
}

main();