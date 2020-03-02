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
    pw_length = 5
    
    # for strings less than or equal to 4 characters
    if pw_length <= 4:
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
            
    if pw_length > 4:
        # create list of all 2 character values
        two_filter = [[a+b for a in my_characters] for b in my_characters]
        
        # print('\ntwo_filter --- ' + str(len(two_filter)) + str(two_filter))
        two = []
        
        f = 0
        while f < len(two_filter):
            for (d, e) in enumerate(two_filter[f]):
                two.append(e)
            f += 1
            
        # print('\two --- ' + str(two))
        
        three_filter = [[a+b for a in two] for b in my_characters]
        
        # print('\ntthree_filter --- ' + str(len(three_filter)) + str(three_filter))
        three = []
        
        f = 0
        while f < len(three_filter):
            for (d, e) in enumerate(three_filter[f]):
                three.append(e)
            f += 1
            
        # print('\three --- ' + str(three))
        
        # Odd or even
        oe = pw_length%2
        
        if oe == 1:
            five_filter = [[a+b for a in three] for b in two]
            
            five = []
            
            f = 0
            while f < len(five_filter):
                for (d, e) in enumerate(five_filter[f]):
                    five.append(e)
                f += 1
            
    #print('\nbig_list --- ' +str(big_list))
    
    big_list_length = len(big_list)
    
    print('big_list ' + str(len(big_list)))
    # print('temp_list ' + str(type(big_list)))
        
    return big_list

my_word_list = build_word_list()

my_word = 'sF5w'

answer = my_word in my_word_list
print(answer)