print("This is the insurance quote comparison program.")
print("Let's start.")
print()

company_1 = input("Name of the first company: ")
fee_1 = float(input("Initiation fee of first company e.g 256.60 means R256.60: "))
prem_1 = float(input("Basic premium of the first company e.g 256.60 means R256.60: "))
perc_1 = int(input("Loading percentage of first company e.g 80 means 80 percent: "))
print()

company_2 = input("Name of the second company: ")
fee_2 = float(input("Initiation fee of second company e.g 256.60 means R256.60: "))
prem_2 = float(input("Basic premium of the second company e.g 256.60 means R256.60: "))
perc_2 = int(input("Loading percentage of second company e.g 80 means 80 percent: "))
print()

prem_load_1 = (perc_1 / 100) * prem_1 + prem_1
prem_load_2 = (perc_2 / 100) * prem_2 + prem_2

print("-"*30)
print("Info | Company 1 | Company 2")
print("-"*30)


print(f"Name | {company_1} | {company_2}")
print(f"Init Fee | {fee_1} | {fee_2}")
print(f"Premium | {prem_1} | {prem_2}")
print(f"Premium Loaded | {prem_load_1} | {prem_load_2} ")
print("-"*30)


