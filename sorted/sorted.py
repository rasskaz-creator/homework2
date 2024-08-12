import os

file_names = ['1.txt', '2.txt', '3.txt']

files_data = []

for file_name in file_names:
    with open(file_name, encoding='utf-8') as f:
        lines = f.readlines()
        lines_count = (len(lines))
        files_data.append((file_name, lines_count, lines))

files_data.sort(key=lambda x: x[1])

with open('final.txt', 'w', encoding='utf-8') as output_f:
    for file_name, line_count, lines in files_data:
        output_f.write(f"{file_name}\n")
        output_f.write(f"{line_count}\n")
        output_f.writelines(lines)
#print(files_data)