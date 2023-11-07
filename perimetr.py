class point:
    def __init__(self, x: int, left: bool):
        self.x = x
        self.left = left
    
    def __str__(self):
        return str(self.x)

def klumby():
    with open('input.txt') as input:
        n = int(input.readline())
        M = []
        for i in range(n):
            x,y = ([int(a) for a in input.readline().split()])
            M.extend([point(x,left=True),point(y,left=False)])
        M.sort(key=lambda a: a.x)
        BR = 1
        left = M[0]
        for i in range(1,2*n-1):
            if M[i].left:
                BR +=1
            else:
                BR -=1
            if BR == 0 and M[i].x!=M[i+1].x:
                print(left.x, M[i].x)
                left = M[i+1]
        print(left,M[2*n-1].x)
        
        return None

if __name__=="__main__":
    klumby()