from parser import transliteration as tr, html_converter

print(tr.HarvardKyotoToIAST("vRtrasya niNyam vi carantyApo dIrghaM tama Azayad indrazatruH"))

with open("converted_test.md","w") as f:
    f.write(html_converter.preprocessor("/home/krishh/My_Projects/MySSG/test.md"))