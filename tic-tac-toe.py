import re
import os

def return_state(s):
    if(len(s) != 9): return;
    for symbol in s:
        if(symbol not in ['X', 'O', '_']): return;
        
    if(abs(s.count('X') - s.count('O')) > 1): return "Impossible"
    
    check_states = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]
    state = []
    
    for arr in check_states:
        if not(s[arr[0]] == s[arr[1]] == s[arr[2]]): continue
        val = s[arr[0]]
        if(val == 'X'): state.append("X wins")
        elif(val == 'O'): state.append("O wins")
    
    if(len(state) > 1): return "Impossible"
    elif(len(state) == 1): return state[0]
    elif('_' in s): return "Game not finished"
    else: return "Draw"

            
def print_state(symbols):
    if(len(symbols) != 9): return;
    for symbol in symbols:
        if(symbol not in ['X', 'O', '_']): return;
    
    s = symbols.replace("_", " ")
    
    
    print(f"\n\t {s[0]} | {s[1]} | {s[2]} ")
    print("\t-----------")
    print(f"\t {s[3]} | {s[4]} | {s[5]} ")
    print("\t-----------")
    print(f"\t {s[6]} | {s[7]} | {s[8]} \n")
    
    
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_command(symbols, turn):
    command = input(f"(Player '{turn}')Enter the coordinates: ")
    if not(re.match('^[0-2]\s[0-2]$', command)):
        if(re.match('^\d{1,}\s\d{1,}', command)): 
            print("Coordinates should be from 0 to 2!")
            return get_command(symbols, turn)
        else: 
            print("You should enter numbers!")
            return get_command(symbols, turn)
    command = tuple([int(command.split(' ')[0]), int(command.split(' ')[1])])
    
    for r in range(3):
        for c in range(3):
            i = r * 3 + c
            pos = tuple([r, c])
            if(pos == command):
                if(symbols[i] != '_'): 
                    print("This cell is occupied! Choose another one!")
                    return get_command(symbols, turn)
                else:
                    symbols = symbols[:i] + turn + symbols[i+1:]
                    if(turn == 'X'): turn = 'O'
                    else: turn = 'X'
                    cls()
                    print_state(symbols)
                    result = return_state(symbols)
                    if(result == 'X wins' or result == 'O wins' or result == 'Draw'): 
                        return print(result)
                    return get_command(symbols, turn)
            
      
turn = "X"      
symbols = "_________"            
print_state(symbols)
get_command(symbols, turn)


