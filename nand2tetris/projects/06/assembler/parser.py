#!/usr/bin/env python3

class Parser:
    def __init__(self):
        self.lineno = 0             # keep track of current line

    def parse_label(self, line):
        if self.type_of_expression(line) != 'L':
            raise Exception('Expression is not in type-L format')
        return ('L', line[1:-1])
    
    def parse_instr_type_A(self, line):
        '''
        Parse instructions of type-A format
            @VARIABLE_NAME
            @1234
        '''
        if self.type_of_expression(line) != 'A':
            raise Exception('Expression is not in type-A format')

        line = line[1::]
        if line.isnumeric():
            return ('A-INT', int(line))
        else:
            return ('A-VAR', line)
    
    def parse_instr_type_C(self, line : str):
        '''
        Parse instructions of type-C format
            dest=comp
            dest=comp;jmp
            comp;jmp
        '''
        if self.type_of_expression(line) != 'C':
            raise Exception('Expression is not in type-C format')

        dest = None
        comp = None
        jump = None

        split_eq = line.split('=')
        if len(split_eq) == 2: 
            dest = split_eq[0]
            split_eq_sem = split_eq[1].split(';')
            comp = split_eq_sem[0]
            if len(split_eq_sem) == 2:
                jump = split_eq_sem[1]
        else:
            split_sem = line.split(';')
            comp = split_sem[0]
            jump = split_sem[1]

        return ('C', [dest, comp, jump])

    def parse_line(self, line : str):
        ret = None
        if line[0] == '@':
            ret = self.parse_instr_type_A(line)
        elif line[0] == '(':
            if line[-1] != ')': 
                raise Exception(f'Error: Unable to parse label - missing closing bracket at line {self.lineno}')
            ret = self.parse_label(line)
        else:
            ret = self.parse_instr_type_C(line)
        self.lineno += 1
        return ret

    def type_of_expression(self, line : str) -> str:
        if line[0] == '@': return 'A'
        elif line[0] == '(': return 'L'
        else: return 'C'