
"""
PerformanceMeter was something I developed in about 5 minutes while
I was checking if loading a CSV was faster than loading an XLSX file.

I ended up using it for a lot of things over time. Hope it does the same for you!
"""

# Define a very inefficient test function to test:
def testFunc(string):
    for i in string:
        import time
        print(i)
        time.sleep(1)

# Wrap any operation between lines 11 and 13 to measure performance in seconds:

import time
start_time = time.time()
testFunc('So slow!') # Your function callout goes here!
print(f"Process took {(time.time() - start_time)} seconds")



