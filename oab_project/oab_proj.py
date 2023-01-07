# STEP 1
# import libraries
import fitz
import io
from PIL import Image
import pprint as pp
import re


file = "COMO PASSAR NA OAB - 5.000 QUESTÕES - 15ª EDIÇÕES - 2019.pdf"
pdf_dict = {}
index_list = []
q_list = []


def extract1():    
    pdf_file = fitz.open(file)

    for page in range(len(pdf_file)):
        
        pdf_dict[page] = {pdf_file[page].get_text()}
    for x, y in pdf_dict.items():
        if x < 6:
            index_list.append(str(y))
        else:
            q_list.append(str(y))
    return q_list

q_list = extract1()


###########################################

def extract2(list):
    lines = [x.split("\\n") for x in q_list]
    delList = ["{'EDUARDO DOMPIERI", "'}", "{''}"]
    concatLines = []
    for x in lines:
        for y in x:
            if y not in delList:
                concatLines.append(y)
    return concatLines

concatLines = extract2(q_list)



def l_check(lineList):
    lineTotal = len(lineList)
    #starts with an lowercase letter
    l1 = re.compile(r"^[a-z]{1}")    
    n1 = 0
    #starts with an uppercase letter
    l2 = re.compile(r"^[A-Z]{1}")    
    n2 = 0
    #starts with parentheses and has only one uppercase letter inside them
    l3 = re.compile(r"^(\(){1}[A-Z]{1}")    
    n3 = 0

    l4 = re.compile(r"^(\(){1}[a_z,A-Z]{2,}")    
    n4 = 0

    
    for line in lineList:
                
        m1 = re.match(l1, line)
        m2 = re.match(l2, line)
        m3 = re.match(l3, line)
        m4 = re.match(l4, line)

        if m1 is not None:
            n1 += 1 
        elif m2 is not None:
            n2 += 1
        elif m3 is not None:
            n3 += 1
        elif m4 is not None:
            n4 += 1
        
        else:
            pass
    notMatch = lineTotal - n1 - n2 -n3 -n4
    print(f"Total lines: {lineTotal} \n " +
            f"Matched lines: lowercase letter start -- {n1} \n" +
            f"Matched lines: uppercase letter start -- {n2} \n" +
            f"Matched lines: parenthesis with single uppercase  -- {n3} \n" +
            f"Matched lines: l4 -- {n4} \n" + 
            "Unindentified lines: {:.2f} %".format(notMatch/lineTotal*100)
            )
    
###############################################
def concatenate(stringList, index=0, referenceList= ""):
    headString = ""
    bodyString = ""
    lastIndex = 0
    finalStringList = []
    export = True
    for stringLine in stringList:
        
        lastIndex = stringList.index(stringLine)

        
        print(f"{stringLine} \n" + f"Status: {lastIndex}/{len(stringList)}")
        if stringLine.startswith("(") == True:
            print("------------------------------Parenthesis found: Concatenation process started")
            
            if headString == "":
                headString == stringLine
                
                
            else:
                print("------------------------------------------------New parenthesis found: Concatenation process started")
                finalStringList.append(headString + bodyString)
                print("###################################################################################")
                break
                
        else:
            print("-------------------------------------No parenthesis foud: stored line")
            if stringLine[0].islower():
                bodyString += stringLine
            else:
                pass
    if lastIndex < 31296:
        finalStringList.append(concatenate(stringList=stringList, index=lastIndex, referenceList=referenceList))
    else:
        return finalStringList




def extract3(list):
    mainDict = {}
    count = 0
    for item in list:
        count += 1
        if "Gabarito" in item:
            mainDict[count] = {'l_kind': 'ans', 'l_body': item }
            continue
        elif"(" in item and ")" in item:   
            if "(" in item[:4] and ')' in item[:4]:
                mainDict[count] = {'l_kind': 'body', 'l_body': item }
            else:
                if item.startswith("("):
                    mainDict[count] = {'l_kind': 'head', 'l_body': item }
        else:
            mainDict[count] = {'l_kind': 'body', 'l_body': item }
            
    return mainDict    
#mainDict = extract3(concatLines)


def extract4(dict):
    finalDict = {}
    main_line = ""
    ans_line = ""
    count = 0
    for x in dict.values():
        line = x.get('l_body')
        if x.get('l_kind') == "head":
            if main_line == "":
                main_line += line
            else:   
                count += 1
                finalDict[count] = {'string': main_line}
                main_line = line
                continue
        elif x.get("l_kind") == "body":
            main_line += line
        #elif x.get('l_kind') == "ans":
       #     ans_line = line

    return finalDict
    

def extract5(file):
    mainDict = {}
    count2 = 0
    stringList = []
    with open(file, mode="r", encoding="utf-8") as file:
        r = file.readlines()
        lines = [line for line in r]
        for line in lines:        
            l= line.split(",",2)
            if l[2] != "":
                mainDict[int(l[0])] = {'l_kind': str(l[1][1:]), 'l_body': str(l[2][:-1]) }
            else:
                continue
    return mainDict
            
#faltajoga no excell ou num csv

mainDict = extract5("oab2.txt")
finalDict = extract4(mainDict)


with open("oab3.txt", mode="w", encoding="utf-8") as file:
    for x in finalDict.values():
        string = x.get('string')
        ans = x.get("ans")
        file.write(f"{string}" + '##' +  "Resposta" + '\n'L)



        