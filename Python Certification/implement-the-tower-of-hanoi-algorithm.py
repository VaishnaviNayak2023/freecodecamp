def hanoi_solver(n):
    # Initialize rods: A with all disks, B and C empty
    rod_a = list(range(n, 0, -1))
    rod_b = []
    rod_c = []
    
    moves = []
    
    # Helper function to record current state
    def record_state():
        moves.append(f"{rod_a} {rod_b} {rod_c}")
    
    # Recursive function to move disks
    def move_disks(num, source, target, auxiliary):
        if num == 0:
            return
        # Move n-1 disks to auxiliary
        move_disks(num - 1, source, auxiliary, target)
        # Move the largest disk from source to target
        target.append(source.pop())
        record_state()
        # Move n-1 disks from auxiliary to target
        move_disks(num - 1, auxiliary, target, source)
    
    # Record initial state
    record_state()
    # Solve the puzzle
    move_disks(n, rod_a, rod_c, rod_b)
    
    # Return moves as a single string with newlines
    return "\n".join(moves)
