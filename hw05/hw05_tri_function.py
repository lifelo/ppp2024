pip install tabulate
table = [['각', '라디안', 'sin', 'cos', 'tan'], ['0', '0.0000', '0.0000', '1.0000', '0.0000'], ['1', '0.0175', '0.0000', '0.9998', '0.0000'], ['2', '0.0349', '0,.0000', '0.9994', '0.0000'], ['3', '0.0524', '0.0523', '0.9986', '0.0524'], ['4', '0.0698', '0.0000', '0.9976', '0.0699'], ['5', '0.0873', '0.0872', '0.9962', '0.0875'], ['6', '0.1047', '0.1045', '0.9945', '0.1051'], ['7', '0.1222', '0.1219', '0.9925', '0.1228'], ['8', '0.1396', '0.1392', '0.9903', '0.1405'], ['9', '0.1571', '0.1564', '0.9877', '0.1584'], ['10', '0.1745', '0.1736', '0.9848', '0.1763']]
print(tabulate(table))


