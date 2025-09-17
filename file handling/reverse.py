def print_file_reverse(filename):
    with open(filename, 'r') as f:
        content = f.read()
        print(content[::-1])   

print_file_reverse("merged.txt")
