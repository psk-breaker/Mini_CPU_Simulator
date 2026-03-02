

def encode(instruction):
    
    return


def parse_program(filename):
    instructions = []

    with open(filename, "r") as file:
        for line in file:
            print(line)
            line = line.strip()

            # skip blank lines or comments
            if not line or line.startswith("#"):
                continue

            tokens = line.split()
            print(tokens)
            instructions.append(tokens)
    
    print(instructions)
    return instructions