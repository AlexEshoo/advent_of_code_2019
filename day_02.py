class ProgramRuntime(object):
    def __init__(self, instructions):
        self.memory = instructions.copy()
        self.cursor = 0
        self.stop = False

    def read_at_cursor(self, offset=0):
        return self.memory[self.cursor + offset]

    def deref(self, pos):
        return self.memory[self.memory[pos]]

    def execute_command(self, cmd):
        if cmd == 1:
            m = self.deref(self.cursor + 1)
            n = self.deref(self.cursor + 2)
            r = m + n
        elif cmd == 2:
            m = self.deref(self.cursor + 1)
            n = self.deref(self.cursor + 2)
            r = m * n
        elif cmd == 99:
            self.stop = True
            return
        else:
            raise RuntimeError(f"Unrecognized command {cmd}")

        self.memory[self.read_at_cursor(offset=3)] = r
        self.cursor += 4

    def execute_next_instruction(self):
        try:
            cmd = self.read_at_cursor()
            self.execute_command(cmd)
        except IndexError:
            self.stop = True

    def run(self):
        while not self.stop:
            self.execute_next_instruction()


with open("input/input_day02.txt") as f:
    inst = [int(n) for n in f.read().split(',')]

# Initialize state:
inst[1] = 12
inst[2] = 2

rt = ProgramRuntime(inst)
rt.run()

print(f"Final value of position 0: {rt.memory[0]}")


## Part II

for noun in range(0, 100):
    for verb in range(0, 100):
        inst[1] = noun
        inst[2] = verb
        rt = ProgramRuntime(inst)
        rt.run()
        if output := rt.memory[0] == 19690720:
            print(f"Parameters found: noun = {noun}, verb = {verb}. Answer: {100 * noun + verb}")
            break
