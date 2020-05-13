"""
coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
x, y, z = coordinates
print(y)
"""

"""
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer.get("birthdate", "Jan 1 1980"))
"""

phone = input("Phone")
digits_mapping = {
    "1": "One",
    "2": "Two",

}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + ""
    print(output)
