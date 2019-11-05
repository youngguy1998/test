def tool(x):
    b = x.capitalize()
    return b
def main():
    r = map(tool, ["adam", "LISA", "barT"])
    print([s for s in r])
main()