import time

def process(line):
    # Simulate some processing
    return line.upper()

def test_without_walrus():
    start_time = time.time()
    while True:
        line = input("Enter text (without walrus): ")
        if not line:
            break
        process(line)
    end_time = time.time()
    return end_time - start_time

def test_with_walrus():
    start_time = time.time()
    while (line := input("Enter text (with walrus): ")):
        process(line)
    end_time = time.time()
    return end_time - start_time

print("Testing without walrus operator...")
time_without = test_without_walrus()
print(f"Time without walrus: {time_without:.6f} seconds")

print("\nTesting with walrus operator...")
time_with = test_with_walrus()
print(f"Time with walrus: {time_with:.6f} seconds")

print(f"\nDifference: {abs(time_with - time_without):.6f} seconds") 