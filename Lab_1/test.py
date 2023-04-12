import max_min_matrix

A_test = [
    [345.1, 261.8, 292.4, 326.4, 396.1, 307.7, 372.3],
    [260.1, 285.6, 224.4, 346.8, 280.5, 334.9, 348.5],
    [243.1, 341.7, 285.6, 249.9, 353.6, 331.5, 260.1],
    [328.1, 302.6, 275.4, 266.9, 387.6, 372.3, 212.5],
    [171.7, 358.7, 311.1, 249.9, 246.5, 307.7, 312.8],
    [236.3, 324.7, 314.5, 343.4, 404.6, 283.9, 346.8],
    [331.5, 292.4, 333.2, 234.6, 362.1, 297.5, 329.8],
    [302.6, 229.5, 302.6, 200.6, 316.2, 324.7, 331.5]
]

A_transposed_test = [
    [345.1, 260.1, 243.1, 328.1, 171.7, 236.3, 331.5, 302.6],
    [261.8, 285.6, 341.7, 302.6, 358.7, 324.7, 292.4, 229.5],
    [292.4, 224.4, 285.6, 275.4, 311.1, 314.5, 333.2, 302.6],
    [326.4, 346.8, 249.9, 266.9, 249.9, 343.4, 234.6, 200.6],
    [396.1, 280.5, 353.6, 387.6, 246.5, 404.6, 362.1, 316.2],
    [307.7, 334.9, 331.5, 372.3, 307.7, 283.9, 297.5, 324.7],
    [372.3, 348.5, 260.1, 212.5, 312.8, 346.8, 329.8, 331.5]
]

def test_max_min_matrix(A):
    return max_min_matrix.max_min_for_matrix(A)

def test_max_min_row(A):
    return max_min_matrix.max_min_row(A)

def test_max_min_columns(A_transposed):
    return max_min_matrix.max_min_columns(A_transposed)

if __name__ == "__main__":
    min_max_for_whole_matfix, range_matrix = test_max_min_matrix(A_test)
    print("Тест максимуму і мінімуму матриці", min_max_for_whole_matfix)
    print("Тест розмаху матриці", range_matrix)
    min_max_for_rows, range_row, min_max_row_range = test_max_min_row(A_test)
    print("Тест максимуму і мінімуму рядків", min_max_for_rows)
    print("Тест розмаху рядків", range_row)
    print("Тест максимуму і мінімуму розмаху рядків", min_max_row_range)
    min_max_for_columns, range_columns, min_max_columns_range = test_max_min_columns(A_transposed_test)
    print("Тест максимуму і мінімуму стовпців", min_max_for_columns)
    print("Тест розмаху стовпців", range_columns)
    print("Тест максимуму і мінімуму розмаху стовпців", min_max_columns_range)