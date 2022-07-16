import os
import sys

file_path_dir = sys.argv[1]

def read_file_handler(f):
    fd = open(f, 'r')
    return fd

file_name = 0
for fd in os.listdir(file_path_dir):
    file_path = file_path_dir + "/" + fd

    content_list = []

    file_fd = read_file_handler(file_path)
    for line in file_fd:
        content_list.append(line.strip())

    print('\t'.join([str(file_name), ' '.join(content_list)]))

    file_name += 1



#for line in sys.stdin:
    #ss = line.strip().split('\t')
