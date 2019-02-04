
# coding: utf-8

# In[13]:


class Solution:
    def longestPalindrome(self, s):
        
        """
        :type s: str
        :rtype: str
        """
        
        longest_one = ""
		#start with window of size 1 to detect single character palindrome
        window=1

		#If the whole word is a palindrome
        if isPalindrome(s):
            return s

        while window < len(s):
            for i in range(len(s)):
                current = s[i: i + window]
                if isPalindrome(current):
                    if len(current) > len(longest_one):
						#Store the longest palindrome
                        longest_one = current
			#Keep increasing the window size to detect longer palindrome
            window = window + 1

        print(longest_one)
        return longest_one


def isPalindrome(s):
    return s == s[::-1]

if __name__=='__main__':
    s=Solution()
    stri='abcbad'
    s.longestPalindrome(stri)

