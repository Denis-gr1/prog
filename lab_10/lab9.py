def line_generator(file_path, max_length):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip('n')
            if len(line) > max_length:
                yield line[:max_length]
            else:
                yield line

if __name__ == "__main__":
    file_path = 'example.txt'
    max_length = 10

    for short_line in line_generator(file_path, max_length):
        print(short_line)
