# Module to calculate the hypotenuse of a 
# right angled triangle

# Function to check input is float/integer
# Throw error if not

# Function to add two numbers together
# input: floats or int or list/array of ints/floats
def add_nums(a, b):
    """Add two number together

    Args:
        a (float, int, array): A number to add
        b (float, int, array): A number to add

    Returns:
        float, int, array: The sum of a and b
    """
    sum_of_numbers = a + b 
    return sum_of_numbers


# Function to calculate the square of a number
# input: floats or int or list/array of ints/floats
def square_number(a):
    """Return the square of a number

    Args:
        a (float, int, array): Number(s) to be squared

    Returns:
        float, int, array: Squared Number
    """
    squared = a ** 2
    return squared
# Function to calculate the square root of a number
# input: floats or int or list/array of ints/floats
def square_root(a):
    """Calculate square root 

    Args:
        a (float, int, array): Number whose square root is needed

    Returns:
        float, int, array: Square root of a
    """
    sqrt_num = a ** 0.5
    return sqrt_num


# Function to calculate the hypotenuse using all the above
# a^2 + b^2 = c^2
# c = sqrt(a^2 + b^2)
# input: floats or int or list/array of ints/floats

def calc_hypot(opp, adj):
    """Calculate the length of the hypotenuse of a Right angled triangle

    Args:
        opp (float, int, array): Length of opposite side
        adj (float, int, array): Length of adjacent side

    Returns:
        float, int, array: Length of hypotenuse
    """
    #opposite and adjacent
    opp_sqrd = square_number(opp)
    adj_sqrd = square_number(adj)
    summed_nums = add_nums(opp_sqrd, adj_sqrd)
    hypotenuse = square_root(summed_nums)
    return hypotenuse
    
