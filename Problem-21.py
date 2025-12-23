while True:
    print("1.cm to ft\n2.kl to miles\n3.usd to inr\n4.exit")
    
    op = input("Choice: ")
    
    if op == '1': 
        print(float(input("cm: ")) * 0.0328)
    elif op == '2': 
        print(float(input("kl: ")) * 0.621)
    elif op == '3': 
        print(float(input("usd: ")) * 82.5)
    elif op == '4': 
        break
