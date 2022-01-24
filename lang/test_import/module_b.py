from lang.test_import.module_a import a


a['value'] = a['value'] + 1

print(f'a={a} in module_b')
