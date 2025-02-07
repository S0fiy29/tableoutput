import csv

#Import Table 1
with open('Table_Input.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    table1 = {row[0]: int(row[1]) for row in reader}

#Calculate the values
alpha = table1['A5'] + table1['A20']
beta = table1['A15'] / table1['A7']
charlie = table1['A13'] * table1['A12']

#Table 2
table2 = [
    ["Category", "Value"],
    ["Alpha", alpha],
    ["Beta", beta],
    ["Charlie", charlie]
]

#Generate the HTML file
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Table Display</title>
    <style>
        table {{
            width: 50%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }}
        table, th, td {{
            border: 1px solid black;
        }}
        th, td {{
            padding: 10px;
            text-align: left;
        }}
    </style>
</head>
<body>

<h1>Table Display</h1>

<!-- Display Table 1 -->
<h2>Table 1</h2>
<table>
    <tr><th>Index</th><th>Value</th></tr>
    {"".join(f"<tr><td>{index}</td><td>{value}</td></tr>" for index, value in table1.items())}
</table>

<!-- Display Table 2 -->
<h2>Table 2</h2>
<table>
    {"".join(f"<tr><td>{row[0]}</td><td>{row[1]}</td></tr>" for row in table2)}
</table>

</body>
</html>
'''

#Write HTML content to a file
with open('index.html', 'w') as html_file:
    html_file.write(html_content)

print("HTML file generated successfully.")
