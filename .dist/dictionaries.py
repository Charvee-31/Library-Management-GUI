Month_Name={
    1:"January",
    2:"Feburary",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}
num=int(input("Enter the month number:"))
print(Month_Name.get(num,"THERE ARE ONLY 12 MONTHS!!"))