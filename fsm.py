# Finite-state machine (FSM) by @AnRV90
# Displays Fibonacci Sequence
# Python >= 3.6
import time
from enum import Enum, auto

# States of FSM
class States(Enum):    
    ini = auto()
    fib = auto()
    off = auto()

def ini():
    # Code
    global a 
    global b
    a = b = 1
    print(a)
    print(b)

    # Next state
    return States.fib

def fib():
    # Code
    global a
    global b
    c = a + b
    print(c)
    a = b
    b = c
    time.sleep(0.1)

    # Next state
    if a + b < 620:
        return States.fib
    else:
        return States.off

def off():
    # Code
    pass

# FSM function
def fsm(st):
    switcher = {
        States.off: off,
        States.ini: ini,
        States.fib: fib
        }
    func = switcher.get(st)
    return func()

# Iterative function
def fsm_loop(st):
    while 1:
        if st == States.off:
            fsm(st)
            break
        else:
            st = fsm(st)

# Runs iterative function
fsm_loop(States.ini)
