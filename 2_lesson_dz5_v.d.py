prix = [57.8, 46.51, 97, 100, 55.5, 63, 22.5, 155, 150.3, 170]

for i, num in enumerate(prix):
    price = str(f"{float(num):.2f}").split(".")
    print(f"{price[0]} руб {price[1]} коп,", end = ' ')

print(f"{'b':-^100}")

prix.sort()
print(prix)

print(f"{'c':-^100}")
prix_2 = sorted(prix, reverse=True)
print(prix_2)

print(f"{'d':-^100}")
print((f"Пять самых дорогих товаров {prix[4:9]}!"))






