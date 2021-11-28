class Solution:
    def __init__(self) -> None:
        pass

    def predictPartyVictory(self, senate: str) -> str:
        queue_radiant, queue_dire = [], []
        max_int = 99999
        for index, char in enumerate(senate):
            if char == "R":
                queue_radiant.append(index)
            else:
                queue_dire.append(index)

        while queue_dire and queue_radiant:
            index_dire = queue_dire.pop(0)
            index_radiant = queue_radiant.pop(0)
            if index_dire < index_radiant:
                queue_dire.append(index_dire+max_int)
            else:
                queue_radiant.append(index_radiant+max_int)
        if queue_dire:
            return "Dire"
        else:
            return "Radiant"


rotasenete = Solution()
print(rotasenete.predictPartyVictory("RD"))
print(rotasenete.predictPartyVictory("RDD"))
