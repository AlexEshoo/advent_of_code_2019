from collections import defaultdict, namedtuple, Counter
from dataclasses import dataclass


@dataclass
class Cursor:
    x: int = 0
    y: int = 0

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

    def right(self):
        self.x += 1

    def left(self):
        self.x -= 1

    @property
    def coordinates(self):
        return (self.x, self.y)


Point = namedtuple("Point", ['x', 'y'])


def one_norm(v1, v2):
    return sum(abs(p2 - p1) for p1, p2 in zip(v1, v2))


def trace_wire(wire, grid, start=Point(0, 0), wire_number=0):
    cursor = Cursor(**start._asdict())
    move = {'U': cursor.up, 'D': cursor.down, 'L': cursor.left, 'R': cursor.right}
    for direction, distance in [(s[0], int(s[1:])) for s in wire]:
        for n in range(distance):
            move[direction]()
            grid[(cursor.x, cursor.y)].add(wire_number)


circuit_cabinet = defaultdict(set)

origin = Point(x=0, y=0)

with open("input/input_day03.txt") as f:
    wire1 = f.readline().split(',')
    wire2 = f.readline().split(',')

trace_wire(wire1, circuit_cabinet, wire_number=1)
trace_wire(wire2, circuit_cabinet, wire_number=2)

vertices = [Point(*p) for p, wires in circuit_cabinet.items() if len(wires) > 1]
vertices.sort(key=lambda v: one_norm(origin, v))
print(f"The closest vertex is at {vertices[0]},"
      f" which is a Manhattan distance of {one_norm(origin, vertices[0])} away from the origin")


# PART II
def count_steps(wire, verts):
    step_counts = {}
    cursor = Cursor(0, 0)
    move = {'U': cursor.up, 'D': cursor.down, 'L': cursor.left, 'R': cursor.right}
    steps = 0
    for direction, distance in [(s[0], int(s[1:])) for s in wire]:
        for n in range(distance):
            move[direction]()
            steps += 1
            if cursor.coordinates in verts:
                step_counts[Point(*cursor.coordinates)] = steps


    return step_counts

wire1_steps = Counter(count_steps(wire1, vertices))
wire2_steps = Counter(count_steps(wire2, vertices))

combined_step_totals = dict(wire1_steps + wire2_steps)

print(f"The shortest combined distance to a vertex is {min(combined_step_totals.values())}")
