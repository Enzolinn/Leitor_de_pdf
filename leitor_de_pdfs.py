import PyPDF2, pyttsx3


#Lembre-se de no nome do pdf usar o endereço certinho do mesmo.

print("digite o pdf que vc quer ouvir")
livro=input()
path= open(livro, 'rb')
pdf_reader= PyPDF2.PdfReader(path)

speak = pyttsx3.init()

    
for pages in range(len(pdf_reader.pages)):
    text= pdf_reader.pages[pages].extract_text()
    speak.say(text)
    speak.runAndWait()
speak.stop








