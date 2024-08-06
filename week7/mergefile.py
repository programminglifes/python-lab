def merge_files(file1, file2, output_file):
    """
    Merge the contents of two files into a third file.

    Args:
        file1 (str): Path to the first file.
        file2 (str): Path to the second file.
        output_file (str): Path to the output file.
    """
    try:
        # Open the first file in read mode and the output file in write mode.
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as fo:
            # Read the contents of the first file and write them to the output file.
            fo.write(f1.read())
            # Read the contents of the second file and write them to the output file.
            fo.write(f2.read())
        print(f"Files merged successfully into {output_file}.")
    except FileNotFoundError:
        print("One of the input files does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    file1 = 'file1.txt'
    file2 = 'file2.txt'
    output_file = 'merged_file.txt'
    merge_files(file1, file2, output_file)
