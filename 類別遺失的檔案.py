class Data:
    def __init__(self, name, pri):
        self.product_name = name
        self.price = pri
        self.number_of_sold = 0     
 
 
class Data2:
    def __init__(self, name, num):
        self.product_name = name
        self.number = num
 
class OFM: #Old_Farmer_Market
    def __init__(self):
        self.Product_list = []
        self.item_type = 0
        self.profit = 0
        self.total_item_sold = 0
 
    def __del__(self):
        print('Thanks for visiting Old Farmer Market. Wish you have a good day. Bye bye.')
 
    def business(self):
        self.Product_list = []
        self.item_type = 0
        self.profit = 0
        self.total_item_sold = 0
 
    #進行加入新產品
    def add(self,x):
        self.Product_list.append(x)
        print("Added. Product: "+x.product_name+\
              ".\nSell price: "+str(x.price))
        self.item_type+=1
    #更新產品
    def update(self, x):
        for i in range(0,self.item_type):
            if x.product_name == self.Product_list[i].product_name:
                self.Product_list[i].price=x.price
                print("Updated. Product: "+x.product_name+\
                      ".\nSell Price: "+str(x.price))
                break
 
    #賣出產品
    def sell(self,x):
        for i in range(self.item_type):
            if x.product_name==self.Product_list[i].product_name:
                self.Product_list[i].number_of_sold+=x.number
                print("Sold. Product: "+x.product_name+\
                      ".\nNumber of sold: "+str(x.number))
                self.profit += x.number * self.Product_list[i].price
                self.total_item_sold += x.number
                break
    #顯示目前賣出產品的數量和目前的總利潤
    def display(self):
        for i in range(self.item_type):
            print("Product: "+self.Product_list[i].product_name+\
                  ".\nTotal number of sold:",self.Product_list[i].number_of_sold)   
        print("Total product sold: "+str(self.total_item_sold)+"\nProfit:",self.profit)
 
if __name__=='__main__':
    Old = OFM()
    Old.business()
    print("Welcome to Old Farmer Market, what can I help you?")
 
    while True:
        s1 = input()
        na = s1.split()
        nna = ''
        
        for i in range(1, len(na)):
            nna += na[i]
            if i != len(na)-1:
                nna += ' '

        if na[0] == 'a':
            name = nna
            pri  = int(input())
            x1 = Data(name, pri)

            Old.add(x1)
        elif na[0] == 'u':
            name = nna
            pri  = int(input())
            x1 = Data(name, pri)
            Old.update(x1)
        elif na[0] == 's':
            name = nna
            num = int(input())
            x2 = Data2(name, num)
            Old.sell(x2)
        elif na[0] == 'd':
            Old.display()
        elif na[0] == 'q':
            break
    #....遺失的部分.....
    del Old