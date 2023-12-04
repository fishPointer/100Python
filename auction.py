# Auction Program Flow Chart

# Take Name, Bid Value, and ask if there are other bidders
# If yes, clear screen

# It repeats the inputs
# It logs all the inputs

# Once no, it lists the winner and the bid value

# The clear function is native in replit, and I don't want to use a module so \n * 100

# Use the max() function, native, no math module needed

bidlist = []
bidvalues = []


def screen_clear():
    print("\n" * 100)


def new_bid():
    name = input("What is your name? \n")
    bidvalue = int(input("What is your bid? \n$"))
    loop = input("Are there other bidders? (Y or N)\n")

    bid_entry = {
        "name": name,
        "value": bidvalue,
    }

    bidlist.append(bid_entry)

    if loop == "Y":
        screen_clear()
        new_bid()


print("Welcome to the Silent Auction")
new_bid()

bidlistlength = range(len(bidlist))

for x in bidlistlength:
    bidvalues.append(bidlist[x]["value"])

# print(f"bidvalues list: {bidvalues}")

winvalue = max(bidvalues)

# print(f"winning value: {winvalue}")

for x in bidlistlength:
    if bidlist[x]["value"] == winvalue:
        winnername = bidlist[x]["name"]
        # print(f"winner: {winnername}")

print(f"The winner is {winnername} with a bid of {winvalue}.")
print("This concludes the silent auction.")
