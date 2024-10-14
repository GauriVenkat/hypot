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