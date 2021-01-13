def minOperations(self, logs: List[str]) -> int:
    ret = 0
    for i in logs:
        if i == '../':
            ret -= 1
            ret = max(0, ret)
        elif i == './':
            continue
        else:
            ret += 1
    return ret