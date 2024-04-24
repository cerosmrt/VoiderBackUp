import os
import random

def get_random_line(file_path, encoding='utf-8'):
  try:
    with open(file_path, 'r', encoding=encoding) as file:
      lines = file.readlines()
      valid_lines = [line.rstrip() for line in lines if line and line != '.']
      return random.choice(valid_lines) if valid_lines else None
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    return None

void_dir = os.path.join(os.getcwd(), 'void')
os.makedirs(void_dir, exist_ok=True)

# Look for .txt files in the 'void' subdirectory
txt_files = [f for f in os.listdir(void_dir) if f.endswith('.txt')]

if not txt_files:
  print("No .txt files found in the 'void' subdirectory.")
else:
  while txt_files:
    random_file = random.choice(txt_files)
    file_path = os.path.join(void_dir, random_file)
    void_file_path = os.path.join(void_dir, '0.txt')  # Path for the new file
    while True:
      random_line = get_random_line(file_path)
      if random_line:
        print(random_line)
        key_pressed = input("Press Enter to try another line, 's' to stamp, or Ctrl+C to quit: ")
        if key_pressed == 's':
          with open(void_file_path, 'a', encoding='utf-8') as void_file:
            void_file.write(random_line + '\n')
          print(f"Line stamped to '{void_file_path}'.")
      else:
        print("No valid lines found in the current file. Moving to the next file.")
        txt_files.remove(random_file)  # Remove the current file from the list
        break  # Break the inner loop to select another file