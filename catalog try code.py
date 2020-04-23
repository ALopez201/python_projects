import color_options_catalog

appliances = color_options_catalog.ColorOptionsCatalog()

appliances.add_product('microwave', ['black', 'white'])
appliances.add_product('stove', ['white', 'stainless'])
print(appliances.get_matching_products('white'))
