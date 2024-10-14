import hypot.pythag
import numpy as np

def test_add_nums():
    '''Tests the function that adds two numbers'''

    # Arrange
    test_variable_a = 3
    test_variable_b = 4
    expected_output = 7

    # Act
    output = hypot.pythag.add_nums(test_variable_a, test_variable_b)

    # Assert
    assert output == expected_output
    
def test_add_nums_arrays():
    '''Tests the function that adds two arrays'''

    # Arrange
    test_array_a = np.array([2, 5.7, 8])
    test_array_b = np.array([1.0, 1.0, 1.0])
    expected_output = np.array([3, 6.7, 9])

    # Act
    output = hypot.pythag.add_nums(test_array_a, test_array_b)

    # Assert
    assert np.allclose(expected_output, output)

    # No cleanup needed
    
def test_square_number():
    '''Tests the function that squares a number'''

    # Arrange
    test_variable_1 = 7
    expected_output = 49

    # Act
    output = hypot.pythag.square_number(test_variable_1)

    # Assert
    assert output == expected_output

def test_square_array():
    '''Tests the function that squares arrays'''

    # Arrange
    test_array_1 = np.array([1, 4, 5])
    expected_output = np.array([1, 16, 25])

    # Act
    output = hypot.pythag.square_number(test_array_1)

    # Assert
    assert np.allclose(expected_output, output)
    
def test_square_root():
    '''Tests for the square root function'''

    # Arrange
    test_variable_1 = 16
    expected_output = 4

    # Act
    output = hypot.pythag.square_root(test_variable_1)

    # Assert
    assert output == expected_output
    
def test_square_root_array():
    '''Tests for the square root function for an array'''

    # Arrange
    test_array_1 = np.array([16, 9, 64])
    expected_output = np.array([4, 3, 8])

    # Act
    output = hypot.pythag.square_root(test_array_1)

    # Assert
    assert np.allclose(expected_output, output)
    
def test_square_root_2():
    '''Tests for the square root function'''

    # Arrange
    test_variable_1 = 16
    expected_output = np.sqrt(16)

    # Act
    output = hypot.pythag.square_root(test_variable_1)

    # Assert
    assert output == expected_output
    
def test_calc_hypot():
    """Integration for hypot
    """
    # Arrange
    test_variable_1 = 5.6
    test_variable_2 = 7.8
    expected_output = 9.60208

    # Act
    output = hypot.pythag.calc_hypot(test_variable_1, test_variable_2)

    # Assert
    assert np.allclose(expected_output, output, atol = 1e-3)
    
def test_calc_hypot():
    """Integration for hypot
    """
    # Arrange
    test_variable_1 = np.array([10, 30045, 6.9, 0.04])
    test_variable_2 = np.array([23, 2400, 8.9, 0.34])
    expected_output = np.array([25.08, 30140.7, 11.26, 0.34])

    # Act
    output = hypot.pythag.calc_hypot(test_variable_1, test_variable_2)

    # Assert
    assert np.allclose(expected_output, output, rtol= 1e-1)
