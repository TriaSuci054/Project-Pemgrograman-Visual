productList = {}


def file_open():
    with open('Products.txt' , 'r') as file:
        for row in file:
            if not row:
                continue
            else:
                product, values = row.split(',')
                productList[product] = values


def result(product, gram):
    """Calculates the nutritional values and returns result"""
    kcalValue = proteinValue = karbohidratValue = lemakValue = 0
    if product in productList:
        (kcal, protein, karbohidrat, lemak) = productList[product].split(':')
        kcalValue += gram / 100 * int(kcal)
        proteinValue += gram / 100 * int(protein)
        karbohidratValue += gram / 100 * int(karbohidrat)
        lemakValue += gram / 100 * int(lemak)
        outcome = "Hasil perhitungan nutrisi %d kcal, "\
           "%d protein, %d karbohidrat, %d lemak."\
           % (kcalValue, proteinValue, karbohidratValue, lemakValue)
    else:
        outcome = "Maaf, makanan yang anda masukkan belum tersedia datanya : %s, but you can add it! :)"% (product)
    return outcome











