# Andrew Keefe
# RBOT 250, Exercise 2
# October 19, 2021

import math
import numpy as np

# axis of motion,  k = [0, 0 ,1]
# rotation angle, theta = 45 degrees (pi/4)

theta = math.pi/4

# compute exponential map of the rotation angle using Rodrigue's formula
# https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula

# Rodrigue's formula
# R = I + (sin(theta)K + (1-cos(theta)K^2))
# K = [[0, -kz, ky],[kz, 0, -kz],[-ky, kx,0]]

k = np.array([0,0,1])
K = np.array([[0, -k[2], k[1]],[k[2], 0, -k[2]],[-k[1],k[0],0]])

I = np.array([[1,0,0],[0,1,0],[0,0,1]])

R = I + (math.sin(theta)*K + (1.-math.cos(theta)*np.square(K)))

print(R)