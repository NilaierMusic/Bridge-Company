![Alt text](BridgeCompany.webp)

This repository contains a Python script for calculating the decay rate and time until collapse of a bridge based on the number of players, their weights, and the presence of a giant. The decay rate is determined by various factors, including the number of players on the bridge, the total weight they carry, and an optional giant's contribution.

## Usage

To use the script, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/NilaierMusic/Bridge-Company.git
   cd Bridge-Company
   ```

2. **Run the Script:**
   ```bash
   python bridge.py
   ```
   Follow the on-screen prompts to input the number of players, their weights, and whether a giant is present on the bridge.

3. **View Results:**
   The script will output the calculated decay rate and time until collapse of the bridge.

## Script Details

The core functionality of the script is encapsulated in the `calculate_decay_rate_and_time` function, which takes the number of players, their weights, and a flag indicating the presence of a giant as inputs. It then computes the decay rate and time until collapse based on the provided information.

### Function Signature

```python
def calculate_decay_rate_and_time(players, weights, is_giant):
    # Function logic...
    return total_decay_rate, time_until_collapse
```

### Input Parameters

- `players`: The number of players on the bridge.
- `weights`: A list containing the weights of each player.
- `is_giant`: A boolean flag indicating whether a giant is present on the bridge.

### Output

- `total_decay_rate`: The calculated decay rate of the bridge.
- `time_until_collapse`: The estimated time until the bridge collapses.

### Formula Used

The script employs the following formulas to calculate decay rate and time until collapse:

- `player_decay_rate`: 0.02 * players^2
- `weight_decay_rate`: 0.00265625 * total weight carried by players
- `total_decay_rate`: player_decay_rate + weight_decay_rate + (giant decay rate if giant is present)
- `time_until_collapse`: bridge durability / total_decay_rate

### User Input

The script prompts the user to input the number of players, the weight of each player, and whether a giant is currently on the bridge.

## Example

```bash
Enter the number of players on the bridge: 4
Enter the amount of weight for player 1: 16
Enter the amount of weight for player 2: 12
Enter the amount of weight for player 3: 19
Enter the amount of weight for player 4: 0
Is a giant currently on the bridge (yes/no)? no
The bridge will collapse in 2.25 seconds with a decay rate of 0.44484 per second.
```

Feel free to explore and modify the script to suit your needs!
