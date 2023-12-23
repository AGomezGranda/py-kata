def zero_fuel(distance_to_pump, mpg, fuel_left):
    range_left = mpg * fuel_left
    return range_left >= distance_to_pump
