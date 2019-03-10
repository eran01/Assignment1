def check_palindrome():
    palindromes=[]
    V=list(range(100000,999999))
    for i in V:
        if str(i)[2:6]==str(i)[5:1:-1]:
            X=i+1
            if str(X)[1:6]==str(X)[5:0:-1]:
                X=X+1
                if str(X)[1:5]==str(X)[4:0:-1]:
                    X=X+1
                    if str(X)[0:6] == str(X)[::-1]:
                        palindromes.append(i)
    return palindromes

check_palindrome()
