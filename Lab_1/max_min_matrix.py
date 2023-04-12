import math
import sys
import os

A = [
    [345.1, 261.8, 292.4, 326.4, 396.1, 307.7, 372.3],
    [260.1, 285.6, 224.4, 346.8, 280.5, 334.9, 348.5],
    [243.1, 341.7, 285.6, 249.9, 353.6, 331.5, 260.1],
    [328.1, 302.6, 275.4, 266.9, 387.6, 372.3, 212.5],
    [171.7, 358.7, 311.1, 249.9, 246.5, 307.7, 312.8],
    [236.3, 324.7, 314.5, 343.4, 404.6, 283.9, 346.8],
    [331.5, 292.4, 333.2, 234.6, 362.1, 297.5, 329.8],
    [302.6, 229.5, 302.6, 200.6, 316.2, 324.7, 331.5]
]

A_transposed = [
    [345.1, 260.1, 243.1, 328.1, 171.7, 236.3, 331.5, 302.6],
    [261.8, 285.6, 341.7, 302.6, 358.7, 324.7, 292.4, 229.5],
    [292.4, 224.4, 285.6, 275.4, 311.1, 314.5, 333.2, 302.6],
    [326.4, 346.8, 249.9, 266.9, 249.9, 343.4, 234.6, 200.6],
    [396.1, 280.5, 353.6, 387.6, 246.5, 404.6, 362.1, 316.2],
    [307.7, 334.9, 331.5, 372.3, 307.7, 283.9, 297.5, 324.7],
    [372.3, 348.5, 260.1, 212.5, 312.8, 346.8, 329.8, 331.5]
]

def max_min_for_matrix(A):
    max = 0
    min = 0
    count = 0
    for row in A:
        for elem in row:
            if count == 0:
                max = elem
                min = elem
            if float(elem) > float(max):
                max = elem
            if float(elem) < float(min):
                min = elem
            count += 1
    range_matrix = float(max) - float(min)
    return {"max": max, "min": min}, range_matrix

def max_min_row(A):
    min_max_row = []
    range_row = []
    min_max_row_range = []
    for row in A:
        max = 0
        min = 0
        count = 0
        for elem in row:
            if count == 0:
                max = elem
                min = elem
            if float(elem) > float(max):
                max = elem
            if float(elem) < float(min):
                min = elem
            count += 1
        min_max_row.append({"max": max, "min": min})
        range_row.append(float(max) - float(min))
    count = 0
    for elem in range_row:
        if count == 0:
            max = elem
            min = elem
        if float(elem) > float(max):
            max = elem
        if float(elem) < float(min):
            min = elem
        count += 1
    min_max_row_range.append({"max": max, "min": min})
    return min_max_row, range_row, min_max_row_range

def max_min_columns(A_transposed):
    min_max_columns = []
    range_columns = []
    min_max_columns_range = []
    for row in A_transposed:
        max = 0
        min = 0
        count = 0
        for elem in row:
            if count == 0:
                max = elem
                min = elem
            if float(elem) > float(max):
                max = elem
            if float(elem) < float(min):
                min = elem
            count += 1
        min_max_columns.append({"max": max, "min": min})
        range_columns.append(float(max) - float(min))
    count = 0
    for elem in range_columns:
        if count == 0:
            max = elem
            min = elem
        if float(elem) > float(max):
            max = elem
        if float(elem) < float(min):
            min = elem
        count += 1
    min_max_columns_range.append({"max": max, "min": min})
    return min_max_columns, range_columns, min_max_columns_range


if __name__ == '__main__':
    min_max_for_whole_matrix, range_matrix = max_min_for_matrix(A)
    print("Максимум і мінімум матриці: ", min_max_for_whole_matrix)
    print("Розмах матриці: ", range_matrix)
    min_max_for_rows, range_row, min_max_row_range = max_min_row(A)
    print("Максимуми і мінімуми рядків: ", min_max_for_rows)
    print("Розмахи рядків: ", range_row)
    print("Максимуми і мінімуми розмахів рядків: ", min_max_row_range)
    min_max_for_columns, range_columns, min_max_columns_range = max_min_columns(A_transposed)
    print("Максимуми і мінімуми стовпців: ", min_max_for_columns)
    print("Розмахи стовпців: ", range_columns)
    print("Максимуми і мінімуми розмахів стовпців: ", min_max_columns_range)