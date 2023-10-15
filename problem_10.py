class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if "*" in p and "." not in p:
            ...

        elif "." in p and "*" not in p:
            ...
        elif "*" in p and "." in p:
            ...
        else:
            if s != p:
                return False
            else:
                return True


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ...
