class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        wordDict = {}
        maxOccurences = 0
        maxKey = ""        
        for punc in "!?',;.":
            paragraph = paragraph.replace(punc , " ")
        words = paragraph.split()
        for word in words: 
            word = word.lower()
            if word not in banned: 
                if word in wordDict: 
                    wordDict[word] += 1
                else: 
                    wordDict[word] = 1
                if wordDict[word] > maxOccurences: 
                    maxOccurences = wordDict[word]
                    maxKey = word
        return maxKey