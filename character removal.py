def super(prealpha):

    alpha = prealpha.lower().replace(' ','-')

    postalpha = ''

    for i in alpha:
        if i.isalnum() or i == '-':
            postalpha += i

    return postalpha

print(super('hah112121AAAA kaja ah'))

