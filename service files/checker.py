from os import system

f = open('service files/Installed.f')
if f.readline().strip() == "False":
    print('Установка нужных библиотек')
    system('pip install -r service files/libs.txt')
    print('\nГотово!.')
    g = open('service files/Installed.f', 'w')
    g.write('True')
    g.close()
f.close()

#для теста установки, при релизе на Github комментим
'''
g = open('service files/Installed.f', 'w')
g.write('False')
g.close()
'''