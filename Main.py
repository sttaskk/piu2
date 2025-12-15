from Employee import Employee
from package.Manager import Manager
from package.TechManager import TechManager
from package.Technician import Technician

def create_employee():

    name = input("Введите имя сотрудника: ").strip()
    id = input("Введите ID сотрудника: ").strip()
    return Employee(name, id)

def create_manager():
    name = input("Введите имя менеджера: ").strip()
    id = input("Введите ID менеджера: ").strip()
    department = input("Введите отдел менеджера: ").strip()
    return Manager(name, id, department)

def create_technician():
    name = input("Введите имя техника: ").strip()
    id = input("Введите ID техника: ").strip()
    specialization = input("Введите специализацию техника: ").strip()
    return Technician(name, id, specialization)

def create_tech_manager():
    name = input("Введите имя технического менеджера: ").strip()
    id = input("Введите ID технического менеджера: ").strip()
    department = input("Введите отдел технического менеджера: ").strip()
    specialization = input("Введите специализацию технического менеджера: ").strip()
    return TechManager(name, id, department, specialization)

def main():
    print(" Система управления сотрудниками \n")
    employees = {}
    tech_managers = {}

    while True:
        print("\nДоступные команды:")
        print("  1 — Создать сотрудника (Employee)")
        print("  2 — Создать менеджера (Manager)")
        print("  3 — Создать техника (Technician)")
        print("  4 — Создать технического менеджера (TechManager)")
        print("  5 — Добавить сотрудника в команду TechManager")
        print("  6 — Посмотреть информацию о TechManager и его команде")
        print("  7 — Вывести список всех созданных объектов")
        print("  0 — Выход")

        choice = input("\nВыберите команду (0–7): ").strip()

        if choice == "0":
            print("Завершение работы системы.")
            break

        elif choice == "1":
            emp = create_employee()
            employees[emp.id] = emp
            print(f"\nСоздан сотрудник: {emp.get_info()}")

        elif choice == "2":
            mgr = create_manager()
            employees[mgr.id] = mgr
            print(f"\nСоздан менеджер: {mgr.get_info()}")

        elif choice == "3":
            tech = create_technician()
            employees[tech.id] = tech
            print(f"\nСоздан техник: {tech.get_info()}")

        elif choice == "4":
            tm = create_tech_manager()
            tech_managers[tm.id] = tm
            employees[tm.id] = tm
            print(f"\nСоздан технический менеджер: {tm.get_info()}")

        elif choice == "5":
            if not tech_managers:
                print("Нет созданных технических менеджеров!")
                continue

            tm_id = input("Введите ID технического менеджера: ").strip()
            tm = tech_managers.get(tm_id)
            if not tm:
                print("Технический менеджер с таким ID не найден!")
                continue

            emp_id = input("Введите ID сотрудника для добавления в команду: ").strip()
            emp = employees.get(emp_id)
            if not emp:
                print("Сотрудник с таким ID не найден!")
                continue

            tm.add_employee(emp)

        elif choice == "6":
            if not tech_managers:
                print("Нет созданных технических менеджеров!")
                continue

            tm_id = input("Введите ID технического менеджера: ").strip()
            tm = tech_managers.get(tm_id)
            if not tm:
                print("Технический менеджер с таким ID не найден!")
                continue

            print(f"\nИнформация о техническом менеджере:")
            print(tm.get_info())
            print(tm.get_team_info())

        elif choice == "7":
            if not employees:
                print("Пока не создано ни одного сотрудника.")
            else:
                print("\nСписок всех созданных объектов:")
                for emp in employees.values():
                    print(f"  {type(emp).__name__}: {emp.get_info()}")

        else:
            print("Неверная команда! Введите число от 0 до 7.")


if __name__ == "__main__":
    main()
