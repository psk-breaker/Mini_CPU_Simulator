
OPERATIONS = {
    'MOV': 0b0000,
    'ADD': 0b0001,
    'SUB': 0b0010,
    'LOAD': 0b0011,
    'STORE': 0b0100,
    'JMP': 0b0101,
    'HLT': 0b0110,
    'CMP': 0b0111,
    'BEQ': 0b1000,
    'BNE': 0b1001,
    'BLT': 0b1010
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
    elif operation in ['ADD', 'SUB', 'CMP']:
        first_register = REGISTERS[tokens[1]]
        second_register = REGISTERS[tokens[2]]
    elif operation in ['BEQ', 'BNE', 'BLT']:
        immediate_value = int(tokens[1])
    
    operation = OPERATIONS[tokens[0]]
    print(f'Binary instruction: {operation} {first_register} {second_register} {immediate_value}')
    encoded_instruction = (operation << 12) | (first_register << 10) | (second_register << 8) | (immediate_value & 0b11111111)
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