class Solution:
    def reorderSpaces(self, text: str) -> str:
        cnt=text.count(" ")
        n = text.split()
        if len(n)==1:
            return text.strip()+cnt*" "
        space,last = divmod(cnt,len(n)-1)
        return (" "*space).join(n)+" "*last