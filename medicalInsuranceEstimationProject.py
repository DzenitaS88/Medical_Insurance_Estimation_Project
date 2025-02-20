# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = "Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Estimate Akira's insurance cost
akira_insurance_cost = estimate_insurance_cost(name = "Akira", age = 19 , sex = 1, bmi = 27.1, num_of_children = 0, smoker = 0)

names = ["Maria", "Rohan", "Valentina", "Akira"]

insurance_costs = [4150.0, 5320.0, 35210.0, 2930.0]

insurance_data = zip(names, insurance_costs)
print(insurance_data)

converted_data = list(insurance_data)
print(converted_data)

estimated_insurance_data = []

estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))
estimated_insurance_data.append(("Akira", akira_insurance_cost))

print(estimated_insurance_data)

print("Here is the actual insurance cost data: " + str(converted_data))

print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))

maria_insurance_cost_difference = 4150.0 - 4222.0
print(maria_insurance_cost_difference)
print("Maria insurance cost difference is " + str(maria_insurance_cost_difference) + " euros.")

rohan_insurance_cost_difference = 5320.0 - 5442.0
print(rohan_insurance_cost_difference)
print("Rohan insurance cost difference is " + str(rohan_insurance_cost_difference) + " euros.")

valentina_insurance_cost_difference = 35210.0 - 36368.0
print(valentina_insurance_cost_difference)
print("Valentina insurance cost difference is " + str(valentina_insurance_cost_difference) + " euros.")

akira_insurance_cost_difference = 2930.0 - 2149.0
print(akira_insurance_cost_difference)
print("Akira insurance cost difference is " + str(akira_insurance_cost_difference) + " euros.")
