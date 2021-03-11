class Data:
    def __init__(self, name, num):
        self.scientific_name = name
        self.number = num

class Animal:
    def __init__(self):
        self.Animal_list = []
        self.type = 0
        self.Endanger_number = 0
        self.Endanger_list = []
    def __del__(self):
        print('That are the endanger animal list we have now. Bye bye.')

    def start(self):
        self.Animal_list = []
        self.type = 0
        self.Endanger_number = 0
        self.Endanger_list = []
    def add(self, x):
        self.Animal_list.append(x)
        print("Add. Animal: "+x.scientific_name+\
              ".\nNumber: "+str(x.number))
        self.type+=1
        if x.number < 1000:
            self.Endanger_number += 1
            self.Endanger_list.append(x)
            print('Endanger species: Yes')
        else:
            print('Endanger species: No')
    def update(self, x):
        count = 0
        for i in range(0,self.type):
            if x.scientific_name == self.Animal_list[i].scientific_name:
                self.Animal_list[i].number=x.number
                print("Update. Animal: "+x.scientific_name+\
                      ".\nNumber: "+str(x.number))
                break

        if x.number < 1000:
            print('Endanger species: Yes')
            for i in range(len(self.Endanger_list)):
                if x.scientific_name == self.Endanger_list[i].scientific_name:
                    count += 1
                else:
                    count += 0
            if count == 0:
                self.Endanger_number += 1
                self.Endanger_list.append(x)
        else:
            print('Endanger species: No')
        for x in self.Endanger_list:
            if x.number > 1000:
                self.Endanger_list.remove(x)
                self.Endanger_number -= 1
                break
    def display(self):
        print('There are', self.Endanger_number, 'animals who are endanger species')
        for i in self.Animal_list:
            if i.number < 1000:
                print('Animal:', i.scientific_name + '.')
                print('Number:', i.number)

if __name__=='__main__':
    Am = Animal()
    Am.start()
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
            num  = int(input())
            x1 = Data(name, num)

            Am.add(x1)
        elif na[0] == 'u':
            name = nna
            num  = int(input())
            x1 = Data(name, num)
            Am.update(x1)
        elif na[0] == 'd':
            Am.display()
        elif na[0] == 'q':
            break

    del Am