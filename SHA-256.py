#!/bin/python3

# +--------------------------------------------+
# |       Created by: Sean R Chappell          |
# |       For: CSC4562 - Project 2 - SHA 256   |
# |       On: April 18th, 2023                 |
# +--------------------------------------------+

import hashlib
import time
import random
import string
import matplotlib.pyplot as plt

# Function to generate a random message of a given length
def generate_random_message(length=32):
    # Randomly select characters from the set of ASCII letters and digits, and join them into a string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to solve the puzzle for a given number of bits (B) and a number of trials
def solve_puzzle(B, trials=1000):
    # Initialize the total time variable
    total_time = 0
    
    # Perform the specified number of trials
    for _ in range(trials):
        # Generate a random puzzle with B bits
        puzzle = format(random.randint(0, 2**B-1), f'0{B}b')
        # Record the start time of the trial
        start_time = time.time()
        
        # Continue generating random messages and checking their hashes until a solution is found
        while True:
            # Generate a random message
            message = generate_random_message()
            # Calculate the SHA-256 hash of the message
            sha256_hash = hashlib.sha256(message.encode()).hexdigest()
            # Convert the hexadecimal hash to a binary representation
            binary_hash = format(int(sha256_hash, 16), '0256b')
            
            # Check if the last B bits of the binary hash match the puzzle
            if binary_hash[-B:] == puzzle:
                # If a match is found, break out of the loop
                break
                
        # Update the total time with the time spent on the current trial
        total_time += time.time() - start_time
    
    # Calculate the average time by dividing the total time by the number of trials
    return total_time / trials

# Define a list of B values for which to test the puzzle
B_values = [4, 8, 12, 16]
# Initialize a list to store the average times for each B value
average_times = []

# Calculate the average time for each B value and store the results
for B in B_values:
    average_time = solve_puzzle(B)
    average_times.append(average_time)
    print(f"B: {B}, Average Time: {average_time}")

# Plot the average times against the B values
plt.plot(B_values, average_times)
plt.xlabel('B bits')
plt.ylabel('Average Time (seconds)')
plt.title('Average Time to Solve Crypto Puzzle vs. B')
plt.show()
