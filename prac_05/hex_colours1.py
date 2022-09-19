"""CP1404_practical"""


color_codes = {'Absolute': '#0048ba','AcidGreen':'#b0bf1a','Amber':'#ffbf00','AntiqueWhite':'#faebd7',
               'Aqua': '#00fff','Azure1':'#f0fff','BabyBlue':'#89cff0','BarnRed':'#7c0a02','Beaver':'#9f8170',
               'Beige': '#f5f5dc'}

color_names = input("Enter a color name:")
while color_codes != "":
    print("The code for {} is {}".format(color_names,color_codes.get(color_names)))

    color_names = input("Enter a color name:")