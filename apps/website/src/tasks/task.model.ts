/**
 * Task model for GK and A Logistics Services Ltd
 */

export interface Task {
  id: number;
  title: string;
  description: string;
  status: 'pending' | 'in-progress' | 'completed' | 'cancelled';
  progress: number; // Progress percentage (0-100)
  createdAt: Date;
  updatedAt: Date;
  deadline?: Date;
  fileLinks?: string[];
  contacts?: string[];
  readme?: string;
  subtasks?: Subtask[];
}

export interface Subtask {
  id: number;
  title: string;
  description: string;
  status: 'pending' | 'in-progress' | 'completed';
  progress: number; // Progress percentage (0-100)
  createdAt: Date;
  updatedAt: Date;
}

export type TaskStatus = 'pending' | 'in-progress' | 'completed' | 'cancelled';
export type SubtaskStatus = 'pending' | 'in-progress' | 'completed';

export interface TaskDatabase {
  addTask(title: string, description?: string, options?: TaskOptions): number;
  updateTask(taskId: number, updates: Partial<TaskUpdates>): boolean;
  updateTaskStatus(taskId: number, status: TaskStatus): boolean;
  updateTaskProgress(taskId: number, progress: number): boolean;
  getAllTasks(): Task[];
  getTasksByStatus(status: TaskStatus): Task[];
  getPendingTasks(): Task[];
  getInProgressTasks(): Task[];
  getCompletedTasks(): Task[];
  deleteTask(taskId: number): boolean;
  getTask(taskId: number): Task | undefined;
  addSubtask(taskId: number, title: string, description?: string): boolean;
  updateSubtask(taskId: number, subtaskId: number, updates: Partial<SubtaskUpdates>): boolean;
  updateSubtaskStatus(taskId: number, subtaskId: number, status: SubtaskStatus): boolean;
  updateSubtaskProgress(taskId: number, subtaskId: number, progress: number): boolean;
}

export interface TaskOptions {
  deadline?: Date;
  fileLinks?: string[];
  contacts?: string[];
  readme?: string;
  progress?: number;
}

export interface TaskUpdates {
  title?: string;
  description?: string;
  status?: TaskStatus;
  progress?: number;
  deadline?: Date;
  fileLinks?: string[];
  contacts?: string[];
  readme?: string;
}

export interface SubtaskUpdates {
  title?: string;
  description?: string;
  status?: SubtaskStatus;
  progress?: number;
}