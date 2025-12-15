from Employee import Employee
from package.Manager import Manager
from package.Technician import Technician

class TechManager(Manager, Technician):

        def __init__(self, name: str, id: str, department: str, specialization: str):
            Manager.__init__(self, name, id, department)
            Technician.__init__(self, name, id, specialization)
            self._team = []

def add_employee(self, employee: Employee) -> None:
        if not isinstance(employee, Employee):
            raise TypeError("Можно добавить только объект класса Employee")
        self._team.append(employee)
        print(f"Сотрудник {employee.name} (ID: {employee.id}) добавлен в команду")

    def get_team_info(self) -> str:
        if not self._team:
            return "В команде нет сотрудников"
        team_info: str = "\nИнформация о команде:\n"
        for emp in self._team:
            team_info += f"  {emp.get_info()}\n"
        return team_info

    def get_info(self) -> str:
        base_info = Manager.get_info(self)
        return f"{base_info}, Специализация: {self._specialization}"

    def perform_maintenance(self) -> str:
        result = Technician.perform_maintenance(self)
        return f"{result} (в рамках управления командой)"
