class StatefulClassroomAgent:
    def __init__(self):
        # Internal storage for the previous target mode
        self.previous_mode = None

    def act(self, temp, occupied):
        # Keep existing temperature thresholds and occupancy priority from the lab manual
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        # Avoid repeating identical control commands
        if self.previous_mode == target_mode:
            send_command = False
        else:
            send_command = True
            self.previous_mode = target_mode

        # Return both the target and whether a command should be sent
        return target_mode, send_command


agent = StatefulClassroomAgent()

# Required scenarios: empty-room, repeated percepts, mode transition, exact boundaries
test_cases = [
    {"desc": "Empty-room case", "temp": 24, "occupied": False},
    {"desc": "Repeated empty-room percept", "temp": 22, "occupied": False},
    {"desc": "Mode transition (Hot)", "temp": 28, "occupied": True},
    {"desc": "Repeated percept (Hot)", "temp": 27, "occupied": True},
    {"desc": "Exact boundary 26C", "temp": 26, "occupied": True},
    {"desc": "Exact boundary 20C", "temp": 20, "occupied": True},
    {"desc": "Mode transition (Cold)", "temp": 18, "occupied": True},
    {"desc": "Exact boundary 20C again", "temp": 20, "occupied": True},
]
#Formatting
print(f"{'Step':<5} | {'Prev Mode':<9} | {'Percept (T, Occ)':<16} | {'Target':<7} | {'Command Sent'}")
print("-" * 65)

# For display purposes, track what the previous mode was at the start of the step
prev_display = "None"

for step, case in enumerate(test_cases, 1):
    temp = case["temp"]
    occupied = case["occupied"]
    
    # Act based on current percept
    target_mode, send_command = agent.act(temp, occupied)
    
    # Record previous mode, percept, target, and command/no-command outcome
    print(f"{step:<5} | {prev_display:<9} | {f'({temp}C, {occupied})':<16} | {target_mode:<7} | {send_command}")
    
    # Update the display tracker if a command was sent and state changed
    if send_command:
        prev_display = target_mode
