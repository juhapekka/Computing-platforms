import threading

# Keep track of currently reading threads
readers=set()
# Keep track of currently writing threads
writers=set()
# Keep track of the number of readers waiting to read
waitingreaders=0
# Keep track of the number of writers waiting to write
waitingwriters=0
# Lock for protecting the shared variables
lock = threading.Lock()
# Condition variable where readers wait for their turn to read
oktoread = threading.Condition(lock)
# Condition variable where writers wait for their turn to write
oktowrite = threading.Condition(lock)

# Function executed by the readers
def reader():
    global readers
    global writers
    global waitingreaders
    global waitingwriters
    # Retrieve the name of this thread
    name = threading.current_thread().name
    # Each reader will read three times
    for _ in range(3):
        lock.acquire()
        # If there are currently writers, a reader needs to wait
        while len(writers) > 0:
            waitingreaders += 1
            oktoread.wait()
            waitingreaders -= 1
        # Now there are no writers, so a reader can read
        readers.add(name)
        print(name + ": Starts reading")
        print("Current readers: " + str(readers) + " Current writers: " + str(writers))
        lock.release()
        print(name + ": Reading...")
        lock.acquire()
        print(name + ": Finishes reading")
        readers.remove(name)
        # If there are no readers left, let the writers start writing
        if len(readers) == 0:
            oktowrite.notify()
        lock.release()

# Function executed by the writers
def writer():
    global readers
    global writers
    global waitingreaders
    global waitingwriters
    # Retrieve the name of this thread
    name = threading.current_thread().name
    # Each writer writes three times
    for _ in range(3):
        lock.acquire()
        # Readers have priority so a writer waits if there are readers/writers currently reading/writing or if there are waiting readrrs
        while len(writers) + len(readers) + waitingreaders > 0:
            waitingwriters += 1
            oktowrite.wait()
            waitingwriters -= 1
        # Now there are no current readers/writers or waiting readers
        writers.add(name)
        print(name + ": Starts writing")
        print("Current readers: " + str(readers) + " Current writers: " + str(writers))
        lock.release()
        print(name + ": Writing...")    
        lock.acquire()
        print(name + ": Finishes writing")
        writers.remove(name)
        # If there is waiting readers, wake them up first as they have priority, otherwise wake up the next writer
        if waitingreaders > 0:
            oktoread.notify_all()
        elif waitingwriters > 0:
            oktowrite.notify()
        lock.release()

# Create the reader and writer threads
readerThreads = [threading.Thread(target=reader, name = "R" + str(i)) for i in range(10)]
writerThreads = [threading.Thread(target=writer, name = "W" + str(i)) for i in range(10)]

# Start the reader and writer threads
for i in range(10):
    readerThreads[i].start()
    writerThreads[i].start()
