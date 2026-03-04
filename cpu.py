class CPU:
    def __init__(self):
        self.registers = [0] * 4
        self.memory = [0] * 256
        self.pc = 0
        self.running = True
        self.program = []
        self.flags = {
            'Z': 0,
            'N': 0
        }

    def load_program(self, program):
        self.program = program

    def update_flags(self, result):
        self.flags['Z'] = int(result == 0)
        self.flags['N'] = int(result < 0)

    def fetch(self):
        instruction = self.program[self.pc]
        self.pc += 1
        return instruction

    def decode(self, instruction):
        operation = instruction >> 12
        first_register = (instruction >> 10) & 0b11
        second_register = (instruction >> 8) & 0b11
        immediate_value = instruction & 0b11111111
        return operation, first_register, second_register, immediate_value

    def execute(self, operation, first_register, second_register, immediate_value):
        
        # HLT
        if operation == 0b0110:
            self.running = False
        
        #JMP
        elif operation == 0b0101:
            self.pc = immediate_value

        # LOAD
        elif operation == 0b0011:
            self.registers[first_register] = self.memory[immediate_value]
        
        # STORE
        elif operation == 0b0100:
            self.memory[immediate_value] = self.registers[first_register]
        
        # MOV
        elif operation == 0b0000:
            self.registers[first_register] = immediate_value
        
        # ADD
        elif operation == 0b0001:
            self.registers[first_register] += self.registers[second_register]
            
        # SUB
        elif operation == 0b0010:
            self.registers[first_register] -= self.registers[second_register]
        
        # CMP
        elif operation == 0b0111:
            result = self.registers[first_register] - self.registers[second_register]
            self.update_flags(result)
        
        # BEQ
        elif operation == 0b1000:
            if self.flags['Z'] == 1:
                self.pc = immediate_value
        
        # BNE 
        elif operation == 0b1001:
            if self.flags['Z'] == 0:
                self.pc = immediate_value
        
        # BLT
        elif operation == 0b1010:
            if self.flags['N'] == 1:
                self.pc = immediate_value

        else:
            raise ValueError(f"Unknown instruction: {operation}")

        

    def run(self):
        while self.running and self.pc < len(self.program):
            fetched_instruction = self.fetch()
            operation, first_register, second_register, immediate_value = self.decode(fetched_instruction)
            self.execute(operation, first_register, second_register, immediate_value)