import os

def generate_train_list(directory, output_file):
    with open(output_file, 'w') as f:
        for root, _, files in os.walk(directory):
            for file in files:
                # Add file paths to train.list (e.g., only .jpg or .png files)
                if file.endswith(('.jpg', '.png', '.txt')):  # Adjust extensions as needed
                    relative_path = os.path.relpath(os.path.join(root, file), directory)
                    f.write(relative_path + '\n')

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(current_directory, 'train.list')
    generate_train_list(current_directory, output_file)
    print(f"'train.list' has been created in {current_directory}")
