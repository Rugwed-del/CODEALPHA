import string
import itertools
import time

# Dummy password (Target)
target_password = input("Set a password for simulation: ")


characters = string.ascii_lowercase
attempts = 0

print("Starting Brute Force Attack Simulation...\n")

start_time = time.time()

for length in range(1, 4):
    for guess in itertools.product(characters, repeat=length):
        attempts += 1
        guess_password = ''.join(guess)
        print("Trying:", guess_password)

        if guess_password == target_password:
            end_time = time.time()
            print("\nPassword Found:", guess_password)
            print("Total Attempts:", attempts)
            print("Time Taken:", round(end_time - start_time, 2), "seconds")
            exit()

print("Password not found.")
