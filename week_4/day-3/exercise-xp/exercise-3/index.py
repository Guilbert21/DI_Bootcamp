brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": "men, women, children, home",
    "international_competitors": "Gap, H&M, Benetton",
    "number_stores": 7000,
    "major_color":{
    "France": "blue",
    "spain": "red",
    "US": "pink, red"
    }
    }

brand.update(
    {"number_stores": 2}
)

# print("The client if Zara are:")

brand["creation_country"]= "Spain"
# print(brand)

iskeyPresent = "international_competitors" in brand
# print(iskeyPresent)
if iskeyPresent == True:
    brand["international_competitors"] = "Gap, H&M, Benetton, Desigual"

# print(brand)

brand.pop("creation_date", 1975)
print(brand)

print(brand.get("international_competitors"[-1]))

print(brand.get("major_color",["US"]))
#some difficulties to target




