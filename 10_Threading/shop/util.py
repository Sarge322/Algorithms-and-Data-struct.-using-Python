def file_reader(file_name):
    with open(file_name, 'r') as lines:
        ls1 = []
        for i in lines.readlines():
            temp = i.strip().split(' ')
            if len(temp) == 2:
                ls1.append([temp[0], temp[1]])
            elif len(temp) == 1:
                ls1.append(temp[0])
    return ls1
