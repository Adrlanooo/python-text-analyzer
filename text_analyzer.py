#this is our main point --> this will open the file 
file_opener = open("sample_txt.txt")
x = file_opener.read() #--> will read the file but wont print out yet

#will split the text into a list and count each string
def count_words(text):
    word_count = len(text.split())
    return word_count

#counts characters, makes into lwercase,true/false if and
def count_character(text):
    char_count = 0  
    letter_count = 0

    for char in text.lower():
        if char.isalpha():
            char_count += 1
            letter_count += 1
        if char.isalpha() == False:
            char_count += 1
        if char.isspace():
            char_count -= 1
            #letter_count -= 1
    return char_count, letter_count

c_c, l_c = (count_character(x))

#vowel counter
def vowel_constant_count(text):
    vowel = "aeiou"
    vowel_count = 0
    constant = 0

    for char in text.lower():
        if char in vowel:
            vowel_count += 1
            constant -= 1
        if char.isalpha():
            constant += 1
    return vowel_count, constant

v_c, const_c = vowel_constant_count(x)
###longest word checker 

def long_word_chck(text):
    
    txt = text.lower()
    words = txt.split()

    clean_words = []
    for word in words:
        clean = word.strip(".,!?;:\"'()")
        if clean != "":
            clean_words.append(clean)

    longest = ""
    for word in clean_words:
        if len(word) > len(longest):
            longest = word

    return longest

lng_wrd = long_word_chck(x)


#main output function
def text_analysis_report():

    print("""----- TEXT ANALYSIS REPORT -----   
          """)
    print("Total Characters:",c_c)
    print("Total Words:",count_words(x))
    print("Letters:",l_c)
    print("Vowels:",v_c)
    print("Constants:", const_c)
    print("Longest Word is:", lng_wrd)


    


text_analysis_report()


