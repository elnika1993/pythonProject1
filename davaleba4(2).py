def zodiaqo():
    z = {"verzi": "21 marti-19 aprili","kuro": "20 aprili-20 maisi", "tyupebi": "21 maisi-20 ivnisi",
         "kirchxibi": "21 ivnisi-22 ivlisi", "lomi": "23 ivlisi-22 agvisto", "qalwuli": "23 agvisto-22 seqtemberi",
         "saswori": "23 seqtemberi-22 oqtombri", "morieli": "23 oqtomberi-21 noembri",
         "mshvildosani": "22 noemberi-21 dekembri", "txis rqa": "22 dekemberi-19 ianvri",
         "merwyuli": "20 ianvari-18 tebervli", "tevzebi": "19 tebervali-20 marti"}
    a = input("sheiyvane saxeli: ")
    b = input("sheiyvane gvari: ")
    c = input("sheiyvane zodiaqo: ")
    if c == "verzi":
        print(a, b, "tqveni zodiaqos mixedvit tqven daibadet", z["verzi"],"-s", "monakvetshi")
    elif c == "kuro":
        print(a, b, "tqveni zodiaqos mixedvit tqven daibadet", z["kuro"], "-s", "monakvetshi")
    elif c == "tyupebi":
        print(a, b, "tqveni zodiaqos mixedvit tqven daibadet", z["tyupebi"], "-s", "monakvetshi")
    elif c == "kirchxibi":
        print(a, b, "tqveni zodiaqos mixedvit tqven daibadet", z["kirchxibi"], "-s", "monakvetshi")
    elif c == "lomi":
        print(a, b, "tqveni zodiaqos mixedvit tqven daibadet", z["lomi"], "-s", "monakvetshi")
    elif c == "qalwuli":
        print(a, b, "tqveni zodiaqos mixedvit tqven daibadet", z["qalwuli"], "-s", "monakvetshi")
    elif c == "saswori":
        print(a, b, "tqveni zodiaqos mixedvit tqven daibadet", z["saswori"], "-s", "monakvetshi")
    elif c == "morieli":
        print(a, b, "tqveni zodiaqos mixedvit tqven daibadet", z["morieli"], "-s", "monakvetshi")
    elif c == "mshvildosani":
        print(a, b, "tqveni zodiaqos mixedvit tqven daibadet", z["mshvildosani"], "-s", "monakvetshi")
    elif c == "txis rqa":
        print(a, b, "tqveni zodiaqos mixedvit tqven daibadet", z["txis rqa"], "-s", "monakvetshi")
    elif c == "merwyuli":
        print(a, b, "tqveni zodiaqos mixedvit tqven daibadet", z["merwyuli"], "-s", "monakvetshi")
    elif c == "tevzebi":
        print(a, b, "tqveni zodiaqos mixedvit tqven daibadet", z["tevzebi"], "-s", "monakvetshi")
    elif c == "zodiac":
        print("arasworia")
    else:
        print("didi shecdoma")
zodiaqo()