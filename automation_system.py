# Author: Oscar
# Project: Automation System Simulator
# Description: Rule-based automation using Python

# Automation System Simulator
print("=== Automation System ===")

# Get user input
temperature = int(input("Enter temperature: "))
humidity = int(input("Enter humidity: "))

# Automation logic
if temperature > 30 and humidity > 70:
    print("Decision: Turn ON Cooling System")
elif temperature < 15:
    print("Decision: Turn ON Heating System")
elif humidity < 30:
    print("Decision: Activate Humidifier")
else:
    print("Decision: System is Stable")
