class Pet:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
        self.pet_list_age=[]
        self.pet_list_name=[]

    def input_3(self):
        for a in range(0, 3):
            self.name = input("請輸入寵物名:")
            self.age = int(input("請輸入年紀:"))
            self.color = input("請輸入毛顏色:")
            self.pet_list_age.append(self.age)
            self.pet_list_name.append(self.name)

    def get_max_age(self):
        max_age = self.pet_list_age[0]
        max_index=0
        for n in range(0,3):
            if self.pet_list_age[n]>max_age:
                max_age=self.pet_list_age[n]
                max_index=n
        return print(self.pet_list_name[max_index],"是年紀最大者",max_age,"歲")

    def get_min_age(self):
        min_age = self.pet_list_age[0]
        min_index=0
        for n in range(0,3):
            if self.pet_list_age[n]<min_age:
                min_age=self.pet_list_age[n]
                min_index=n
        return print(self.pet_list_name[min_index],"是最年輕為",min_age,"歲")

p=Pet("nick",18,"color")
name=p.name
age=p.age
color=p.color
p.input_3()
p.get_max_age()
p.get_min_age()
