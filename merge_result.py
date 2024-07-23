import os
import json
import sys

def merge_json_files(date_str):
    base_dir = f'results-{date_str}'
    speed_file_path = os.path.join(base_dir, 'speed', 'reports', 'speed.json')
    memory_file_path = os.path.join(base_dir, 'memory', 'reports', 'memory.json')
    result_file_path = os.path.join(base_dir, 'result.json')
    
    # Ensure the files exist
    if not os.path.exists(speed_file_path):
        print(f"Speed file not found: {speed_file_path}")
        return
    if not os.path.exists(memory_file_path):
        print(f"Memory file not found: {memory_file_path}")
        return

    # Read the speed data
    with open(speed_file_path, 'r') as speed_file:
        speed_data = json.load(speed_file)

    # Read the memory data
    with open(memory_file_path, 'r') as memory_file:
        memory_data = json.load(memory_file)

    # Merge the data
    result_data = {
        'speed': speed_data,
        'memory': memory_data
    }

    # Save the merged data
    with open(result_file_path, 'w') as result_file:
        json.dump(result_data, result_file, indent=4)

    print(f"Merged data saved to {result_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python merge_json.py <date>")
        print("Example: python merge_json.py 20230102")
    else:
        date_str = sys.argv[1]
        merge_json_files(date_str)