places = []

# ---------------- Functions --------------- #
def destination_picker():
    global places
    print("Please enter your 5 travel destinations:")
    inp1 = input("Destination 1: ")
    inp2 = input("Destination 2: ")
    inp3 = input("Destination 3: ")
    inp4 = input("Destination 4: ")
    inp5 = input("Destination 5: ")
    places = [inp1, inp2, inp3, inp4, inp5]

def print_out_itinerary():
    global places
    count1 = 1
    for x in places:
        numbering = str(count1) + "."
        print(numbering, x)
        count1 += 1

def update_2_and_5():
    global places
    print("Let's update your 2nd and 5th destinations.")
    inp1 = input("Enter a new destination for position 2: ")
    del places[1]
    places.insert(2, inp1)
    inp2 = input("Enter a new destination for position 5: ")
    del places[4]
    places.insert(4, inp2)



# ------------------------- Main --------------------------- #

destination_picker()
print("Original Travel Itinerary:")
print_out_itinerary()
update_2_and_5()
print("Updated Travel Itinerary:")
print_out_itinerary()

