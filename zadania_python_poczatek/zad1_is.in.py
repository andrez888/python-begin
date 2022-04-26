shopping_elements = input("Wprowadź listę zakupów, rozdzielając poszczególne elementy przecinkiem: ")
shopping_list =shopping_elements.split()
print(shopping_elements)
is_shopping_list_long = len(shopping_list) > 4
print(f"Czy uważam, że Twoja lista zakupów jest długa? {is_shopping_list_long}")
if "bułki" or "chleb" in shopping_elements:
    print('Kupileś pieczywo :)')