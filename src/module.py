from typing import List

def rolling_average(values: List, period:int) -> List:
    rolling_averages = []

    for i in range(period, len(values)+1):
        average = sum(values[1-period:i]) / period
    
    return rolling_averages