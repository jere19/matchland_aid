import pandas

data = pandas.DataFrame.from_csv('matchland.csv', index_col=None)

basecols = list(data.keys()[:4])
beasts = list(data.keys()[4:])


def show_optim(beast):
    print(data.sort_values(beast, ascending=False)[['World','Chapter', 'Level', 'Cost'] + [beast]].dropna().astype(int).to_string(index=False))


while True:
    print(list(zip(range(len(beasts)), beasts)))
    print("Input beast number:")
    beast = beasts[int(input())]
    show_optim(beast)
