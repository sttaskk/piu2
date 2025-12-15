from Employee import Employee


class Manager(Employee):
    def __init__(self, name: str, id: str, department: str):
        Employee.__init__(self, name, id)
        self._department = department
        self._managed_projects = []

@property

def department(self):
    return self._department

def manage_project(self, project_name: str) -> str:
    self._managed_projects.append(project_name)
    return (f"{self._name} начал управлять проектом "
            f"'{project_name}' в отделе {self._department}")

def get_info(self) -> str:
    base_info = super().get_info()
    return f"{base_info}, Отдел: {self._department}"
