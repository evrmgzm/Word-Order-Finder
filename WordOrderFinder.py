#import importlib
#Assignment_1 = importlib.import_module(“2020510091_evrimgizem_isci.py”)

bookText =  "book_1.txt"
book_1 = "book_1.txt"
book_2 = "book_2.txt"
Word_Order = 1
File_Output_1 = "result_1.txt"
File_Output_2="result_2.txt"
stopWords = ['able', 'about', 'above', 'abroad', 'according', 'accordingly',
        'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
        'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
        'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
        'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
        'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
        'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
        'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
        'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
        'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
        'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below',
        'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
        'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
        'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
        'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
        'consequently', 'consider', 'considering', 'contain', 'containing',
        'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
        'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
        'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
        'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
        'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
        'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
        'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
        'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
        'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
        'following', 'follows', 'for', 'forever', 'former', 'formerly',
        'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
        'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
        'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
        'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
        'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
        'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
        'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
        'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
        'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
        'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
        'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
        'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
        'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
        'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
        'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
        'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
        'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
        'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
        'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
        'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
        'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
        'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
        'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
        'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
        'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
        'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
        'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
        'overall', 'own', 'particular', 'particularly', 'past', 'per',
        'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
        'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
        'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
        'regardless', 'regards', 'relatively', 'respectively', 'right',
        'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
        'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
        'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
        'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
        'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
        'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
        'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
        'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
        'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
        'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
        'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
        'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
        'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
        'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
        'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
        'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
        'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
        'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
        'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
        'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
        'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
        'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
        'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
        'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
        'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
        'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
        'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
        'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
        'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
        'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
        'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens',
        'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
        'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
        'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
        'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
        'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
        'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
        'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
        'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
        'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
        'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
        'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
        'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
        'importance', 'important', 'index', 'information', 'invention', 'itd',
        'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
        'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
        'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
        'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
        'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
        'readily', 'ref', 'refs', 'related', 'research', 'resulted',
        'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
        'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
        'similar', 'similarly', 'slightly', 'somethan', 'specifically',
        'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
        'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
        'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
        'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
        'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
        'world', 'youd', 'youre']

#function for just 1 book
def Word_Order_Frequency_One_Book(bookText=None,Word_Order=None,File_Output_1="result_1.txt"):
    #control for if user call wrong input
    if (type(bookText) != str) or ( Word_Order != 1 and Word_Order != 2 ) or ( type(File_Output_1) != str ):        
        return
    if bookText and Word_Order and File_Output_1 is None:
        return
    #variables
    frequency = {}
    sortedV = {}
    sortedD = {}
    newWordList=[]
    #call the book and read them
    bookText=open("book_1.txt","r",encoding="utf-8")
    fileContents=bookText.read()
    bookText.close()
    #convert whole book to lowercase
    lowFileCont=fileContents.lower()
    #remove unnecessary char
    charList=["\",","*","_","{","}","[","]","(",")",">","+",".","!","$","'",":",",","/",'"',";","%","“","”","’","?"]
    for ch in charList:
        if ch in lowFileCont:
            lowFileCont = lowFileCont.replace(ch,"")
            
    #if word has - or — or \n, replace space there
    lowFileCont=lowFileCont.replace("\n"," ").replace("—"," ").replace("-"," ")    
    wordList=lowFileCont.split(' ')
    #remove alpha numeric words
    for item in wordList:
        if item.isalnum():
            wordList.remove(item)
     
    #remove digit and empty list elements
    wordList = [i for i in wordList if not i.isdigit()]       
    wordList = [x for x in wordList if x != '']
    
    #remove stop words and add new list(if lists elements have not stop words, add new list to this word)
    for q in wordList:
        if q not in stopWords:
            newWordList.append(q)
    #find same words and add frequency       
    if Word_Order==1:  
        for i in newWordList:
            if i in frequency:
                frequency[i] += 1
            else:      
                frequency[i] = 1
    #find same pairs and add frequency            
    elif Word_Order==2:        
        pairList = [newWordList[s]+' '+newWordList[s+1] for s in range(len(newWordList)-1)]
        for m in pairList:
            if m in frequency:
                frequency[m] += 1
            else:      
                frequency[m] = 1   
    
    #sorted reverse frequency
    sortedV = sorted(frequency, key=frequency.get, reverse=True)

    #sorted value and frequency add new dictionary
    for w in sortedV:
        sortedD[w] = frequency[w]
    
    
    #print(sortedD)
 
    #open new text and write result
    result_1=open("result_1.txt","w",encoding="utf-8")  
    result_1.write("      | word      |  word      | \n")
    result_1.write("      | order     |  order     | \n")
    result_1.write("      | sequence  |  frequency | \n")
    result_1.write("      --------------------------\n\n")
    

    keyList = list(sortedD.keys())
    for i in range (0 , 100):   
        result_1.write( keyList[i] )
        result_1.write(" - - - - > ")
        result_1.write( str(sortedD[ keyList[i]]))
        result_1.write("\n")
    
    result_1.close()

