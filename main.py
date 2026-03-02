

from cpu import CPU
from instructionparser import parse_program


cpu = CPU()
program = parse_program("program.txt")

cpu.load_program(program)
cpu.run()

print("Registers:", cpu.registers)


#       =======================================================================================
# 
# ++ 1 ++ 
# I need clean error messages, comments, a STRONG README, design_notes.pdf, architecture diagram,
# and example programs tested, for this to appear well polished.
# README: Project Overview, How it Works, Instruction Set, Example Program, How to Run,
# Design Decisions, Future Improvements
#
# ++ 2 ++ 
# I need to document this process on git as soon as possible.
#
# ++ 3 ++
# A debug mode would BANG, and a binary instruction encoder would slap too. 
#
# ++ 4 ++
# ADVANCED: Binary instruction decoding, Full ARM instruction set, pipeline simulation,
# cache simulation (whatever cache is?), Interrupt system, step execution?, instruction counter