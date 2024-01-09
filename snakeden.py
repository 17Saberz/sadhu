def convert_arrow(arrows):
    location_x = 0
    location_y = 0
    output = []
    for member in arrows:
        if member == '^':
            location_y += 1
        elif member == 'v':
            location_y += -1
        elif member == '>':
            location_x += 1
        elif member == '<':
            location_x += -1
        elif member == 'x':
            output.append("({}, {})".format(location_x, location_y))
    return output

def get_output(data):
    output = ''
    if data != []:
        for member in data:
            output += member
            output += ' '
        print("Locations: {}".format(output))
    else:
        print("Not Found")

    

path = input("Path: ")
output = convert_arrow(path)
get_output(output)

