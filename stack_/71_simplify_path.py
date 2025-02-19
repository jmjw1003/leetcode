class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_objs = path.split("/")

        for i in path_objs:
            if not i or i == ".":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return "/" + "/".join(stack)
