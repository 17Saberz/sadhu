def check_green(data):
    data_int = [int(data[0]), int(data[1]), int(data[2])]
    for value in data_int:
        if value < 0 or value > 255:
            return "Value Out of Range"
    meanRB = (data_int[0] + data_int[2]) / 2
    if data_int[1] - meanRB >= 30:
        return "Green"
    else:
        return "Not Green"

user = input("RGB: ").split(',')
print(check_green(user))
