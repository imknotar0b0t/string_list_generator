"""
Was curious about generating a giant list of strings.

Figured out how to create a list with 15,018,570 entries.

Could not get a larger set due to the exponential increase in the size of the list
when going from a length of 4 to a length of 5.

Justin Mitchell
"""
def build_word_list():
	
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = alphabet_lower.upper()
    digits = '1234567890'
    
    my_characters = list()
	
    for a in alphabet_lower:
        my_characters.append(a)

    for a in alphabet_upper:
        my_characters.append(a)

    for a in digits:
        my_characters.append(a)
	
    temp_list = my_characters[:]
    big_list = list()
    pw_length = 4
    
    c = 0
    while c < pw_length:
        #print('temp_list 1 --- ' + str(temp_list))
        holder = []
        for (d, e) in enumerate(temp_list):
            holder.append(e)
            big_list.append(e)
        #print('\nholder 1 --- ' + str(c) + str(holder))
        
        c += 1
        if c != pw_length:
            mid_way = []
            for (f, g) in enumerate(holder):
                mid_way.append(g)
            #print('\nmid_way --- ' + str(c) + str(mid_way))
            
            holder =[]
            holder = [[a+b for a in my_characters] for b in mid_way]
            #print('\nholder 2 --- ' + str(c) +str(holder))
            holder_length = len(holder)
            temp_list = []
            z = 0
            while z < holder_length:
                for (m, n) in enumerate(holder[z]):
                    temp_list.append(n)
                z += 1
            #print('\ntemp_list 2 --- ' + str(temp_list))
            
    #print('\nbig_list --- ' +str(big_list))
    
    big_list_length = len(big_list)
    
    print('big_list ' + str(len(big_list)))
    # print('temp_list ' + str(type(big_list)))
        
    return big_list

my_word_list = build_word_list()

my_word = 'sF5w'

answer = my_word in my_word_list
print(answer)