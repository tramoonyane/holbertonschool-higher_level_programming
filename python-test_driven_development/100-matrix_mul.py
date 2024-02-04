#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    # Validate m_a and m_b
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Validate elements in m_a and m_b
    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_b should contain only integers or floats")

    # Validate row sizes
    if len(set(len(row) for row in m_a)) > 1 or len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Validate matrix multiplication compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result


if __name__ == "__main__":
    # Test cases
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    assert matrix_mul(matrix_a, matrix_b) == [[19, 22], [43, 50]]

    try:
        matrix_mul(123, matrix_b)
    except TypeError as e:
        assert str(e) == "m_a must be a list or m_b must be a list"

    try:
        matrix_mul(matrix_a, [1, 2, 3])
    except TypeError as e:
        assert str(e) == "m_b must be a list of lists"

    try:
        matrix_mul([], matrix_b)
    except ValueError as e:
        assert str(e) == "m_a can't be empty"

    try:
        matrix_mul([[1, 'a'], [3, 4]], matrix_b)
    except TypeError as e:
        assert str(e) == "m_a should contain only integers or floats"

    try:
        matrix_mul([[1, 2], [3, 4, 5]], matrix_b)
    except TypeError as e:
        assert str(e) == "each row of m_a must be of the same size"

    try:
        matrix_mul([[1, 2], [3, 4]], [[1, 2, 3], [4, 5, 6]])
    except ValueError as e:
        assert str(e) == "m_a and m_b can't be multiplied"
