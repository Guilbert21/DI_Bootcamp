class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        kwargs['is_child'] = True
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs['name']} was born into the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"The {self.last_name} family:")
        for member in self.members:
            print(f"- {member['name']}")

f = Family([
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
], 'Johnson')

f.family_presentation()

f.born(name='David', age=0, gender='Male')

print(f.is_18('Michael'))
print(f.is_18('David'))
