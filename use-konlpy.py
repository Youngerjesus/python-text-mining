from konlpy.tag import Mecab

def tokenizer(text):
    nouns = mecab.nouns(text)
    # 불용어를 처리하는 작업도 추가하면 좋다.
    return [noun for noun in nouns if len(noun) > 1]

sample = "[서울=뉴시스] 이준호 기자 = 경찰이 한강에서 숨진 채 발견된 대학생 A(22)씨의 아버지가 26일 입장문을 통해 경찰 수사가 미흡했다고 주장한 것과 관련, 수사 일부 과정을 공개하며" \
         "실체적 진실을 밝히기 위해 최선을 다하고 있다고 반박했다." \
         "서울 서초경찰서는 이날 관련자들의 진술을 청취하고 폐쇄회로(CC)TV를 분석하는 등 사실관계 확인을 위한 조사가 진행 중인 관계로 구체적인 내용은 답변드리지 못한다고 하면서도, A씨 실종 이후 친구 B씨에 대한 조사 내역을 공개했다." \
         "또 이달 9일에도 B씨를 조사했고, 12일 B씨와 프로파일러 면담에 이어 14일과 22일 등 총 4회 조사했다고 전했다. B씨의 부모도 각각 2회, 1회 조사했다고 경찰은 밝혔다."

mecab = Mecab()
# print(mecab.pos(sample)[:10])
# print(mecab.nouns(sample))
# print(mecab.morphs(sample))

print(tokenizer(sample))

