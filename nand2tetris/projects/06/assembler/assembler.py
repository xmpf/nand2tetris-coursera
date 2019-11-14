#!/usr/bin/env python3

import sys

from parser import Parser
from symbol_table import SymbolTable

from internals import DEST_MAP
from internals import COMP_MAP
from internals import JUMP_MAP

class Assembler:
    def __init__(self):
        self.symtab = SymbolTable()
        self.parser = Parser()
        
        self.buffer = []
        self.lineno = 0

        self.source_filename = None
        self.binary_filename = None
        self.next_free = 16
        

    def run(self, filename = None):
        if filename == None:
            raise Exception('Missing filename')

        self.source_filename = filename
        self.binary_filename = self.source_filename.split('.')[0] + '.hack'

        # preprocess file, scan for labels, variables, etc
        self.first_pass()
        # translate expressions
        self.assemble()


    def first_pass(self):
        with open(self.source_filename, 'r') as fr:
            for line in fr:
                line = line.split('//')[0].strip()  # remove junk
                if len(line) == 0: continue         # skip whitespace
                
                self.buffer.append(line)

                # add all variables and labels in symbol table
                expr_ty = self.parser.type_of_expression(line)
                if expr_ty != 'L': self.lineno += 1
                if expr_ty == 'L':
                    # add label
                    _, v = self.parser.parse_label(line)
                    self.symtab.insert(v, self.lineno)

    def assemble(self):
        with open(self.binary_filename, 'w') as fw:
            for line in self.buffer:
                t, v = self.parser.parse_line(line)
                if t == 'L': continue
                bin_expr = self.translate(t, v)
                fw.write(bin_expr + '\n')

    def translate(self, expr_ty, value):
        if expr_ty == 'A-VAR': 
            v = self.symtab.lookup(value)
            if v == None:
                self.symtab.insert(value, self.next_free)
                v = self.next_free
                self.next_free += 1
            return bin(v)[2::].zfill(16)
        elif expr_ty == 'A-INT':
            return bin(value)[2::].zfill(16)
        elif expr_ty == 'C':
            dest, comp, jump = value
            return f'111{COMP_MAP[comp]}{DEST_MAP[dest]}{JUMP_MAP[jump]}'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('Wrong number of parameters given!')
    
    assembler = Assembler()
    assembler.run(str(sys.argv[1]))
    for line in assembler.buffer:
        print(line)