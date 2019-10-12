class Solution:
    def findRadius(self, houses, heaters) -> int:
        ## 去重且降低时间复杂度
        houses = set(houses)
        heaters = set(heaters)
        houses_heaters = list(houses.union(heaters))
        houses_heaters.sort()
        house = [] #房屋列表
        ans = [0]
        last_heaters = 0
        for k, v in enumerate(houses_heaters):
            if v in heaters:
                if house:
                    # 有上供暖
                    if last_heaters:
                        ans.append(
                            max(map(lambda x: min(x - last_heaters, v - x), house)))
                    else:
                        # 没有上供暖
                        ans.append(v - house[0])
                #已经计算的房屋清空,并更新上供暖
                house = []
                last_heaters = v
            else:
                house.append(v)
        if house:
            # 剩余的房屋
            ans.append(house[-1] - last_heaters)
        return max(ans)