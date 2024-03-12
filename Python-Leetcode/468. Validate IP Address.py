# cook your dish here

"""
468. Validate IP Address
Medium
976
2.7K
company
Facebook
company
Amazon
company
TikTok
Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

 

Example 1:

Input: queryIP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:

Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:

Input: queryIP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
 

Constraints:

queryIP consists only of English letters, digits and the characters '.' and ':'.
"""


# class Solution:
#     def validIPAddress(self, queryIP: str) -> str:
        
#         answer = self.isIPv4(queryIP)

#         return answer




class Solution:  # Assuming your code is within a class 
    def isIPv4(self, IP) -> bool:
        try:
            ip_address = IP.split('.')
        except:
            return False
        if len(ip_address) != 4:
            return False
        for segment in ip_address:
            if segment.isdigit()==False or (int(segment)>255 or int(segment)<0) or (len(segment)>1 and int(segment[0])==0):
                return False
        return True

# Create test cases
test_cases = [
    ("172.16.254.1", True),
    ("0.0.0.0", True),
    ("255.255.255.255", True),
    ("127.0.0.1", True),
    ("10.0.0.256", False),
    ("172.16.254.", False),
    ("256.256.256.256", False),
    ("123.456.789.1011", False),
    ("192.168.0.abc", False),
    ("01.0.0.1", False)
]

# Run the tests
test_tool = Solution()  # Create an instance of your solution class
for ip, expected_result in test_cases:
    result = test_tool.isIPv4(ip)
    if expected_result!=result:
        print(f"IP: {ip}, Expected: {expected_result}, Result: {result}")
    else:print("All cases Passsed")


# aa = Solution()

# queryIP = "172.16.254.01"
# result = aa.validIPAddress(queryIP)


# print(result)