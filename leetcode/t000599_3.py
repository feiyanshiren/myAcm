from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m11 = {}
        m2 = {}
        for i in range(len(list1)):
            m11[list1[i]] = i
        for i in range(len(list2)):
            i1 = list2[i]
            if i1 in m11:
                k = i + m11[i1]
                a = list(m2.keys())
                if a:
                    mi = a[0]
                    if mi < k:
                        continue
                    elif mi > k:
                        del m2[mi]
                        m2[k] = [i1]
                    else:
                        m2[k].append(i1)
                else:
                    m2[k] = [i1]
        return (list(m2.values())[0])
            

s = Solution()
print(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
print(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]))

