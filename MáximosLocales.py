with open("EstrellaEspectro.txt", "r") as ee:
    lines = ee.read().split("\n")
    for line in lines:
        line = lines.split("  ")
    print(lines)