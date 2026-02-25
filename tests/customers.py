from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    surname: str
    postcode: str

    def full_name(self) -> str:
        return f"{self.name} {self.surname}"

    def as_list(self) -> list:
        return [self.name, self.surname, self.postcode]