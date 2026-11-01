class Task:
    def __init__(self, title):
        self.title = title
    def show_title(self):
        return self.title
class UrgentTask(Task):
    def __init__(self, title, deadline):
        super().__init__(title)
        self.deadline = deadline
u = UrgentTask("a", "b")
print(u.show_title())
print(u.deadline)
