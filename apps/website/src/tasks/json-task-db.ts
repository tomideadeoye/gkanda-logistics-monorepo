/**
 * JSON-based Task Database Implementation for GK and A Logistics Services Ltd
 */
import * as fs from 'fs';
import * as path from 'path';
import { Task, TaskDatabase, TaskStatus, TaskOptions, TaskUpdates, Subtask, SubtaskStatus, SubtaskUpdates } from './task.model';

export class JsonTaskDatabase implements TaskDatabase {
  private dbPath: string;
  private tasks: Task[];

  constructor(dbPath: string = 'tasks.json') {
    this.dbPath = dbPath;
    this.tasks = this.loadTasks();
  }

  private loadTasks(): Task[] {
    try {
      if (fs.existsSync(this.dbPath)) {
        const data = fs.readFileSync(this.dbPath, 'utf8');
        const tasks = JSON.parse(data);
        // Convert date strings back to Date objects
        return tasks.map((task: any) => ({
          ...task,
          createdAt: new Date(task.createdAt),
          updatedAt: new Date(task.updatedAt),
          deadline: task.deadline ? new Date(task.deadline) : undefined,
          subtasks: task.subtasks ? task.subtasks.map((subtask: any) => ({
            ...subtask,
            createdAt: new Date(subtask.createdAt),
            updatedAt: new Date(subtask.updatedAt)
          })) : []
        }));
      }
    } catch (error) {
      console.error('Error loading tasks:', error);
    }
    return [];
  }

  private saveTasks(): void {
    try {
      fs.writeFileSync(this.dbPath, JSON.stringify(this.tasks, null, 2));
    } catch (error) {
      console.error('Error saving tasks:', error);
    }
  }

  addTask(title: string, description: string = '', options?: TaskOptions): number {
    const newId = this.tasks.length > 0 ? Math.max(...this.tasks.map(t => t.id)) + 1 : 1;
    const now = new Date();
    
    const newTask: Task = {
      id: newId,
      title,
      description,
      status: 'pending',
      progress: options?.progress || 0,
      createdAt: now,
      updatedAt: now,
      deadline: options?.deadline,
      fileLinks: options?.fileLinks || [],
      contacts: options?.contacts || [],
      readme: options?.readme,
      subtasks: []
    };

    this.tasks.push(newTask);
    this.saveTasks();
    return newId;
  }

  updateTask(taskId: number, updates: Partial<TaskUpdates>): boolean {
    const taskIndex = this.tasks.findIndex(task => task.id === taskId);
    if (taskIndex === -1) {
      return false;
    }

    // Update only the provided fields
    const updatedTask = {
      ...this.tasks[taskIndex],
      ...updates,
      updatedAt: new Date()
    };

    // Handle special cases for array fields
    if (updates.fileLinks !== undefined) {
      updatedTask.fileLinks = updates.fileLinks;
    }
    
    if (updates.contacts !== undefined) {
      updatedTask.contacts = updates.contacts;
    }

    // Ensure progress is between 0 and 100
    if (updates.progress !== undefined) {
      updatedTask.progress = Math.max(0, Math.min(100, updates.progress));
      
      // Auto-update status based on progress
      if (updatedTask.progress === 0) {
        updatedTask.status = 'pending';
      } else if (updatedTask.progress > 0 && updatedTask.progress < 100) {
        updatedTask.status = 'in-progress';
      } else if (updatedTask.progress === 100) {
        updatedTask.status = 'completed';
      }
    }

    this.tasks[taskIndex] = updatedTask;
    this.saveTasks();
    return true;
  }

  updateTaskStatus(taskId: number, status: TaskStatus): boolean {
    return this.updateTask(taskId, { status });
  }

  updateTaskProgress(taskId: number, progress: number): boolean {
    return this.updateTask(taskId, { progress });
  }

  getAllTasks(): Task[] {
    return [...this.tasks].sort((a, b) => b.createdAt.getTime() - a.createdAt.getTime());
  }

  getTasksByStatus(status: TaskStatus): Task[] {
    return this.getAllTasks().filter(task => task.status === status);
  }

  getPendingTasks(): Task[] {
    return this.getTasksByStatus('pending');
  }

  getInProgressTasks(): Task[] {
    return this.getTasksByStatus('in-progress');
  }

  getCompletedTasks(): Task[] {
    return this.getTasksByStatus('completed');
  }

  deleteTask(taskId: number): boolean {
    const initialLength = this.tasks.length;
    this.tasks = this.tasks.filter(task => task.id !== taskId);
    
    if (this.tasks.length < initialLength) {
      this.saveTasks();
      return true;
    }
    
    return false;
  }

  getTask(taskId: number): Task | undefined {
    return this.tasks.find(task => task.id === taskId);
  }

  addSubtask(taskId: number, title: string, description: string = ''): boolean {
    const task = this.tasks.find(task => task.id === taskId);
    if (!task) {
      return false;
    }

    const newSubtaskId = task.subtasks && task.subtasks.length > 0 
      ? Math.max(...task.subtasks.map(st => st.id)) + 1 
      : 1;
    
    const now = new Date();
    const newSubtask: Subtask = {
      id: newSubtaskId,
      title,
      description,
      status: 'pending',
      progress: 0,
      createdAt: now,
      updatedAt: now
    };

    if (!task.subtasks) {
      task.subtasks = [];
    }
    
    task.subtasks.push(newSubtask);
    task.updatedAt = now;
    this.saveTasks();
    return true;
  }

  updateSubtask(taskId: number, subtaskId: number, updates: Partial<SubtaskUpdates>): boolean {
    const task = this.tasks.find(task => task.id === taskId);
    if (!task || !task.subtasks) {
      return false;
    }

    const subtask = task.subtasks.find(st => st.id === subtaskId);
    if (!subtask) {
      return false;
    }

    // Update only the provided fields
    const updatedSubtask = {
      ...subtask,
      ...updates,
      updatedAt: new Date()
    };

    // Ensure progress is between 0 and 100
    if (updates.progress !== undefined) {
      updatedSubtask.progress = Math.max(0, Math.min(100, updates.progress));
      
      // Auto-update status based on progress
      if (updatedSubtask.progress === 0) {
        updatedSubtask.status = 'pending';
      } else if (updatedSubtask.progress > 0 && updatedSubtask.progress < 100) {
        updatedSubtask.status = 'in-progress';
      } else if (updatedSubtask.progress === 100) {
        updatedSubtask.status = 'completed';
      }
    }

    Object.assign(subtask, updatedSubtask);
    task.updatedAt = new Date();
    this.saveTasks();
    return true;
  }

  updateSubtaskStatus(taskId: number, subtaskId: number, status: SubtaskStatus): boolean {
    return this.updateSubtask(taskId, subtaskId, { status });
  }

  updateSubtaskProgress(taskId: number, subtaskId: number, progress: number): boolean {
    return this.updateSubtask(taskId, subtaskId, { progress });
  }
}