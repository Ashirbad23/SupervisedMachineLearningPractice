from scipy.special import comb

no_of_Students = 8
no_of_members = 3

total = comb(no_of_Students, no_of_members)
print(total)