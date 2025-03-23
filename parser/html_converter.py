import os
import parser.transliteration as tr

def preprocessor(filepath : str) -> str:

    if not os.path.exists(filepath):
        raise FileNotFoundError
    if not filepath.endswith(".md"):
        raise Exception("ExtensionError: Only Markdown Files Accepted.")
    
    with open(file=filepath, mode="r+") as f:
        lines = f.readlines()
        preprocessed_stack = []
        
        for line in lines:
            i = 0
            parse_stack = []
            
            while i < len(line):
                if line[i] != "|":
                    parse_stack.append(line[i])
                else:
                    hk_sanskrit_stack = []
                    while parse_stack[-1] != "/":
                        try:
                            hk_sanskrit_stack.append(parse_stack.pop())
                        except IndexError:
                            raise Exception("""Syntax Error: To convert from Harvard-Kyoto to IAST, please enclose designated text in these delimiters: /|. E.g.: /Rbhus|, /vRtra|, etc.""")
                    parse_stack.pop()
                    hk_sanskrit_stack.reverse()
                    parse_stack.append(tr.HarvardKyotoToIAST("".join(hk_sanskrit_stack)))
                
                i += 1
                            
            if parse_stack != ["\n"]:
                preprocessed_stack.append("".join(parse_stack[:-1]) + "<br>")
            else:
                preprocessed_stack.append("\n")
        
    return "\n".join(preprocessed_stack)

if __name__ == "__main__":
    pass