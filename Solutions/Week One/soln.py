#This file contains the functions you will need to implement for Drill 1 of DSGT Bootcamp

def cube(n):
    """
    Given a number n, return the cube of the number. For example, cube(4) = 64
    """
    #YOUR CODE HERE
    return n*n*n

def factorial(n):
    """
    Given a number n, return n!. Make sure to handle the relevant edge cases
    """
    #YOUR CODE HERE
    if (int(n) != n):
        raise ValueError("You can take factorial of integers only")
    if (n < 0):
        raise ValueError("You can't take factorial of negative integers")
    result = 1
    for i in range(1, n+1):
        result = result*i
    return result

def count_digits(n):
    """
    Given a non-negative integer, return the number of digits
    """
    #YOUR CODE HERE
    ctr = 0
    if (n == 0):
        return 1
    while (n != 0):
        ctr += 1
        n = n // 10
    return ctr

def average_grade(scores, targetGrade):
    """
      Given a set of exam scores as such: {"Exam 1": 43, "Exam 2": 59, "Exam 3": 60, "Exam 4": 90}
  
      Find how much the student will need to score on the final exam to acheive the target grade. Assume that all exams (including the final exam) are weighted equally
      for the sake of simplicity.

      In the above example, if the student wants to have a target grade of 70, the student will need to score a 98 on the final (70* 5 exams = 43+59+60+90 + X. Solve the equation for X)

      Assume that scores will always be a nonempty dictionary
    """
    #YOUR CODE HERE
    targetTotal = targetGrade*(len(scores.keys()) + 1)
    currSum = 0
    for k in scores.keys():
        currSum += scores[k]
    return targetTotal - currSum

def slice_product(numList, start_pos, end_pos):
    """
    Given a list of numbers, a start index, and end index, find the product of the entries in the given slice. Below is an example

    Suppose that the list is [1,2,3,4,5], start_pos = 1, end_pos = 3, then slice_product should return 24 (lists are zero-indexed in the sense that the first element in the list is at index 0, so 2*3*4 = 24)

    If the start_pos is a negative number, raise/throw a ValueError with an informative reason. If the end_pos is an integer that is at least the length of the list, raise/throw a ValueError (eg: in the above array, if end_pos >= 5, raise a ValueError.)

    If the end_pos is smaller than the start_pos, raise/throw a ValueError as well. The start_pos and end_pos are guaranteed to be integers.
    """
    #YOUR CODE HERE
    if (start_pos < 0):
        raise ValueError("Start position can't be negative")
    elif (end_pos >= len(numList)):
        raise ValueError("End position is at least the length of the list")
    elif (end_pos < start_pos):
        raise ValueError("End position must be larger than the start position")
    product = 1
    for i in range(start_pos, end_pos + 1):
        product = product*numList[i]
    return product
    #raise NotImplementedError("Did not implement slice_product function")

def encrypt(message, shift):
    """
    This function is responsible for encrypting a message using Caesar Cipher. The Caesar Cipher is basically shifting the alphabet. For example, if the shift is 2, then a becomes c, b becomes d and so on.
    If the shift is 1, then a becomes b, b becomes c and so on.

    Helpful Link to understand Caesar Cipher: https://medium.com/blockgeeks-blog/cryptography-for-dummies-part-2-the-caesar-cipher-665106afac78

    If the shift value is negative, you will need to perform a manipulation to find an equivalent shift value (for example if shift was -27, the equivalent shift value that's positive is 25)

    (Hint: For the shift value case, think mathematically how the Cipher works)

    Caesar Cipher is case insensitive!!! ("J" shifted by 3 should be treated the same as "j" shifted by 3 for example). How can you use this property to simplify your solution?
    """
    #YOUR CODE HERE
    cipher = ''
    for char in message:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher

def decrypt(message, shift):
    """
    Same rules as encrypt, but decrypt the message
    """
    #YOUR CODE HERE
    result = ""
    s = 26 - shift
    # traverse text
    for i in range(len(message)):
        char = message[i]
        if (char == ' '):
            result += char
            continue
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
