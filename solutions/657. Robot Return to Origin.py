class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # 4n solution
        cntU = moves.count("U")
        cntD = moves.count("D")
        cntR = moves.count("R")
        cntL = moves.count("L")
        if cntU == cntD and cntR == cntL:
            return True
        else:
            return False