state = {'A': None, 'B': None, 'C': None, 'D': None}  
print("Initial states:")
for block in state:
    if state[block] is None:
        print(f"Block {block} is on the table.")
    else:
        print(f"Block {block} is on top of {state[block]}.")
        
print("\nMaking some moves:")
state['D'] = 'None'  # Block D is on top (on the table)
state['C'] = 'D'     # Block C is on top of D
state['B'] = 'C'     # Block B is on top of C
state['A'] = 'B'     # Block A is on top of B

# Print final state of the blocks
for block in state:
    if state[block] is None:
        print(f"Block {block} is on the table.")
    else:
        print(f"Block {block} is on top of {state[block]}.")
