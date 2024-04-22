from bs4 import BeautifulSoup

with open('my.html','r') as html_file:
    content=html_file.read()
    #print(content)
    soup = BeautifulSoup(content,'html.parser')
    # print(soup.prettify())

    #find only one tag
    # tag = soup.find('h1')
    # print(tag)

    #find all tages if you want and must be present in  our html file
    # tags = soup.find_all('h2')
    # for tag in tags:
        # print(tag.text)

    #____
    pages = soup.find_all('section')
    for page in pages:
        # print(page)
        #print(page.h2)
        # card_tag = page.h2.text.split()[-1]
        card_tag = page.h2.text
        card_p = page.p.text
        # pring using f string method 
        print(f' The page is {card_tag} and its detail {card_p}')