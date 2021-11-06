from bs4 import BeautifulSoup

html = """
<html><body>
    <h1> スクレイピングとは</h1>
    <p>Webページを解析すること</p>
    <p>任意の箇所を抽出すること</p>
    </body></html>
"""

#HTMLを解析する
soup = BeautifulSoup(html, 'html.parser')

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

print("h1 = " + h1.string)
print("p = " + p1.string)
print("p = " + p2.string)




#任意の部分を抽出する
#links = soup.find_all("a")

#show all link
#for a in links:
#    href = a.attrs['href']
#    text = a.string 
#    print(text, ">", href)