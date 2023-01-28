with open('asdf.txt', 'w', encoding='UTF-8') as f:
    for i in range(0, 10):
        f.write('{}'.format(i))
        if i == 5: break
    f.write('end')