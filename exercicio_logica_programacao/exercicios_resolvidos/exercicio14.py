import math

def calculate_traffic_light_sync_time(distance, speed_limit_kmh, acceleration, buffer_time=3):
    """
    Calculates the synchronization time for the next traffic light.

    Args:
        distance (float): Distance between traffic lights in meters.
        speed_limit_kmh (float): Speed limit of the road in km/h.
        acceleration (float): Typical car acceleration in m/s².
        buffer_time (int): Time in seconds for the light to turn green before the car arrives.

    Returns:
        float: The time in seconds for the next traffic light to turn green.
    """
    speed_limit_mps = speed_limit_kmh / 3.6

    accel_time = speed_limit_mps / acceleration
    accel_distance = 0.5 * acceleration * accel_time**2

    if accel_distance >= distance:
        total_travel_time = math.sqrt(2 * distance / acceleration)
    else:
        constant_speed_distance = distance - accel_distance
        constant_speed_time = constant_speed_distance / speed_limit_mps
        total_travel_time = accel_time + constant_speed_time

    sync_time = total_travel_time - buffer_time

    return sync_time

distance_between_lights = 500
speed_limit = 60
car_acceleration = 2.5

sync_time = calculate_traffic_light_sync_time(
    distance_between_lights,
    speed_limit,
    car_acceleration
)

print(f"The next traffic light should turn green {sync_time:.2f} seconds later.")

short_distance = 30

short_sync_time = calculate_traffic_light_sync_time(
    short_distance,
    speed_limit,
    car_acceleration
)

print(f"On a shorter stretch, the traffic light should turn green {short_sync_time:.2f} seconds later.")