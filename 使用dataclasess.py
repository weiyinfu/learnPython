from dataclasses import dataclass, asdict, astuple, replace


@dataclass()
class Point:
    x: int
    y: int


p = Point(3, 2)
pp = replace(p, y=10)
print(pp)
print(p)
