heros=['spider man','Thor','hulk','Iron man','Captain america']

print("The lenght of the heros array is " + str(len(heros)))

length_array = len(heros)

heros.insert(length_array, "Batman")

heros.remove("Batman")

heros.insert(3, "Batman")

print(heros)

heros[1:3] = ["God"] # Remember this

print(heros)

heros.sort() # Sorts alphabetically ------<Case matters>
print(heros)