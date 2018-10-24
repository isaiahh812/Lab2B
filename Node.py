class Node(object):
    password = ""
    count = -1
    next = None
    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next    
    def D (x):
        dict ={}
        count =0
        temp = x
        while x:
            count = count + 1
            x= x.next
        X = []
        c = 0
        x = temp
        while c < count:
            X.append(x.password)
            temp = x.next 
            c = c+1
        for item in X:
            if item in dict:
                dict[item] = dict[item] +1
            else:
                dict[item] = 1
            return
    
    def add(self ,templ):
        count = 0
        x = Node("", 0, next)
        y = Node("", 0,next)
        while templ:
            if count < len(templ):
                G = self.check(templ[count], count)
                if G == False:
                    y = self 
                    y = y.next
                    self.password = templ[count]
                    self.count = 1
                    x = y 
                elif G == True:
                    self.count +=1
                count +=1
            else:    
                return x    
    def check(self, y, i):
        x =i
        c = self.password
        Temp = self
        if i == 0:
            return False
        while x>0:
            if c == y:
                return True
            Temp = self.next
            x = x - 1
        return False    
    def Split(head):
        slow = head
        fast = head
        if fast:
            fast = fast.next
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
        mid = slow.next
        slow.next = None
        return(head, mid)
    def remake(p):
        temp = Node("", 0, next) 
        num = 0
        while num < len(p, s):
            temp.password = p[num]
            temp.count = s[num]
            temp = temp.next
            num +=1
        return temp    

    def bubSort(x ,y):
        for i in range(len(x)):
            swapped = False
            n = 0
            while n<len(x)-1:
                if x[i+1]>x[i]:
                    x[i],x[i+1] = x[i+1],x[i]
                    y[i],x[i+1] = y[i+1],y[i]
                    swapped = True
            n = n+1
            if swapped == False:
                break
        return x ,y
    def mergeSort(leftHalf, rightHalf):
        temp = Node(None, None, None)
        while leftHalf and rightHalf:
            if leftHalf.count < rightHalf.count:
                temp.next = rightHalf
                rightHalf = rightHalf.next
            else:
                temp.next = leftHalf
                leftHalf = leftHalf.next
                temp = temp.next    
            if leftHalf == None:
                temp.next = rightHalf

            elif rightHalf == None:
                temp.next = leftHalf
        X = []
        Y = []
        while temp:
            X.append(temp.password)
            Y.append(temp.count)
            temp = temp.next
        return X, Y   
    
    
    def makeList(self):
        NG = []
        we = []
        while self:
            NG.append(self.count)
            we.append(self.password)
            self.next
        return(NG, we)    
    num = 0
    y = Node("", 0,next)
    x = Node("", 0,next)
    temp = Node("", 0, next)
    templ = []
    with open('10-million-combos.txt','r') as f:
            for word in f: 
                P = word.split()
                templ.append(P[1])
    y =  x.add(templ)    
    temp = y
    #y.D()
    left, right = y.Split()
    p = []
    s = []
    p, s = y.(mergeSort(left, right))
    while(num < 20):
        print(p[num])
        print(s[num])
        num = num + 1
    temp = remake(p,s)
    NG = []
    we = []
    NG, we = temp.makeList()
    passw,ct = bubsort(NG, we)    
    while(num < 20):
        print(passw[num])
        print(ct[num])
        num = num + 1    
    
        