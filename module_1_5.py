immutable_var = 1, 2, 'Alex', False
print('Immutable taple:', immutable_var)
#immutable_var[1] = True
#print(immutable_var)
#Код выдаёт ошибку, поэтому он был превращён мной в комментарий
#Кортеж относится к неизменяемому типу данных, поэтому изменить значения элементов кортежа нельзя
mutable_list = [1, 2, 'Alex', False]
mutable_list[3] = 'Masha'
mutable_list[1] = True
print('Mutable list:', mutable_list)
