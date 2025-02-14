from threading import Thread, current_thread

# Alice and Bob will both run n laps
n=10
# Total number of laps
laps=0

# Function executed by both Alice and Bob threads
def runlaps():
    global laps
    name = current_thread().name    # Is this Alice or Bob?
    for _ in range(n):
        # Which lap is starting?
        mylap = laps+1
        print(name + " starting lap: " + str(mylap))
        # Store the lap number that was finished
        laps = mylap
        print(name + " finished lap: " + str(laps))

# Create the threads for Alice and Bob
alice_thread = Thread(target=runlaps, name="Alice")
bob_thread = Thread(target=runlaps, name="Bob")

# Start the threads
alice_thread.start()
bob_thread.start()

# Wait for Alice and Bob threads to finish
alice_thread.join()
bob_thread.join()

# Print the total number of laps
print("Total laps: " + str(laps))
