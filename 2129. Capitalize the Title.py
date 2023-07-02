class Solution:
    def capitalizeTitle(self, title: str) -> str:

        title = title.split()
        
        ans = []

        for i in range(len(title)):
            if len(title[i]) <= 2:
                ans.append(title[i].lower())
            else:
                ans.append(title[i].capitalize())
        return " ".join(ans)
