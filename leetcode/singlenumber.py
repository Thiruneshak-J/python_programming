num=[3,5,3,5,2,4,4]
class solution:
    def sn(self,num):
        result=0
        for i in num:
            result ^= i
        return result
s=solution()
print(s.sn(num))