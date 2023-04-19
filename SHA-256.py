# +--------------------------------------------+
# |       Created by: Sean R Chappell          |
# |       For: CSC4562 - Project 2 - SHA 256   |
# |       On: April 18th, 2023                 |
# +--------------------------------------------+

import hashlib
import os
import time
import matplotlib.pyplot as plt
import numpy as np

def generate_random_message(length=64):
    return os.urandom(length)

def sha256_hash(message):
    return hashlib.sha256(message).hexdigest()

def solve_crypto_puzzle(B, n_trials=10):
    target = 2 ** (256 - B)
    total_time = 0

    for trial in range(n_trials):
        start_time = time.time()
        found = False
        while not found:
            message = generate_random_message()
            hashed_message = sha256_hash(message)
            if int(hashed_message, 16) % target == 0:
                found = True
        end_time = time.time()
        total_time += (end_time - start_time)

        print(f'Trial {trial + 1} of {n_trials} for B = {B} completed')

    average_time = total_time / n_trials
    return average_time

B_values = [4, 8, 12, 16]
average_times = [solve_crypto_puzzle(B) for B in B_values]

plt.plot(B_values, average_times, marker='o')
plt.xlabel('B')
plt.ylabel('Average Time (seconds)')
plt.title('Time Cost vs Puzzle Complexity (B)')
plt.grid(True)
plt.show()
