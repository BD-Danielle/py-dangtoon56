# write source to file
def with_open_write(fileName, extension, source):
    with open('{}.{}'.format(fileName, extension), 'w') as f:
        f.write(source)


def with_open_read(fileName, extension):
    with open('{}.{}'.format(fileName, extension), 'r') as f:
        return f.read()