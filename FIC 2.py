import hashlib
import time
import os
from tkinter import messagebox
import pymsgbox

files_to_monitor = [""] # Directory of the file#
hash_dict = {}



# Get files Hash #
def get_file_hash(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def hashes():
    for file in files_to_monitor:
        hash_dict[file] = get_file_hash(file)


# Checks file integrity #
print("[+] Checking Files Integrity")
def check_integrity():
    for file, initial_hash in hash_dict.items():
        if not os.path.exists(file):
            print(f"{file} not found!")
            continue
        current_hash = get_file_hash(file)
        if current_hash != initial_hash:
            messagebox.showwarning(message="A change has been detected")
            pymsgbox.alert(f'A Change Has Been Detected. File: {file}', title="Alert")


hashes()

while True:
    check_integrity()
    time.sleep(4000)  # time for the program to check the files #