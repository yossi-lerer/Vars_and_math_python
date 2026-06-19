# #step 2
# agent_name = "jj"
# mission_code = 118842
# distance_to_target = 10.8
# mission_active_atatus = True
# #step 3
# print(f"agent name: {agent_name}, mission code: {mission_code}, distance to target: {distance_to_target}, mission active status: {mission_active_atatus}")
# #step 4
# print(f"type of all varable: agent_name {type(agent_name)}, mission_code: {type(mission_code)}, distance_to_target: {type(distance_to_target)}, mission_active_atatus: {type(mission_active_atatus)}.")
# #step 5
# travel_distance = distance_to_target * 2 
# print(f"full distance for a trip from base to target and back: {travel_distance}")
# #step 6
# fuel_usage = 2 # liter/KM
# fuel_needed = fuel_usage * travel_distance
# print(f"fuel needed for the trip: {fuel_needed}")
# #step 7
# total_fuel = 200
# remaining_fuel = total_fuel - fuel_needed
# print(f"remaining fuel: {remaining_fuel}")
# #step 8
# countdown_conversion = input("How long until your mission starts in seconds? ")
# countdown_conversion = int(countdown_conversion)
# countdown_in_minutes = countdown_conversion / 60
# countdown_in_hours = countdown_in_minutes / 60
# print(f"your mission start at {countdown_in_hours} hours. in minutes at {countdown_in_minutes}. at seconds {countdown_conversion}")
# #step 9
# km_input = int(input("enter km to convert it to miles "))
# km_to_mile = km_input * 0.6214
# print(f"{km_input} km = {km_to_mile} miles")
# #step 10 
# new_agent_name = input("enter new name for agent ")
# agent_name = new_agent_name
# print(f"new agent name is {agent_name}")

#part 2 binary
#step 1 
binary_str = ''.join(format(ord(char), '08b') for char in "5")
binary_number = bin(5)
check_bin_equals = binary_str == binary_number
print(f"are they binary the same? {check_bin_equals}")
which_is_larger = binary_str > binary_number
print(f"the 5 in string is larger? {which_is_larger}.")
