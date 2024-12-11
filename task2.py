
class Project:
    def __init__(self, name, description, tasks=None):
        self.name = name
        self.description = description
        self.tasks = tasks if tasks is not None else []

    def add_task(self, title, description, status):
        task = {"title": title, "description": description, "status": status}
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task["title"] != title]

    def get_task_status(self, title):
        for task in self.tasks:
            if task["title"] == title:
                return task["status"]
        return "there's no such task"

    def update_task_status(self, title, new_status):
        for task in self.tasks:
            if task["title"] == title:
                task["status"] = new_status
                return "the task status has been successfully updated"
        return "there's no such task"

    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task["status"] == status]

    def print_tasks(self):
        for task in self.tasks:
            print(f"Title: {task['title']}, Description: {task['description']}, Status: {task['status']}")


project = Project("Website Redesign", "A project for redesigning the company website")
project.add_task("Design Layout", "Create a layout for the new website", "Planned")
project.add_task("Develop Homepage", "Develop the homepage of the website", "In Progress")
project.add_task("Refactor", "Make it work", "Planned")
project.update_task_status("Design Layout", "Completed")
project.print_tasks()
planned_tasks = project.get_tasks_by_status("Planned")
print(planned_tasks)

