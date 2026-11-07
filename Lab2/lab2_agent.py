class StatefulClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        if self.previous_mode == target_mode:
            send_command = False
        else:
            send_command = True
            self.previous_mode = target_mode

        return target_mode, send_command


agent = StatefulClassroomAgent()
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

print(f"{'Step':<5} | {'Prev Mode':<9} | {'Percept (T, Occ)':<16} | {'Target':<7} | {'Command Sent'}")
print("-" * 65)

prev_display = "None"

for step, case in enumerate(test_cases, 1):
    temp = case["temp"]
    occupied = case["occupied"]
    
    target_mode, send_command = agent.act(temp, occupied)
    
    print(f"{step:<5} | {prev_display:<9} | {f'({temp}C, {occupied})':<16} | {target_mode:<7} | {send_command}")
    
    if send_command:
        prev_display = target_mode
