class student:
    def __init__(self, name, gender):
        self.Name = name
        self.Gender = gender
        self.Grades = []
    def __gt__(self, tar):
        if self.avg() > tar.avg():
            return True
        else:
            return False
    def avg(self):
        return ('%.1f' %(sum(self.Grades) / len(self.Grades)))
    def add(self, grade):
        self.Grades.append(grade)
    def fcount(self):
        fail = 0
        for i in self.Grades:
            if i < 60:
                fail += 1
        return fail
    def show(self):
        print('Name:', self.Name)
        print('Gender:', self.Gender)
        print('Grades:', self.Grades)
        print('Avg:', self.avg())
        print('Fail Number:', self.fcount())
        print()

def top(*students):
    for i in students:
        i.show()
    top = max(students)
    #print(top)    
    return top
    

s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

top_student = top(s1,s2,s3,s4,s5)
print('Top Student:')
top_student.show()