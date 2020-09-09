# Check the file is actually an image
# I hate python for not allowing me to camelCase the function name


def is_image(f_ext):
    if f_ext.endswith('png'):
        return True
    if f_ext.endswith('jpg'):
        return True
    if f_ext.endswith('jpeg'):
        return True
    return False
