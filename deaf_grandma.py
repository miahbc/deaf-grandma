def deaf_grandma(g, str):
    
    # input('command Prompt')
    if len(str) > 0 and str != str.upper():
        print("SPEAK UP, KID!")
        deaf_grandma(0, input('command Prompt'))
    elif str == str.upper() and str != '' and str != "" and str != "GOODBYE!":
        print("NO, NOT SINCE 1946!")
        deaf_grandma(0, input('command Prompt'))
    elif str == "GOODBYE!" and g == 0:
        print("LEAVING SO SOON?")
        g = g + 1
        deaf_grandma(1, input('command Prompt'))
    elif str == "GOODBYE!" and g > 0:
        print("LATER, SKATER!")
    else:
        if len(str) == 0:
            print("WHAT?!")
            deaf_grandma(0, input('command Prompt'))
            # print("something went wrong")
            # input('command Prompt')
    

deaf_grandma(0, input('command Prompt'))

# deaf_grandma('')
# deaf_grandma('hi, grandma!')
# deaf_grandma('Hi, grandma!')
# deaf_grandma('I SAID HI, GRANDMA!')
# deaf_grandma('GOODBYE!')
# deaf_grandma('GOODBYE!')
# deaf_grandma('HELLO')


# HEY KID!
# > hi, grandma
# SPEAK UP, KID!
# > I SAID HI, GRANDMA
# NO, NOT SINCE 1946!
# >
# WHAT?!
# > Goodbye!
# SPEAK UP, KID!
# > GOODBYE!
# LEAVING SO SOON?
# > GOODBYE!
# LATER, SKATER!