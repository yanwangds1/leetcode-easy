class Solution2(object):
    def isPalindrome(self,s):

        """
        :param s: str
        :return: bool
        """
        left, right = 0,len(s)-1
        while left<right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
            return True



class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Method #
        """
        the length of s is odd
        the middle of the character is itself
        find the indice of the middle character
        from start of the string to interate to middle  == from end of the string to iterate to midde
        """

        # Step1: need to remove all Alphanumeric characters
        import re
        regex = r'[^a-zA-Z0-9]'
        s = re.sub(regex,'',s)
        # Step2: need to remove all space in the string
        s = s.replace(' ','')
        # step3: need to convert all upper case to lower case
        s = s.lower()
        # step 4: if length of string is even, we directly return False
        if len(s) % 2 == 0 :
            return False
        middle_char = int((len(s)-1)/2)
        len_s = len(s)
        stack = []
        for i in range (0,middle_char):

            if s[i] == s[len_s-1-i]:
                stack.append(s[i])
            else:
                return False
        if len(stack)  == int((len(s)-1)/2):
            return True

##create a solution instance
solution_instance = Solution2()
##input
s = "A man, a plan, a canal: Panama"
##call isPalindrome in the instance
result = solution_instance.isPalindrome(s)
print(result)






