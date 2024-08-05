class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # First pass: count occurrences of each element
        count = {}
        for item in arr:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1

        # Second pass: collect distinct elements
        distinct_elements = []
        for item in arr:
            if count[item] == 1:
                distinct_elements.append(item)
                
        # Return the k-th distinct element if it exists
        if k <= len(distinct_elements):
            return distinct_elements[k - 1]
        else:
            return ""
