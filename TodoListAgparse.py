import argparse
import pickle
import time
import sys
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class TaskEntry:
    def __init__(self, task_id, task, status="TODO", timer_end_time=None, priority="undefined", due_date=None, timestamp=None):
        self.task_id = task_id
        self.task = task
        self.status = status
        self.timer_end_time = timer_end_time
        self.priority = priority
        self.due_date = due_date
        self.timestamp = timestamp if timestamp else int(datetime.now().timestamp())

    def to_dict(self):
        return {
            "id": self.task_id,
            "task": self.task,
            "status": self.status,
            "timer_end_time": self.timer_end_time,
            "priority": self.priority,
            "due_date": self.due_date,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dict(data):
        return TaskEntry(
            task_id=data["id"],
            task=data["task"],
            status=data.get("status", "TODO"),
            timer_end_time=data.get("timer_end_time"),
            priority=data.get("priority"),
            due_date=data.get("due_date"),
            timestamp=data.get("timestamp", int(datetime.now().timestamp()))
        )

    def set_timer(self, duration_seconds):
        self.timer_end_time = int((datetime.now() + timedelta(seconds=duration_seconds)).timestamp())

    def get_remaining_time(self):
        if self.timer_end_time:
            remaining_time = self.timer_end_time - int(datetime.now().timestamp())
            return max(remaining_time, 0)
        return None


class TaskDb:
    def __init__(self, filename='tasks.pkl'):
        self.filename = filename

    def load_tasks(self):
        try:
            with open(self.filename, 'rb') as file:
                tasks_data = pickle.load(file)
                return [TaskEntry.from_dict(task) for task in tasks_data]
        except FileNotFoundError:
            return []

    def save_tasks(self, tasks):
        with open(self.filename, 'rb') as file:
            pickle.dump([task.to_dict() for task in tasks], file)


class TaskManager:
    def __init__(self):
        self.task_db = TaskDb()
        self.todo_list = self.task_db.load_tasks()
        self.task_id_counter = max((task.task_id for task in self.todo_list), default=0) + 1

    def get_task_by_id(self, task_id):
        for task in self.todo_list:
            if task.task_id == task_id:
                return task
        return None

    def add_task(self, task_description, priority="undefined", due_date=None):
        task = TaskEntry(self.task_id_counter, task_description, priority=priority, due_date=due_date)
        self.todo_list.append(task)
        print(f"Added: {task_description} - Priority: {priority} - Due Date: {due_date} - Task <ID>: {self.task_id_counter}")
        self.task_id_counter += 1

    def modify_task(self, task_id, new_description):
        task = self.get_task_by_id(task_id)
        if task:
            task.task = new_description
            print(f"Modified task with ID {task_id}. New text: {new_description}")
        else:
            print(f"No task found with ID {task_id}")

    def list_tasks(self):
        if not self.todo_list:
            print("No tasks in the todo list.")
        else:
            for task in self.todo_list:
                print(f"ID: {task.task_id}, Task: {task.task}, Priority: {task.priority}")

    def show_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            current_time = int(datetime.now().timestamp())
            elapsed_time = current_time - task.timestamp
            minutes, seconds = divmod(elapsed_time, 60)
            remaining_time = task.get_remaining_time()
            timer_str = f", Timer: {remaining_time // 60} minutes and {remaining_time % 60} seconds remaining" if remaining_time is not None else ""
            print(f"Task ID: {task.task_id} - Task: {task.task} - Status: {task.status} - Priority: {task.priority} - Time Passed: {minutes} minutes and {seconds} seconds{timer_str}")
        else:
            print(f"No task found with ID {task_id}")

    def mark_done(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.status = "DONE"
            print(f'Marking the task with ID {task_id} as done.')
        else:
            print('No task found with this ID')

    def mark_halfdone(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.status = "HALF DONE"
            print(f'Marking the task with ID {task_id} as half done.')
        else:
            print('No task found with this ID')

    def time_passed(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task_time = datetime.fromtimestamp(task.timestamp)
            current_time = datetime.now()
            delta = relativedelta(current_time, task_time)   #relativedelta provides a way to calculate the difference between two datetime objects in terms of years, months, days, hours, minutes, and seconds.

            print(f"The time that has passed since you added the task '{task.task}' is "
                  f"{delta.years} years, {delta.months} months, {delta.days} days, "
                  f"{delta.hours} hours, {delta.minutes} minutes, and {delta.seconds} seconds.")
        else:
            print(f"No task found with ID {task_id}")

    def priority(self, task_id, new_priority):
        task = self.get_task_by_id(task_id)
        if task:
            task.priority = new_priority
            print(f'Changing the priority of the task with ID {task_id} to {new_priority}.')
        else:
            print('No task found with this ID')

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.todo_list.remove(task)
            print(f"Deleted task with ID {task_id}.")
        else:
            print(f"No task found with ID {task_id}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-add', nargs='+', type=str, help='Add task to the todo list')
    parser.add_argument('-priority', type=str, help='Priority of the task', default='low')
    parser.add_argument('-due_date', type=str, help='Due date of the task')
    parser.add_argument('-modify', nargs='+', type=str, metavar=('ID', 'new_text'), help='Modify an existing task. Enter task ID and the new text.')
    parser.add_argument('-list', action='store_true', help='Show the whole todo list')
    parser.add_argument('-show', type=int, metavar='ID', help='Show a single task by ID')
    parser.add_argument('-done', type=int, help='Mark task as done')
    parser.add_argument('-halfdone', type=int, help='Mark the task as half done')
    parser.add_argument('-timepassed', type=int, help='Check how much time has passed since you added the task')
    parser.add_argument('-set_priority', nargs=2, type=str, help='Specify the priority of the task')
    parser.add_argument('-delete', type=int, help='delete a task')

    args = parser.parse_args()

    task_manager = TaskManager()
    if args.add:
        task_description = ' '.join(args.add)
        task_manager.add_task(task_description, priority=args.priority, due_date=args.due_date)
    elif args.modify and len(args.modify) >= 2:
        task_id = int(args.modify[0])
        new_description = ' '.join(args.modify[1:])
        task_manager.modify_task(task_id, new_description)
    elif args.delete:
        task_manager.delete_task(args.delete)
    elif args.list:
        task_manager.list_tasks()
    elif args.show is not None:
        task_manager.show_task(args.show)
    elif args.done is not None:
        task_manager.mark_done(args.done)
    elif args.halfdone is not None:
        task_manager.mark_halfdone(args.halfdone)
    elif args.timepassed is not None:
        task_manager.time_passed(args.timepassed)
    elif args.set_priority and len(args.set_priority) == 2:
        task_id = int(args.set_priority[0])
        priority = args.set_priority[1]
        task_manager.priority(task_id, priority)
    else:
        print("Usage: -add [task] -priority [priority] -due_date [due_date] -modify [ID new_text] -list -show [ID] -done [ID] -halfdone [ID] -set_timer [ID seconds] -timepassed [ID] -set_priority [ID priority]")
        sys.exit(1)

    task_manager.task_db.save_tasks(task_manager.todo_list)
    sys.exit(0)


if __name__ == "__main__":
    main()
