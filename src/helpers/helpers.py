def read_attack_vectors(word_list_path):
    import os
    print(os.getcwd())
    result = []
    with open(word_list_path, 'r') as file:
        for line in file:
            l = line.strip()
            if not l.startswith('#'):
                result.append(expr_evaluator(l))
    return result



