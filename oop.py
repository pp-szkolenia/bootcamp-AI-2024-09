class Task:
    def __init__(self, text, assignee=None, tags=[]):
        self.description = text
        self.assignee = assignee
        self.__tags = tags
        self._comments = []  # 'comments' attribute is protected

    def modify_description(self, new_description):
        self.description = new_description

    def add_comment(self, comment):
        self._comments.append(comment)


class TaskInheritance(Task):
    def __init__(self):
        super().__init__("text")

    def method(self):
        self._comments = []



task = Task("opis zadania")
print(task._comments)
print(task._Task__tags)

task_inherit = TaskInheritance()
print(task_inherit._Task__tags)
