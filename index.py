import random
import json
import markdown
from bs4 import BeautifulSoup
# loading json file
f=open("quotes.json")
quotes=json.load(f)

# to choose a random quote 
quote=random.choice(quotes)

with open("README.md",mode="r",encoding="utf8") as f:
    readme_text=f.read()

#finding tag
readme_text
opening_tag="<p quote"
closing_tag="</p quote"

start_index=readme_text.index(opening_tag)
end_index=readme_text.index(closing_tag)

quotemarkdown="<p quote align='center'>"+quote["text"]+"</p quote>"

content=readme_text[start_index+len(opening_tag):end_index]
new_content=readme_text[:start_index]+quotemarkdown+readme_text[end_index+len(closing_tag)+1:]

#writing into readme file
readme_file=open("README.md",mode="w",encoding="utf8",)
readme_file.write(new_content)