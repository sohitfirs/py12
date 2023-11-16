# 1

class cashbox(object):
    val = 0

    def __init__(self, v):
        self.val = v
    
    def top_up(self, x):
        self.val += x
        
    def count_1000(self):
        y = self.val // 1000
        print (y)
        
    def take_away(self, x):
        self.val -= x

x = cashbox(1500)
print(x.val)
x.top_up(1000)
print(x.val)
x.count_1000()
print(x.val)
x.take_away(500)
print(x.val)
print()

# 2 

class turtle(object):
    x = 0
    y = 0
    s = 1
        
    def go_up(self):
        self.y += self.s
        print('y = ', self.y)

    def go_down(self):
        self.y -= self.s
        print('y = ', self.y)
        
    def go_left(self):
        self.x -= self.s
        print('x = ', self.x)
        
    def go_right(self):
        self.x += self.s
        print('x = ', self.x)

        
    def evolve(self):
        self.s += 1
        print('s = ', self.s)
        
    def degrade(self):
        if self.s >= 0:
            self.s -= 1
        else:
            print('ERROR')
        print('s = ', self.s)

    def count_moves(self):
        count = 0
        
        while self.x != 2:
            if self.x > 2:
                self.x -= self.s
                count += 1
            else:
                self.x += self.s
                count += 1   
                
        while self.y != 2:
            if self.y > 2:
                self.y -= self.s
                count += 1
            else:
                self.y += self.s
                count += 1
        print(count)
        
        
aaa = turtle()

aaa.evolve()
aaa.go_up()
aaa.go_down()
aaa.go_left()
aaa.go_right()
aaa.degrade()

aaa.count_moves()

input()