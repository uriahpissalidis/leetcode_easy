class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """
        items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]] 
        ruleKey = "color" 
        ruleValue = "silver"
        
        1: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
        type = index 0
        color = index 1
        name = index 2
        """
        count = 0
        if ruleKey == "type": index = 0
        if ruleKey == "color": index = 1
        if ruleKey == "name": index = 2
        for item in items:
            if item[index] == ruleValue:
                count += 1        
        return count