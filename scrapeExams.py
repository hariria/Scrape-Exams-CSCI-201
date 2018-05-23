# MADE BY ANDREW HARIRI 05/22/2018
# SCRIPT IS DESIGNED TO GRAB ALL OF THE SAMPLE PRACTICE TESTS AVAILABLE
# ON USC'S CSCI 201 SITE

import os
import requests

# getPracticePDFs FIRST GOES THROUGH THE PAGE, ADDS ALL THE RELEVENT PDFS TO A
# 2D LIST. THEN SAVES THOSE TO YOUR LOCAL DIRECTORY
def getPracticePDFs(url="http://www-scf.usc.edu/~csci201/exams.html"):
    arrayOfPDFs = []
    directoryURL = url[:len(url) - 10]
    page = requests.get(url)
    countRow = 0
    for line in page.iter_lines():
        decodedLine = line.decode('utf-8')
        if "<tr>" in decodedLine:
            arrayOfPDFs.append([])
        elif "</tr>" in decodedLine:
            countRow += 1
        if ".pdf" in decodedLine:
            temp = decodedLine.split("\"")
            for element in temp:
                if ".pdf" in element:
                    arrayOfPDFs[countRow].append(directoryURL + element)
    for elementArray in arrayOfPDFs:
        if (len(elementArray) == 0):
            continue
        else:
            # print(elementArray)
            file1 = elementArray[0]
            indexOfPDF = elementArray[0].find(".pdf")
            decIndex = indexOfPDF
            while(decIndex != 1):
                if file1[decIndex - 1] == '-':
                    break
                else:
                    decIndex -= 1
            newFolderName = file1[decIndex: indexOfPDF]
            if "syllabus" in newFolderName:
                continue
            if not os.path.exists(newFolderName):
                os.makedirs(newFolderName)
            for element in elementArray:
                response = requests.get(element)
                savePath = os.path.join(os.getcwd(), newFolderName, element[element.find("exams/") + 6: ])
                with open(savePath, "wb") as pdf:
                    pdf.write(response.content)


getPracticePDFs()
