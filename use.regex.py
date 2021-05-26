import re
reg = re.compile("[a-zA-Z0-9]+@[a-z,A-Z,0-9]+(\.co\.kr|\.com|\.co)")
email = "yjm950516@gmail.com"

print(reg.search(email))

req = re.compile("\[.*?\]|\(.*?\)")
text = "faslfkjaslf(falskfjasjlkf.fajsfkloalj)"
text2 = "gajldksgjalsg(fjaslkfjafj) faklfjaslfj(fajklsfja) fasjklfasjl(mgmggmglm)"
print(req.sub("", text2))

req = re.compile("\S.+?다\.")
sentence = "표현식의 다양한 특수기호(패턴)는 그 기호의 의미(기능)와 매칭되어 인식되지 않기 때문에 따로 외우지 않으면 의미를 파악할 수가 없습니다."
print(req.findall(sentence))

