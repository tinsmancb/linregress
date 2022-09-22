import pandas as pd


def main():
    penguins = pd.read_csv('penguins.csv')
    adelie = penguins[penguins['species'] == 'Adelie']
    chinstrap = penguins[penguins['species'] == 'Chinstrap']
    gentoo = penguins[penguins['species'] == 'Gentoo']

    del adelie['species']
    del adelie['island']
    del adelie['sex']
    del adelie['bill_depth_mm']
    del adelie['body_mass_g']

    adelie.dropna().to_csv('adelie.csv', index=False)

    del chinstrap['species']
    del chinstrap['island']
    del chinstrap['sex']
    del chinstrap['bill_depth_mm']
    del chinstrap['body_mass_g']

    chinstrap.dropna().to_csv('chinstrap.csv', index=False)

    del gentoo['species']
    del gentoo['island']
    del gentoo['sex']
    del gentoo['bill_depth_mm']
    del gentoo['body_mass_g']

    gentoo.dropna().to_csv('gentoo.csv', index=False)

if __name__ == '__main__':
    main()