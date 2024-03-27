import multiprocessing
import subprocess
import sys
import os

def run_python_file(file_path):
    try:
        subprocess.run([sys.executable, file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {file_path}: {e}")
        # Log the error here if needed

if __name__ == "__main__":
    # Check if file paths are provided as command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python main.py file1.py file2.py file3.py")
        sys.exit(1)

    # Extract Python files from command-line arguments
    python_files = sys.argv[1:]

    # Create a process for each Python file
    processes = []
    for file in python_files:
        if not os.path.exists(file):
            print(f"File not found: {file}")
            continue
        process = multiprocessing.Process(target=run_python_file, args=(file,))
        processes.append(process)

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("All processes have finished.")
