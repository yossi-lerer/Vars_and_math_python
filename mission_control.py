agent_name = "jj"
mission_code = 118842
distance_to_target = 10.8
mission_active_atatus = True
print(f"agent name: {agent_name}, mission code: {mission_code}, distance to target: {distance_to_target}, mission active status: {mission_active_atatus}")
print(f"type of all varable: agent_name {type(agent_name)}, mission_code: {type(mission_code)}, distance_to_target: {type(distance_to_target)}, mission_active_atatus: {type(mission_active_atatus)}.")

travel_distance = distance_to_target * 2 
print(f"full distance for a trip from base to target and back: {travel_distance}")

fuel_usage = 2 # liter/KM
fuel_needed = fuel_usage * travel_distance
print(f"fuel needed for the trip: {fuel_needed}")

total_fuel = 200
remaining_fuel = total_fuel - fuel_needed
print(f"remaining fuel: {remaining_fuel}")