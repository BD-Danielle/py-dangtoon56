# write source to file
def with_open_write(extension, fileName, source):
    with open('{}.{}'.format(fileName, extension), 'w') as f:
        f.write(source)


def with_open_read(extenshion, fileName):
    with open('{}.{}'.format(fileName, extenshion), 'r') as f:
        return f.read()