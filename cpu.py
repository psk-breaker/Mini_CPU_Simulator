class CPU:
    def __init__(self):
        self.registers = [0] * 4
        self.memory = [0] * 256
        self.pc = 0
        self.running = True
        self.program = []

    def load_program(self, program):
        self.program = program

    def fetch(self,):
        instruction = self.program[self.pc]
        self.pc += 1
        return instruction

    def decode(self, instruction):
        operation = instruction >> 13
        first_register = (instruction >> 11) & 0b11
        second_register = (instruction >> 9) & 0b11
        immediate_value = instruction & 0b111111111
        return operation, first_register, second_register, immediate_value

    def execute(self, operation, first_register, second_register, immediate_value):
        
        # HLT
        if operation == 0b111:
            self.running = False
        
        #JMP
        elif operation == 0b101:
            self.pc = immediate_value

        # LOAD
        elif operation == 0b011:
            self.registers[first_register] = self.memory[immediate_value]
        
        # STORE
        elif operation == 0b100:
            self.memory[immediate_value] = self.registers[first_register]
        
        # MOV
        elif operation == 0b000:
            self.registers[first_register] = immediate_value
        
        # ADD
        elif operation == 0b001:
            self.registers[first_register] += self.registers[second_register]
            
        # SUB
        elif operation == 0b010:
            self.registers[first_register] -= self.registers[second_register]

        else:
            raise ValueError(f"Unknown instruction: {operation}")

        

    def run(self):
        while self.running and self.pc < len(self.program):
            fetched_instruction = self.fetch()
            operation, first_register, second_register, immediate_value = self.decode(fetched_instruction)
            self.execute(operation, first_register, second_register, immediate_value)