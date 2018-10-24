def print_models(unprinted_designs, completed_models):
    # No idea how to handle detect the situation of second parameter
    # if completed_models != False:
    #     print('Please pass a blank Array')
    #     exit()
    while unprinted_designs:
        # unprinted_designs = sorted(unprinted_designs)
        current_design = unprinted_designs.pop()
        print('Printing model: ' + current_design)
        completed_models.append(current_design)
        # completed_models = unprinted_designs[:]
    print('The following models have been printed: ')
    for x in completed_models:
        print(x)
    print('The unprinterd designs is : ')
    for i in unprinted_designs:
        print(i)



print_models(['1', '2', '3'][:], [])
