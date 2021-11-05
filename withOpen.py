# write source to file
def with_open_write(fileName, extension, mode, source):
    with open('{}.{}'.format(fileName, extension), mode) as f:
        return f.write(source)


def with_open_read(fileName, extension):
    with open('{}.{}'.format(fileName, extension), 'r') as f:
        return f.read()
