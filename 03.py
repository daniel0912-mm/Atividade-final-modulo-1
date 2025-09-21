ip = ('1.1.1.1')
ip_modificado = ''
for i in ip:
    if i == '.':
        simbolo_mod = i.replace('.', '[.]')
        ip_modificado += simbolo_mod
    else:
        ip_modificado += i
print(ip)
print(ip_modificado)