#call function
#Word_Order_Frequency_One_Book(bookText,Word_Order,File_Output_1)

#function for 2 books
def Word_Order_Frequency_Two_Books(book_1=None,book_2=None,Word_Order=None,File_Output_2="result_2.txt"):
    #control function parameters
    if (type(book_1) != str) or (type(book_2) != str) or ( Word_Order != 1 and Word_Order != 2 ) or ( type(File_Output_2) != str ) :        
        return
    if book_1 and book_2 and Word_Order and File_Output_2 is None:
        return
    #variables
    frequency_1 = {}
    sortedV_1 = {}
    sortedD_1 = {}
    newWordList_1=[]
    #open book 1 and read
    book_1=open("book_1.txt","r",encoding="utf-8")
    fileContents_1=book_1.read()
    book_1.close()
    #convert to lowercase whole book
    lowFileCont_1=fileContents_1.lower()
    charList=["\",","*","_","{","}","[","]","(",")",">","+",".","!","$","'",":",",","/",'"',";","%","“","”","’","?"]
    #remove unnecessary char
    for ch in charList:
        if ch in lowFileCont_1:
            lowFileCont_1 = lowFileCont_1.replace(ch,"")
            
    
    lowFileCont_1=lowFileCont_1.replace("\n"," ").replace("—"," ").replace("-"," ")   
    #convert to list
    wordList_1=lowFileCont_1.split(' ')
    #remove alpha numberic words
    for item in wordList_1:
        if item.isalnum():
            wordList_1.remove(item)
     
    #remove number and space list elements
    wordList_1 = [i for i in wordList_1 if not i.isdigit()]       
    wordList_1 = [x for x in wordList_1 if x != '']
    #remove stop words and add new list for book 1
    for q in wordList_1:
        if q not in stopWords:
            newWordList_1.append(q)
    #find same word and add frequency for book 1        
    if Word_Order==1:  
        for i in newWordList_1:
            if i in frequency_1:
                frequency_1[i] += 1
            else:      
                frequency_1[i] = 1
    #find same pairs and add frequency for book 1            
    elif Word_Order==2:        
        pairList_1 = [newWordList_1[s]+' '+newWordList_1[s+1] for s in range(len(newWordList_1)-1)]
        for m in pairList_1:
            if m in frequency_1:
                frequency_1[m] += 1
            else:      
                frequency_1[m] = 1   
    
    #sort and reverse the dictionary
    sortedV_1 = sorted(frequency_1, key=frequency_1.get, reverse=True)

    #add to new dictionary 
    for w in sortedV_1:
        sortedD_1[w] = frequency_1[w]

    #for book 2
    #variables
    frequency_2 = {}
    sortedV_2 = {}
    sortedD_2 = {}
    newWordList_2=[]
    #open and read book 2
    book_2=open("book_2.txt","r",encoding="utf-8")
    fileContents_2=book_2.read()
    book_2.close()
    #convert to lowercase whole book 2
    lowFileCont_2 =fileContents_2.lower()
    charList=["\",","*","_","{","}","[","]","(",")",">","+",".","!","$","'",":",",","/",'"',";","%","“","”","’","?"]
    #remove unnecessary char
    for ch in charList:
        if ch in lowFileCont_2:
            lowFileCont_2 = lowFileCont_2.replace(ch,"")
            
    
    lowFileCont_2=lowFileCont_2.replace("\n"," ").replace("—"," ").replace("-"," ") 
    #convert to list
    wordList_2=lowFileCont_2.split(' ')
    #remove alpha numeric word
    for item in wordList_2:
        if item.isalnum():
            wordList_2.remove(item)
     
    #remove space and digit
    wordList_2 = [i for i in wordList_2 if not i.isdigit()]       
    wordList_2 = [x for x in wordList_2 if x != '']
    #remove stop words and add new list for book 2
    for q in wordList_2:
        if q not in stopWords:
            newWordList_2.append(q)
            

                            
    #find same words for book 2 and add frequency      
    if Word_Order==1:  
        for i in newWordList_2:
            if i in frequency_2:
                frequency_2[i] += 1
            else:      
                frequency_2[i] = 1
    #find same pairs for book 2 and add frequency        
    elif Word_Order==2:        
        pairList_2 = [newWordList_2[s]+' '+newWordList_2[s+1] for s in range(len(newWordList_2)-1)]
        for m in pairList_2:
            if m in frequency_2:
                frequency_2[m] += 1
            else:      
                frequency_2[m] = 1   
    
    #sorted value list for book 2
    sortedV_2 = sorted(frequency_2, key=frequency_2.get, reverse=True)
    
    #sorted dictionary for book 2
    for w in sortedV_2:
        sortedD_2[w] = frequency_2[w]


    #find same words for book1 and book2
    newDictSameWord={}
    #add to list sorted dictionary keys(words)    
    keyList_1 = list(sortedD_1.keys())
    keyList_2 = list(sortedD_2.keys())
    
    #compare 2 list length 
    
    if len(keyList_1) < len(keyList_2):                     
        for k in range(0 , len(keyList_1)): 
            #if list2 in list1, add new dictionary and calculate the total number
            if keyList_1[k] in keyList_2:
                avarage = sortedD_1 [keyList_1[k]] + sortedD_1[keyList_1[k]]
                newDictSameWord={}.update({keyList_1[k]:avarage })                                
    else:                
        for k in range(0,len(keyList_2)):            
            if keyList_2[k] in keyList_1:
                avarage = sortedD_2[keyList_2[k]]  + sortedD_2[keyList_2[k]]
                newDictSameWord.update({keyList_2[k]:avarage})
         

    #open new file and write result
    result_2=open("result_2.txt","w",encoding="utf-8") 
    result_2.write("      | total     |  Book 1     |  Book 2     |  word        | \n")
    result_2.write("      | order     |  order      |  order      |  order       | \n")
    result_2.write("      | frequency |  frequency  |  frequency  |  sequence    | \n")
    result_2.write("      --------------------------------------------------------\n\n")
    sortedSameWordD={}
    
    #sort for same words
    sortedSameWord = sorted(newDictSameWord, key=newDictSameWord.get, reverse=True)
    
    for h in sortedSameWord:
        sortedSameWordD[h] = newDictSameWord[h]
    keyAvarage = list( sortedSameWordD.keys())
    
    for g in range(0 , len(keyAvarage)):        
        result_2.write( f"{str( sortedD_1[keyAvarage[g]]+sortedD_2[keyAvarage[g]] ):>12}{str( sortedD_1[keyAvarage[g] ]):>12}{str( sortedD_2[keyAvarage[g] ]):>12}{keyAvarage[g]:>25}")
        result_2.write("\n")
       
    
    result_2.close()        




#call the function
#Word_Order_Frequency_Two_Books(book_1,book_2,Word_Order,File_Output_2)










































