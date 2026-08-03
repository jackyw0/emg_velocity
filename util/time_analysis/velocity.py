import numpy as np
from util.time_analysis.correlation import estimate_delay



def calculate_velocity(distance_m, delay_seconds):
  if distance_m <= 0:
    raise ValueError("distance has to be greater than 0")
  
  #if delay_seconds == 0:
    #raise ValueError("delay should be nonzero")
  
  conduction_velocity = distance_m / delay_seconds

  return conduction_velocity