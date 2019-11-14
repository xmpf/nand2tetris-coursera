#!/usr/bin/env python3

from internals import INITIAL_SYMTAB

class SymbolTable:
    def __init__(self):
        self.symtab = INITIAL_SYMTAB

    def lookup(self, symbol : str) -> int:
        try:
            return self.symtab[symbol]
        except KeyError:
            return None

    def insert(self, symbol : str, value : int):
        self.symtab[symbol] = value