from threading import Thread, current_thread

# An object representing a one-lane bridge
class Bridge():    
    def __init__(self):
        # Keep track of cars currently on the bridge
        # Add here the variables, locks and condition variables needed for synchronization
        self.cars = set()

    # A car wishing to cross the bridge westbound will call this when entering the bridge
    def enter_west(self, name):
        # Add code here to synchronize the cars on the bridge properly
        self.cars.add(name)
        print("Cars on the bridge: " + str(self.cars))
        return
        
    # A car wishing to cross the bridge westbound will call this when exiting the bridge
    def exit_west(self, name):
        # Add code here to synchronize the cars on the bridge properly
        self.cars.remove(name)
        print("Cars on the bridge: " + str(self.cars))
        return

    # A car wishing to cross the bridge eastbound will call this when entering the bridge
    def enter_east(self, name):
        # Add code here to synchronize the cars on the bridge properly
        self.cars.add(name)
        print("Cars on the bridge: " + str(self.cars))
        return

    # A car wishing to cross the bridge eastbound will call this when exiting the bridge
    def exit_east(self, name):
        # Add code here to synchronize the cars on the bridge properly
        self.cars.remove(name)
        print("Cars on the bridge: " + str(self.cars))
        return

        
# A car driving westbound over the bridge
def drive_westbound(bridge):
    name = current_thread().name
    print(name + ": Driving westbound...")
    bridge.enter_west(name)
    print(name + ": Westbound on the bridge")
    bridge.exit_west(name)
    print(name + ": Crossed the bridge westbound")

# A car driving eastbound over the bridge
def drive_eastbound(bridge):
    name = current_thread().name
    print(name + ": Driving eastbound...")
    bridge.enter_east(name)
    print(name + ": Eastbound on the bridge")
    bridge.exit_east(name)
    print(name + ": Crossed the bridge eastbound")

# Initialize the bridge and the car threads
bridge = Bridge()
Twest = [Thread(target=drive_westbound, kwargs={"bridge": bridge}, name = "W" + str(i)) for i in range(10)]
Teast = [Thread(target=drive_eastbound, kwargs={"bridge": bridge}, name = "E" + str(i)) for i in range(10)]

# Start the car threads
for i in range(10):
    Twest[i].start()
    Teast[i].start()
