# import random
# import math


# def initialize(N, systemEnergy, delta):
#     v = [math.sqrt(2.0 * systemEnergy / N) for _ in range(N)]
#     demonEnergy = 2
#     mcs = 0
#     systemEnergyAccumulator = 0
#     demonEnergyAccumulator = 0
#     acceptedMoves = 0
#     return v, demonEnergy, mcs, systemEnergyAccumulator, demonEnergyAccumulator, acceptedMoves


# def doOneMCStep(v, demonEnergy, mcs, systemEnergyAccumulator, demonEnergyAccumulator, acceptedMoves, N, delta):
#     for j in range(N):
#         particleIndex = int(random.random() * N)
#         dv = (2.0 * random.random() - 1.0) * delta
#         trialVelocity = v[particleIndex] + dv

#         dE = 0.5 * (trialVelocity ** 2 - v[particleIndex] ** 2)

#         if dE <= demonEnergy:
#             v[particleIndex] = trialVelocity
#             acceptedMoves += 1
#             systemEnergyAccumulator += systemEnergy + dE
#             demonEnergyAccumulator += demonEnergy - dE

#         mcs += 1

#     return v, demonEnergy, mcs, systemEnergyAccumulator, demonEnergyAccumulator, acceptedMoves


# # Usage
# N = 10  # Set the number of particles
# systemEnergy = 100.0  # Set the initial system energy
# delta = 1  # Set the delta value

# v, demonEnergy, mcs, systemEnergyAccumulator, demonEnergyAccumulator, acceptedMoves = initialize(
#     N, systemEnergy, delta)

# print(v, demonEnergy, mcs, systemEnergyAccumulator,
#       demonEnergyAccumulator, acceptedMoves)

# for _ in range(100):  # Perform 1000 MC steps
#     v, demonEnergy, mcs, systemEnergyAccumulator, demonEnergyAccumulator, acceptedMoves = doOneMCStep(
#         v, demonEnergy, mcs, systemEnergyAccumulator, demonEnergyAccumulator, acceptedMoves, N, delta)

# print("Accepted Moves:", acceptedMoves)
# print("System Energy:", systemEnergyAccumulator / mcs)
# print("Demon Energy:", demonEnergyAccumulator / mcs)
import numpy as np
import random
import math
import matplotlib.pyplot as plt

# Define the lattice size
L = 20

# Initialize the protein conformation randomly on the lattice
protein = np.random.choice([-1, 1], size=(L, L))

# Define the initial temperature and cooling rate
T = 1.0
cooling_rate = 0.95

# Define the number of Monte Carlo steps
MCS = 10000

# Define lists to store the energy and temperature values
energies = []
temperatures = []

# Define the energy function (simplified)


def calculate_energy(protein):
    return -np.sum(protein)


# Main Metropolis algorithm loop
for step in range(MCS):
    # Randomly select a position on the lattice
    x, y = random.randint(0, L - 1), random.randint(0, L - 1)

    # Calculate the energy change if we flip the residue at (x, y)
    protein[x, y] *= -1
    delta_energy = calculate_energy(protein) - calculate_energy(protein)

    # Accept or reject the move based on the Metropolis criterion
    if delta_energy <= 0 or random.random() < math.exp(-delta_energy / T):
        # Accept the move
        pass
    else:
        # Reject the move and restore the previous conformation
        protein[x, y] *= -1

    # Cool down the system
    T *= cooling_rate

    # Store energy and temperature values for plotting
    energies.append(calculate_energy(protein))
    temperatures.append(T)

# After the simulation, you can analyze the final protein conformation
print("Final protein conformation:")
print(protein)

# Plot energy and temperature over time
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(energies)
plt.xlabel("Monte Carlo Steps")
plt.ylabel("Energy")
plt.title("Energy vs. Monte Carlo Steps")

plt.subplot(1, 2, 2)
plt.plot(temperatures)
plt.xlabel("Monte Carlo Steps")
plt.ylabel("Temperature")
plt.title("Temperature vs. Monte Carlo Steps")

plt.tight_layout()
plt.show()
