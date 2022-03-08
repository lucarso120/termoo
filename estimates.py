from termo import select_word, play_game


x = 0
y = 0

for i in range(100):
    if play_game():
        x += 1
    else:
        y += 1

taxa = x/(x+y)

print("acertos: {} | erros: {} | Taxa de Sucesso: {}".format(x,y,taxa))
