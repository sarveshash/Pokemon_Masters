import multiprocessing
import subprocess
import sys

def run_python_file(file_name):
    file_path = f"/root/Pokemon_Masters/{file_name}.py"  # Replace this path accordingly
    subprocess.run([sys.executable, file_path])

if __name__ == "__main__":
    # List of Python files to run
    python_files = [
        "Start_Command_pm",
        "Start_Command_group",
        "Launch"
    ]

    # Create a process for each Python file
    processes = []
    for file_name in python_files:
        process = multiprocessing.Process(target=run_python_file, args=(file_name,))
        processes.append(process)

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("All processes have finished.")
