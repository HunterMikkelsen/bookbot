def get_num_words(book_contents):
    return len(book_contents.split())

def get_num_chars(text):
    charlist = []
    text = text.lower()

    for word in text.split():
        for char in word:
            match_found = False
            for item in charlist:
                if item["char"] == char:
                    item["num"] += 1
                    match_found = True
                    break
            if match_found is False:
                charlist.append({"char": char, "num": 1})
                
                
    return charlist

def sort_on(items):
    return items["num"]

def print_report(listofchars):
    listofchars.sort(reverse=True, key=sort_on)
    for dictionary in listofchars:
        print(f"{dictionary["char"]}: {dictionary["num"]}")