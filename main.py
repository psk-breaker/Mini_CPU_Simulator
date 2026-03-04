

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
# I need clean error messages, comments, a STRONG README, design_notes.pdf, architecture diagram.
# 
# README: Project Overview, How it Works, Instruction Set, Example Program, How to Run,
# Design Decisions, Future Improvements
#
# ++ 2 ++
# Debug mode next up
#
# ++ 3 ++
# ADVANCED: Pipeline simulation, cache simulation, Interrupt system, step execution