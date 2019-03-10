def trifeca(word):
    m = False
    if len(word)<6:
        return m
    if len(word)==6:
        if word[0]==word[1] and word[2]==word[3] and word[4]==word[5]:
            m=True
    else:
        for i in range(len(word)-6):
            if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
                m=True
    return m
