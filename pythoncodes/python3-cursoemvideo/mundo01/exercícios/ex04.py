algo = input('Digite algo: ')
print('O tipo é {}.'.format(type(algo)))
print('O que você digitou é alfa-numérico? {}. Ou é letra? {}. Ou é decimal? {}. Ou é digito? {}. É tudo minúsculo? {}. É tudo maiúsculo? {}'.format(algo.isalnum(), algo.isalpha(), algo.isdecimal(), algo.isdigit(), algo.islower(), algo.isupper()))