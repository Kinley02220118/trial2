def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk {n} from {source} to {destination}")
    else:
        tower_of_hanoi(n-1, source, destination, auxiliary)
        print(f"Move disk {n} from {source} to {destination}")
        tower_of_hanoi(n-1, auxiliary, source, destination)

# Example usage:
n = 3  # Number of disks
tower_of_hanoi(n, 'Rod 1', 'Rod 2', 'Rod 3')