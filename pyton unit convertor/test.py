
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "meter": 1,
        "kilometer": 0.001,
        "mile": 0.000621371,
        "foot": 3.28084,
        "kilogram":1,
        "gram":1000,
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return "Invalid unit. Please use meter, kilometer, mile, or foot,kilogram or gram."

   
    value_in_meters = value / conversion_factors[from_unit]
    
   
    converted_value = value_in_meters * conversion_factors[to_unit]
    
    return converted_value


value = float(input("Enter value: "))
from_unit = input("Enter from unit (meter, kilometer, mile, foot, kilogram, gram): ").lower()
to_unit = input("Enter to unit (meter, kilometer, mile, foot ,  kilogram, gram): ").lower()

result = convert_units(value, from_unit, to_unit)


print(f"{value} {from_unit} is equal to {result} {to_unit}")
print('"thanks for coming"'),