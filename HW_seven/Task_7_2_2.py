def print_operation_table(operation, num_rows = 6, num_columns = 6):
    num_columns = 1
    while num_columns <= 6:
        row =[]
        for i in range(1, num_rows + 1):
            row.append(str(operation(i, num_columns)))
        print(" ".join(map(str, row)))
        num_columns += 1
    
print_operation_table(lambda x, y: x * y) 