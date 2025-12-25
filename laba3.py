"""with open('example.txt', 'r') as file:
     content = file.read()

 with open('example.txt', 'r') as file:
     for line in file:
         print(line)"""


def write_to_file(file_name, text):
    with open(f'{file_name}', 'w') as file:
        file.write(text)

    print('The text has been written to file')


def append_to_file(file_name, text):
    with open(f'{file_name}', 'a') as file:
        file.write(text + '\n')

    print('The text has been written to file')


def open_file(file_name):
    try:
        with open(file_name) as file:
            text = file.read()
        return print(text)
    except FileNotFoundError:
        print('File not found')
