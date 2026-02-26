from dataclasses import dataclass

@dataclass
class Customer:
    """Used to store customer details. Each customer has a name, surname, and postcode"""
    name: str
    surname: str
    postcode: str

    def full_name(self) -> str:
        """Returns customer's full name as string"""
        return f"{self.name} {self.surname}"

    def as_list(self) -> list:
        """Returns customer's data as list"""
        return [self.name, self.surname, self.postcode]