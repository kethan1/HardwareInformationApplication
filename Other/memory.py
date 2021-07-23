#!/usr/bin/env python
import psutil
import os

print(psutil.virtual_memory())
print('Total Memory (in Bytes):', psutil.virtual_memory().total)
print('Memory Used (in Bytes):', psutil.virtual_memory().used)
print('Memory Available (in Bytes):', psutil.virtual_memory().available)

# [[n * "1" for n in range(2000)] for _ in range(2000)]  # should see a spike in memory usage when uncommented

pid = os.getpid()
python_process = psutil.Process(pid)
print(python_process)
print(python_process.memory_info())
memoryUse = python_process.memory_info()[0] / 2 ** 30
print(f'Memory Used: {memoryUse}')
