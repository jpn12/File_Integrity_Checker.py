import hashlib
import time
import os
from tkinter import messagebox
import pymsgbox

print("[+] FOR A BETTER EXPERIENCE PUT THE WHOLE DIRECTORY OF THE FILE")
print("[+] Dont put the file name")
files_to_monitor = []
hash_dict = {}
search_file = input("Directory of the file: ")
filename = input("filename.txt,log: ")



# this function will search for the file #
def find_files(filename, search_path):

   for root, dir, files in os.walk(search_path):
      if filename in files:
         files_to_monitor.append(os.path.join(root, filename))

find_files(filename, search_file)


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