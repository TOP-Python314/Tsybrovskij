def check_copy_file(n):
    files = []
    current_file = ''
    in_file = False
    
    for symb in n:
        if symb == ';':
            if in_file:
                files.append(current_file.strip())
                current_file = ''
                in_file = False
        else:
            current_file += symb
            in_file = True
    if current_file:
        files.append(current_file.strip())
    
    file_count = {}
    result_list = []
    
    for file in files:
        if file in file_count:
            file_count[file] += 1
            base_name, ext = file.split('.', 1) if '.' in file else (file, '')
            new_file_name = f'{base_name}_{file_count[file]}.{ext}' if ext else f'{base_name}_{file_count[file]}'
            result_list.append(new_file_name)
        else:
            file_count[file] = 1
            result_list.append(file)
    
    result_list.sort()
    return result_list

naims_files = input().strip()
result = check_copy_file(naims_files)
print("\n".join(result))

'''
Пример:
1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz

1.py
1_2.py
1_3.py
aux.h
functions.h
main.cpp
main_2.cpp
main_3.cpp
src.tar.gz
src_2.tar.gz
'''