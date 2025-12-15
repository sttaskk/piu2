from Employee import Employee

class Technician(Employee):
    class Technician(Employee):
        def __init__(self, name: str, id: str, specialization: str):
            Employee.__init__(self, name, id)  # Явно вызываем родителя
            self._specialization = specialization

    @property
    def specialization(self):
        return self._specialization

    def perform_maintenance(self) -> str:
        return (f"{self._name} выполняет техническое обслуживание "
                f"по специализации '{self._specialization}'")

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Специализация: {self._specialization}"
