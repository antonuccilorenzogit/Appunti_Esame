from dataclasses import dataclass


@dataclass
class State:
    id: str
    name: str
    lat: float
    lng: float

    def __hash__(self):
        return hash(self.id)
    def __eq__(self, other):
        return self.id == other.id
    def __repr__(self):
        return f'<State id={self.id} name={self.name}>'