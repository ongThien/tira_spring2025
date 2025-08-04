import time

n = 10**5
l = []

start = time.time()
for i in range(1, n + 1):
    l.append(i)
end = time.time()
print("Time for addition:", round(end - start, 4), "s")

start = time.time()
while l:
    l.pop(0)
end = time.time()
print("Time for deletions:", round(end - start, 4), "s")
