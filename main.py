import multiprocessing
import subprocess

def run_python_file(file_path):
    subprocess.run(["python", file_path])

if __name__ == "__main__":
    # List of Python files to run
    python_files = [
        r"E:\python\Pokémon Masters\Start_Command_pm.py",
        r"E:\python\Pokémon Masters\Start_Command_group.py",
        r"E:\python\Pokémon Masters\Launch.py"
    ]

    # Create a process for each Python file
    processes = []
    for file in python_files:
        process = multiprocessing.Process(target=run_python_file, args=(file,))
        processes.append(process)

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("All processes have finished.")