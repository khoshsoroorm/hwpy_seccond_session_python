word_1 = 'Right>>>'
word_2 = 'Left>>>>'
w1 = word_1.replace('>', '<')
w1_list = list(w1)
w1_listjoin = w1_list[::-1]
w1join = ''.join(w1_listjoin)
w2 = word_2.replace('>', '<')
w2_list = list(w2)
w2_listjoin = w2_list[::-1]
w2join = ''.join(w2_listjoin)
print(word_2, ' | ', word_1)
print(w1join, ' | ', word_1)
print(word_2 , ' | ', w2join)
