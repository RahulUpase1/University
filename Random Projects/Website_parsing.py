from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/xfx-radeon-rx-6800-xt-rx-68xtalfd9/p/N82E16814150848?Description=amd%206800xt&cm_re=amd_6800xt-_-14-150-848-_-Product&quicklink=true"
results = requests.get(url)
doc = BeautifulSoup(results.text, "html.parser")
randomtext = doc.find_all(text="$")
parent = randomtext[0].parent
strong = parent.find("strong")
print(strong.string)