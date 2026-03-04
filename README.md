# 16-Bit RISC CPU Simulator (Python)
[Build](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)
By [psk-breaker](https://github.com/psk-breaker/Mini_CPU_Simulator)[Socials]

A from-scratch simulation of a 16-bit load/store RISC processor written in Python.

This project models the fundamental components of a real CPU — including instruction parsing (assembling), binary encoding, registers, RAM, a program counter, an ALU, status flags, and a full fetch–decode–execute cycle.

The goal of this project was to move beyond high-level programming and gain a deeper understanding of how software executes at the hardware level. Programs can be written from scratch using the instructions provided, with capabilities to add, subtract, loop and store values.


## What This Project Demonstrates

Instruction set architecture (ISA) design

Binary instruction encoding & decoding

Bit manipulation (bit shifting, masking, packing fields)

Fetch–decode–execute cycle

Register file design

Load/store memory architecture

Status flags, looping logic & conditional branching

Program control flow at machine level


## Technical Specs

This project implements a mini 16-bit RISC-style processor with:

4 general-purpose registers

256 memory locations (RAM)

16-bit fixed-width instruction format

4-bit opcode field (supporting up to 16 instructions)

8-bit immediate values

Zero (Z) and Negative (N) status flags

Conditional branching instructions

Load/store memory model

It supports arithmetic operations, memory access, jumps, comparisons, and loops.


## Architecture Overview

Each instruction follows the classical CPU pipeline:

Fetch

Program Counter (PC) reads instruction from memory

PC increments automatically

Decode

Bit shifting & masking extract opcode and operands

Execute

ALU performs arithmetic

Registers update

Flags update

PC may change (branch instructions)


## Load/Store Architecture

The simulator implements a RISC-style load/store design:

Arithmetic operates only on registers

Memory is accessed exclusively through LOAD and STORE, and will not hold instructions as according to Harvard architecture design.

Control flow is handled via JMP, BEQ, BNE, and BLT

This design choice reflects modern architectures such as ARM ---> RISC-V.


## Status Flags - Looping Logic

The CPU maintains a small status register seperate from the 4 free registers available for compute. This register holds the two flags' states determined by the previous instruction:

Z (Zero) — Triggered when A == B

N (Negative) — Triggered when A < B

Where A and B represent values to be compared for compute purposes.

These flags enable conditional branching and loop construction, allowing full program logic to emerge from low-level operations.

Example control flow:
```python
0) MOV R0 5   # -- Update register 0 with value 5
1) MOV R1 1   # -- Update register 1 with value 1
2) SUB R0 R1  # -- R0 = R0 - R1
3) CMP R0 R1  # -- Flags = R0 - R1
4) BEQ 6      # -- Branch to instruction 6 if Flags previously raised
5) BNE 2      # -- Branch to instruction 2 if flags indicated not equal, thereby creating a looping behaviour.
6) MOV R2 10  
7) MOV R3 1
8) ADD R3 R1  # -- R3 = R3 + R1
9) CMP R3 R2
10) BLT 8     # -- If flags raised for R3 less than R2, branch to instruction 8.
11) HLT       # -- Halt compute.
```
This is how high-level constructs like if and while are implemented at machine level.
