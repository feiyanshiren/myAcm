from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m1 = {}
        for i in range(len(list1)):
            i1 = list1[i]
            try:
                mi = list2.index(i1)
                k = mi + i
                if k in m1:
                    m1[k].append(i1)
                else:
                    m1[k] = [i1]
            except:
                pass
        d = sorted(m1.items(), key=lambda x: x[0])
        return d[0][1]

s = Solution()
print(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
print(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]))
