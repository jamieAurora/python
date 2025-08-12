tableData = [['apples','oranges','cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for y in tableData[i]:
            variable = len(y)
            if variable > colWidths[i]:
                colWidths[i] = variable

    for i in range(len(tableData[i])):
        for y in range(len(tableData)):
            print((tableData[y][i]).rjust(colWidths[y]), end = ' ')
        print()
printTable(tableData)