def calculate_decay_rate_and_time(players, weights, is_giant):
    base_decay_rate_per_second = 0.02
    extra_decay_rate_per_pound = 0.00265625
    giant_decay_rate_per_second = 1/6
    bridge_durability = 1.0
    
    # Calculate the decay rate from the players
    player_decay_rate = base_decay_rate_per_second * (players ** 2)
    
    # Calculate additional decay rate from the total weight carried by players
    weight_decay_rate = sum(weights) * extra_decay_rate_per_pound
    
    # Calculate total decay rate
    total_decay_rate = player_decay_rate + weight_decay_rate
    
    # Add decay rate from the giant if present
    if is_giant:
        total_decay_rate += giant_decay_rate_per_second
    
    # Calculate time until collapse
    time_until_collapse = bridge_durability / total_decay_rate

    # Ensure time doesn't become negative
    time_until_collapse = max(time_until_collapse, 0)
    
    return total_decay_rate, time_until_collapse

# Ask user for inputs
players = int(input("Enter the number of players on the bridge: "))
weights = []

for i in range(players):
    weight = float(input(f"Enter the amount of weight for player {i+1}: "))
    weights.append(weight)

is_giant = input("Is a giant currently on the bridge (yes/no)? ").lower() == "yes"

# Calculate and display the results
decay_rate, time_until_collapse = calculate_decay_rate_and_time(players, weights, is_giant)
print(f"The bridge will collapse in {time_until_collapse:.2f} seconds with a decay rate of {decay_rate:.5f} per second.")