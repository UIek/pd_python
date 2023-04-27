# xxx = []
# while True:
#     inp = input()
#     if inp == "stop":
#         break
#     inp = int(inp)
#     if inp <= 200 and inp >= 1:
#         xxx.append(inp)
#     else:
#         print("zły zakres")
# print(xxx)

lista = [28, 56, 72, 37, 63, 68, 90 ]
nowa_lista = []
i = 0
while i < len(lista):
    if lista[i] % 2 == 0 and lista[i] < 70 and lista[i] > 50:
        nowa_lista.append(lista[i])
    i += 1
print(nowa_lista)
