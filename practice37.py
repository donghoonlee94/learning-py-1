from bs4 import BeautifulSoup # type: ignore
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())