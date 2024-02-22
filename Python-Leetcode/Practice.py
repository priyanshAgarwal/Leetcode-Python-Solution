def longestPalindrome(s):
    """
    Returns the longest palindromic substring in a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring in s.
    """
    
    # Initialize an empty string to store the longest palindrome.
    longest = ""
    
    # Iterate over the string, starting from the second character.
    for i in range(1, len(s)):
        # Check for odd-length palindromes centered at i.
        odd = expandAroundCenter(s, i, i)
        if len(odd) > len(longest):
            longest = odd
        
        # Check for even-length palindromes centered at i and i-1.
        even = expandAroundCenter(s, i - 1, i)
        if len(even) > len(longest):
            longest = even
        
    return longest

def expandAroundCenter(s, left, right):
    """
    Expands a palindrome around a given center and returns the longest substring.

    Args:
        s: The input string.
        left: The left index of the center.
        right: The right index of the center.

    Returns:
        The longest palindromic substring centered at (left, right).
    """
    
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    return s[left + 1:right]

# Example usage
s = "babad"
longest_palindrome = longestPalindrome(s)
print(f"The longest palindromic substring in '{s}' is: {longest_palindrome}")

s = "cbbd"
longest_palindrome = longestPalindrome(s)
print(f"The longest palindromic substring in '{s}' is: {longest_palindrome}")
