class CPU:
    def __init__(self):
        self.registers = [0] * 4
        self.memory = [0] * 256
        self.pc = 0
        self.running = True
        self.program = []

    def load_program(self, instructions):
        self.program = instructions

    def get_value(self, operand):
        # If operand is register like R0, return its value
        if operand.startswith("R"):
            return self.registers[int(operand[1])]
        # Otherwise it's a number
        return int(operand)

    def execute(self, instruction):
        op = instruction[0]

        if op == "MOV":
            reg = int(instruction[1][1])
            value = self.get_value(instruction[2])
            self.registers[reg] = value

        elif op == "ADD":
            reg = int(instruction[1][1])
            value = self.get_value(instruction[2])
            self.registers[reg] += value

        elif op == "SUB":
            reg = int(instruction[1][1])
            value = self.get_value(instruction[2])
            self.registers[reg] -= value

        elif op == "LOAD":
            reg = int(instruction[1][1])
            addr = int(instruction[2])
            self.registers[reg] = self.memory[addr]

        elif op == "STORE":
            reg = int(instruction[1][1])
            addr = int(instruction[2])
            self.memory[addr] = self.registers[reg]

        elif op == "JMP":
            addr = int(instruction[1])
            self.pc = addr
            return  # skip pc increment

        elif op == "HLT":
            self.running = False

        else:
            raise ValueError(f"Unknown instruction: {op}")

        self.pc += 1

    def run(self):
        while self.running and self.pc < len(self.program):
            instr = self.program[self.pc]
            self.execute(instr)