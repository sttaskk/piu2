class Employee:

    def __init__(self, name: str, id: str):
        self._name = name
        self._id = id

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    def get_info(self) -> str:

        return f"Имя: {self._name}, ID: {self._id}"


