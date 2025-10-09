import os
import subprocess

# Ищем webhook_server.py
for root, dirs, files in os.walk('.'):
    for file in files:
        if file == 'webhook_server.py':
            file_path = os.path.join(root, file)
            print(f"Found: {file_path}")
            subprocess.run(['python', file_path])
            exit(0)

print("Error: webhook_server.py not found")