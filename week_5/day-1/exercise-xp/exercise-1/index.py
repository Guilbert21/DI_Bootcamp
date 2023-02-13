class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("tom", 3)
cat2 = Cat("yo", 1)
cat3 = Cat("mimi", 6)

cats = [cat1, cat2, cat3]

    
def oldest_cat(cats):
            oldest_age = 0
            oldest_cat = None

            for cat in cats:
                if cat.age>oldest_age:
                    oldest_cat= cat

            return oldest_cat
        
oldest_cat_found = oldest_cat(cats)

print(f"the oldest  cat is {oldest_cat_found.name} and is {oldest_cat_found.age}")

# def youngest_cat(cats):
#             youngest_age = 10000
#             youngest_cat = None

#             for cat in cats:
#                 if cat.age<youngest_age:
#                     youngest_cat= cat

#             return youngest_cat
        
# youngest_cat_found = youngest_cat(cats)

# print(f"the youngest  cat is {youngest_cat_found.name} and is {youngest_cat_found.age}")