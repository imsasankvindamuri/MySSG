hk_to_iast = {
    "A": "ā", "I": "ī", "U": "ū", "R": "ṛ", 
    "M": "ṃ", "H": "ḥ", "G": "ṅ","J": "ñ",
    "T": "ṭ", "D": "ḍ", "N": "ṇ", "n": "n",
    "z": "ś", "S": "ṣ", "L" : "ḻ"
}

def HarvardKyotoToIAST(hkstring : str) -> str:
    iast_first_pass = ''
    iast_text = ''
    i = 0
    
    while i < len(hkstring):
        if hkstring[i] not in hk_to_iast:
            iast_first_pass += hkstring[i]
        else:
            iast_first_pass += hk_to_iast[hkstring[i]]
        i += 1
    
    i = 0

    while i < len(iast_first_pass):
        if iast_first_pass[i] == "ṛ":
            if iast_first_pass[i + 1] == "ṛ":
                iast_text += "ṝ"
                i += 2
            else:
                iast_text += iast_first_pass[i]
                i += 1
        else:
            iast_text += iast_first_pass[i]
            i += 1

    return iast_text

if __name__ == "__main__":
    pass