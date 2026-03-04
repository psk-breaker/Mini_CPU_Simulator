

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
# README: Project Overview, How it Works, Instruction Set, Example Program, How to Run,
# Design Decisions, Future Improvements
# Design notes.pdf
# Architecture diagram
#
