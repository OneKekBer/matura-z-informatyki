def get_data():
    with open("./../data/owoce.txt", "r") as f:
        content = f.read().strip()
        data = content.split("\n")[1:] 
        return data

data = get_data()

month_sums = {
    5: [0, 0, 0],
    6: [0, 0, 0],
    7: [0, 0, 0],
    8: [0, 0, 0],
    9: [0, 0, 0]
}

for line in data:
    line_data = line.split("\t")
    date = line_data[0].split(".")
    month = int(date[1])
    
    month_sums[month][0] += int(line_data[1])
    month_sums[month][1] += int(line_data[2])
    month_sums[month][2] += int(line_data[3])

print(month_sums)
