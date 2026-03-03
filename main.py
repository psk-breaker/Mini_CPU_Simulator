

from cpu import CPU
from instructionparser import parse_program


cpu = CPU()
program = parse_program("program.txt")

cpu.load_program(program)
cpu.run()

print('Registers:', cpu.registers)
print('Memory:', cpu.memory)


#       =======================================================================================
# 
# ++ 1 ++
# FETCH - DECODE - EXECUTE LOOP needs to reflect reality of CPUs: 
#     - Program of instruction set
#     - Parsed and encoded instructions, creating machine code
#     - Machine code stored in memory blocks
#     - Fetch() retrieving instruction machine code from memory and feeding into register - R0 is program counter 
#       and memory address of next instruction
#     - Decode() 
#     - Execute()
# ++ 2 ++ 
# I need clean error messages, comments, a STRONG README, design_notes.pdf, architecture diagram.
# 
# README: Project Overview, How it Works, Instruction Set, Example Program, How to Run,
# Design Decisions, Future Improvements
#
# ++ 3 ++
# Debug mode next up
#
# ++ 4 ++
# ADVANCED: Pipeline simulation, cache simulation, Interrupt system, step execution