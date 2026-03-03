
OPERATIONS = {
    'MOV': 0b000,
    'ADD': 0b001,
    'SUB': 0b010,
    'LOAD': 0b011,
    'STORE': 0b100,
    'JMP': 0b101,
    'HLT': 0b111
}

REGISTERS = {
    'R0': 0b00,
    'R1': 0b01,
    'R2': 0b10,
    'R3': 0b11
}

def encode(tokens):
    operation = tokens[0]
    first_register = 0
    second_register = 0
    immediate_value = 0

    if operation == 'HLT':
        pass
    elif operation == 'JMP':
        immediate_value = int(tokens[1])
    elif operation in ['LOAD', 'STORE']:
        first_register = REGISTERS[tokens[1]]
        immediate_value = int(tokens[2])
    elif operation == 'MOV':
        first_register = REGISTERS[tokens[1]]
        immediate_value = int(tokens[2])
    elif operation in ['ADD', 'SUB']:
        first_register = REGISTERS[tokens[1]]
        second_register = REGISTERS[tokens[2]]
    
    operation = OPERATIONS[tokens[0]]
    print(f'Binary instruction: {operation} {first_register} {second_register} {immediate_value}')
    encoded_instruction = (operation << 13) | (first_register << 11) | (second_register << 9) | (immediate_value & 0b111111111)
    return encoded_instruction


def parse_program(filename):
    machine_code = []

    with open(filename, "r") as file:
        for line in file:
            # skip blank lines or comments
            if not line or line.startswith("#"):
                continue
            else:
                line = line.strip()
                tokens = line.split()
                print(f'Tokens: {tokens}')
                encoded_instruction = encode(tokens)
                machine_code.append(encoded_instruction)
    
    print(f'Machine code: {machine_code}')
    return machine_code