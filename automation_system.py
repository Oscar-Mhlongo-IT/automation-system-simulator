# Author: Oscar
# Project: Automation System Simulator
# Description: Advanced rule-based automation system

print("=== SMART AUTOMATION SYSTEM ===")

# Get inputs
temperature = int(input("Enter temperature: "))
humidity = int(input("Enter humidity: "))
time_of_day = input("Enter time of day (day/night): ").lower()

print("\n--- SYSTEM ANALYSIS ---")

# Automation logic
if temperature > 30 and humidity > 70:
    print("🔥 Decision: Turn ON Cooling System (High Temp & Humidity)")
elif temperature > 30:
    print("🌡️ Decision: Activate Ventilation System")
elif temperature < 15:
    print("❄️ Decision: Turn ON Heating System")

if humidity < 30:
    print("💧 Decision: Activate Humidifier")
elif humidity > 80:
    print("🌫️ Decision: Activate Dehumidifier")

if time_of_day == "night":
    print("🌙 Decision: Enable Energy Saving Mode")
else:
    print("☀️ Decision: Normal Operation Mode")

# Final system state
print("\n✅ Automation Complete")
