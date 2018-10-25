def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: ' + current_design)
        completed_models.append(current_design)
    print('The following models have been printed: ')
    for x in completed_models:
        print(x)
    print('The unprinterd designs is : ')
    for i in unprinted_designs:
        print(i)
