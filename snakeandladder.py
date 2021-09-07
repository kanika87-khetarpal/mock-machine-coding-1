from random import randint
class movement:
    count=0
    cordinates=[]
    def __init__(self,count):
        self.count=count
        self.cordinates=self.take_cordinates()
    def take_cordinates(self):
        cordinates=[]
        for i in range(0,int(self.count)):
            [i,j] = input().split(" ")
            ii=int(i)
            ij=int(j)
            cordinates.append([ii,ij])
        return cordinates
    def immediate_change(self,coin):
        for i in self.cordinates:
            if(coin == i[0]):
                coin=i[1]
class user:
    name=None
    coin=0
    dice=0
    def __init__(self,name):
        self.name=name
    def roll_dice(self):
        self.dice=randint(1,6)
        print(f"{self.name} has rolled out {self.dice}")
        self.coin+=self.dice
    
ladder_count=input()
ladder=movement(ladder_count)
print(ladder.cordinates)
snake_count=input()
snake = movement(snake_count)
print(snake.cordinates)
user1_name=input("Enter first user ")
user1=user(user1_name)
user2_name=input("Enter second user ")
user2=user(user2_name)
while(user1.coin!=100 or user2 != 100):
    user1.roll_dice()
    user2.roll_dice()
    if user1.coin == 100:
        print(f"{user1.name} wins")
        break
    if user2.coin == 100:
        print(f"{user2.name} wins")
        break






