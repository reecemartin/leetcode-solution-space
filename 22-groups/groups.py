class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        placed = False
        for i in range(len(groupSizes)):
            if groupSizes[i] == 1:
                result.append([i])
            else:
                print("active")
                for group in result:
                    print("    active")
                    print(groupSizes[group[0]])
                    if len(group) < groupSizes[group[0]] and groupSizes[i] == groupSizes[group[0]]:
                        print(".       active")
                        group.append(i)
                        placed = True
                        break
                if not placed:
                    result.append([i])
                placed = False
        return result
