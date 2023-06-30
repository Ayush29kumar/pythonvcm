"""import psutil
import subprocess
# Get a list of all the processes that are running.
processes = psutil.pids()

# Iterate through the list of processes.
for process in processes:

    # Get information about the process.
    info = psutil.Process(process)
    # Check if the process is running VS Code.
    if info.name() == "code":
        print(info)
        # Close the process.
        info.kill()

# Open a new instance of VS Code.
subprocess.Popen(["code"])"""

import os
import psutil


def get_vscode_instances():
    vscode_instances = []

    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'code':
            try:
                proc_info = proc.as_dict(attrs=['pid', 'cmdline'])
                pid = proc_info['pid']

                # Get the working directory (folder) of the process
                cwd = os.readlink(f'/proc/{pid}/cwd')

                vscode_instances.append({'pid': pid, 'folder': cwd})
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

    return vscode_instances


# Example usage:
instances = get_vscode_instances()

for instance in instances:
    print(f"Instance PID: {instance['pid']}")
    print(f"Instance Folder: {instance['folder']}")
    print("---")
