def merge_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        out.write(f1.read())
        out.write("\n")   
        out.write(f2.read())

    with open(output_file, 'r') as out:
        print("\n--- Merged File Content ---")
        print(out.read())

merge_files("file1.txt", "file2.txt", "merged.txt")
