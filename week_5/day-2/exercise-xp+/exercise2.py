class TheIncredibles(Family):
    def __init__(self, members, last_name):
        super().__init__(members, last_name)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if self.is_18(name):
                    print(f"{name}'s power is {member['power']}.")
                else:
                    raise Exception(f"{name} is not over 18 years old and cannot use their power.")
        else:
            print(f"{name} is not a member of the {self.last_name} family.")

    def incredible_presentation(self):
        super().family_presentation()
        for member in self.members:
            print(f"- {member['incredible_name']} ({member['power']})")

# Create a new TheIncredibles instance with initial data
ti = TheIncredibles([
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
], 'Parr')

ti.incredible_presentation()

ti.born(name='Jack', age=0, gender='Male', power='Unknown Power', incredible_name='Baby Jack')

ti.incredible_presentation()

try:
    ti.use_power('Jack')
except Exception as e:
    print(str(e))

ti.use_power('Michael')
