from typing import List

def rolling_average(values: List, period:int) -> List:
    rolling_averages = []

    for i in range(period, len(values)+1):
        average = sum(values[1-period:i]) / period
        rolling_averages.append(average)
    
    return rolling_averages

def sum_two_values (val1: int, val2: int):
    
    return val1 + val2