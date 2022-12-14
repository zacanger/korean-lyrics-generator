import random
import collections
import itertools
import re
import korean


class yong_eon:
    def __init__(self, base, verb, noun_ha, obj):
        self.base = base
        self.verb = verb
        self.noun_ha = noun_ha  # ex) 성공 + -하
        self.obj = obj  # only '-를'
        self.last = self.base[len(self.base) - 1]

    def __repr__(self):
        return self.base


def josa(noun, type_):
    if type_ == 1:
        return noun

    # 이/가
    elif type_ == 2:
        if korean.has_batchim(noun[-1]):
            return noun + "이"
        else:
            if noun == "나":
                noun = "내"
            elif noun == "너":
                noun = "네"
            return noun + "가"

    # '의'
    elif type_ == 3:
        return noun + "의"
    # '을/를'
    elif type_ == 4:
        if korean.has_batchim(noun[-1]):
            return noun + "을"
        else:
            return noun + "를"
    # '은/는'
    elif type_ == 5:
        if korean.has_batchim(noun[-1]):
            return noun + "은"
        else:
            return noun + "는"
    # '이다'
    elif type_ == 6:
        return noun + "이다"
    # '와/과'
    elif type_ == 7:
        if korean.has_batchim(noun[-1]):
            return noun + "과"
        else:
            return noun + "와"


def hwalyong(yong_eon, type_):
    if type_ == 1:
        return yong_eon.base + "다"
    elif type_ == 2:
        if yong_eon.verb:
            return yong_eon.base + "는"
        if korean.has_batchim(yong_eon.last):
            return yong_eon.base + "은"
        tmp = korean.divide(yong_eon.last)
        tmp[2] = "ㄴ"

        return yong_eon.base[:-1] + korean.combine(tmp)

    elif type_ == 3:
        if yong_eon.noun_ha:
            return yong_eon.base[:-1]
        if korean.has_batchim(yong_eon.last):
            return yong_eon.base + "음"
        tmp = korean.divide(yong_eon.last)
        tmp[2] = "ㅁ"

        return yong_eon.base[:-1] + korean.combine(tmp)

    elif type_ == 4:
        return yong_eon.base + "자"
    elif type_ == 5:
        return yong_eon.base + "고 싶다"
    elif type_ == 6:
        if korean.has_batchim(yong_eon.last):
            return yong_eon.base + "으면"

        return yong_eon.base + "면"

    elif type_ == 7:
        return yong_eon.base + "고"


def _myungsa(yong_eon):
    return hwalyong(yong_eon, 3)


# TODO: clean this up with a couple of list comprehensions
yong_eons = [
    yong_eon("가", verb=True, noun_ha=False, obj=False),
    yong_eon("경고하", verb=True, noun_ha=True, obj=True),
    yong_eon("결심하", verb=True, noun_ha=True, obj=True),
    yong_eon("공부하", verb=True, noun_ha=True, obj=True),
    yong_eon("관찰하", verb=True, noun_ha=True, obj=True),
    yong_eon("교육하", verb=True, noun_ha=True, obj=True),
    yong_eon("굳", verb=False, noun_ha=False, obj=False),
    yong_eon("극복하", verb=True, noun_ha=True, obj=True),
    yong_eon("기다리", verb=True, noun_ha=False, obj=True),
    yong_eon("기억하", verb=True, noun_ha=True, obj=True),
    yong_eon("깊", verb=False, noun_ha=False, obj=False),
    yong_eon("나타나", verb=True, noun_ha=False, obj=False),
    yong_eon("넘치", verb=True, noun_ha=False, obj=False),
    yong_eon("노래하", verb=True, noun_ha=True, obj=True),
    yong_eon("놓", verb=True, noun_ha=False, obj=True),
    yong_eon("늙", verb=False, noun_ha=False, obj=False),
    yong_eon("닫히", verb=False, noun_ha=False, obj=False),
    yong_eon("던지", verb=True, noun_ha=False, obj=True),
    yong_eon("떠나", verb=True, noun_ha=False, obj=True),
    yong_eon("똑똑하", verb=False, noun_ha=False, obj=False),
    yong_eon("떨어지", verb=True, noun_ha=False, obj=False),
    yong_eon("마시", verb=True, noun_ha=False, obj=True),
    yong_eon("만나", verb=True, noun_ha=False, obj=True),
    yong_eon("매달리", verb=True, noun_ha=False, obj=False),
    yong_eon("먹", verb=True, noun_ha=False, obj=True),
    yong_eon("멍청하", verb=False, noun_ha=False, obj=False),
    yong_eon("미세하", verb=False, noun_ha=False, obj=False),
    yong_eon("미워하", verb=True, noun_ha=False, obj=True),
    yong_eon("미련하", verb=False, noun_ha=True, obj=False),
    yong_eon("미치", verb=False, noun_ha=False, obj=False),
    yong_eon("배고프", verb=False, noun_ha=False, obj=False),
    yong_eon("배우", verb=True, noun_ha=False, obj=True),
    yong_eon("배부르", verb=False, noun_ha=False, obj=False),
    yong_eon("변하", verb=True, noun_ha=False, obj=False),
    yong_eon("보", verb=True, noun_ha=False, obj=True),
    yong_eon("불행하", verb=False, noun_ha=True, obj=False),
    yong_eon("빌리", verb=True, noun_ha=False, obj=True),
    yong_eon("사과하", verb=True, noun_ha=True, obj=True),
    yong_eon("사라지", verb=True, noun_ha=False, obj=False),
    yong_eon("사랑하", verb=True, noun_ha=True, obj=True),
    yong_eon("선택하", verb=True, noun_ha=True, obj=True),
    yong_eon("성공하", verb=False, noun_ha=True, obj=True),
    yong_eon("순수하", verb=False, noun_ha=False, obj=False),
    yong_eon("승리하", verb=False, noun_ha=True, obj=False),
    yong_eon("시작하", verb=True, noun_ha=True, obj=True),
    yong_eon("식사하", verb=True, noun_ha=True, obj=False),
    yong_eon("실패하", verb=False, noun_ha=True, obj=True),
    yong_eon("아프", verb=False, noun_ha=False, obj=False),
    yong_eon("안내하", verb=True, noun_ha=True, obj=True),
    yong_eon("안전하", verb=False, noun_ha=True, obj=False),
    yong_eon("약속하", verb=True, noun_ha=True, obj=True),
    yong_eon("얘기하", verb=True, noun_ha=True, obj=True),
    yong_eon("어색하", verb=False, noun_ha=False, obj=False),
    yong_eon("여행하", verb=True, noun_ha=True, obj=True),
    yong_eon("열리", verb=False, noun_ha=False, obj=False),
    yong_eon("영원하", verb=False, noun_ha=True, obj=False),
    yong_eon("오", verb=True, noun_ha=False, obj=False),
    yong_eon("완벽하", verb=False, noun_ha=True, obj=False),
    yong_eon("외면하", verb=True, noun_ha=True, obj=True),
    yong_eon("움직이", verb=True, noun_ha=False, obj=False),
    yong_eon("위험하", verb=False, noun_ha=True, obj=False),
    yong_eon("웃", verb=True, noun_ha=False, obj=False),
    yong_eon("이별하", verb=True, noun_ha=True, obj=False),
    yong_eon("인정하", verb=True, noun_ha=True, obj=True),
    yong_eon("자", verb=True, noun_ha=False, obj=False),
    yong_eon("젊", verb=False, noun_ha=False, obj=False),
    yong_eon("좋아하", verb=True, noun_ha=False, obj=True),
    yong_eon("죽", verb=False, noun_ha=False, obj=False),
    yong_eon("지나가", verb=True, noun_ha=False, obj=True),
    yong_eon("작", verb=False, noun_ha=False, obj=False),
    yong_eon("청소하", verb=True, noun_ha=True, obj=True),
    yong_eon("채우", verb=True, noun_ha=False, obj=True),
    yong_eon("치열하", verb=False, noun_ha=False, obj=False),
    yong_eon("키우", verb=True, noun_ha=False, obj=True),
    yong_eon("크", verb=False, noun_ha=False, obj=False),
    yong_eon("태어나", verb=False, noun_ha=False, obj=False),
    yong_eon("패배하", verb=False, noun_ha=True, obj=False),
    yong_eon("행복하", verb=False, noun_ha=True, obj=False),
    yong_eon("후회하", verb=True, noun_ha=False, obj=True),
    yong_eon("흐리", verb=False, noun_ha=False, obj=False),
    yong_eon("흩어지", verb=True, noun_ha=False, obj=False),
]

obj_yong_eons = list(filter(lambda x: x.obj, yong_eons))
verbs = list(filter(lambda x: x.verb, yong_eons))
# TODO: use this
# adjs = list(filter(lambda x: not x.verb, yong_eons))
obj_verbs = list(filter(lambda x: x.obj, verbs))

nouns = list(map(_myungsa, yong_eons))

nouns += [
    "가위",
    "가을",
    "감동",
    "강아지",
    "거울",
    "겨울",
    "고통",
    "과거",
    "관계",
    "국가",
    "군인",
    "굴욕",
    "그것",
    "끝",
    "나",
    "날개",
    "내일",
    "너",
    "노을",
    "눈",
    "눈물",
    "단어",
    "돌멩이",
    "마지막",
    "물",
    "미래",
    "미소",
    "바다",
    "바보",
    "불",
    "비극",
    "사람",
    "산",
    "선생님",
    "소녀",
    "소년",
    "소식",
    "아기",
    "아버지",
    "아침",
    "안부",
    "애교",
    "어른",
    "어머니",
    "어제",
    "얼굴",
    "여름",
    "연극",
    "오늘",
    "우리",
    "원숭이",
    "인생",
    "자식",
    "저녁",
    "죄",
    "죽음",
    "지갑",
    "지식",
    "집",
    "찰나",
    "처음",
    "천재",
    "학교",
    "학생",
    "희극",
]

nouns.sort()


def word_gen(type_):
    # nouns
    if type_ // 10 == 0:
        return josa(random.choice(nouns), type_ % 10) + " "

    # yong_eons without obj
    elif type_ // 10 == 1:
        if type_ % 10 == 4:
            return hwalyong(random.choice(verbs), 4)

        return hwalyong(random.choice(yong_eons), type_ % 10) + " "

    # yong_eons with obj
    elif type_ // 10 == 2:
        if type_ % 10 == 4:
            return hwalyong(random.choice(obj_verbs), 4)

        return hwalyong(random.choice(obj_yong_eons), type_ % 10) + " "


def sentence_gen(seq):
    result = ""
    for s in seq:
        result += word_gen(s)
    return result


sequences = [
    (4, 22, 5, 12, 6),
    (7, 4, 25),
    (16, 17, 16, 12, 5, 6),
    (12, 1),
    (4, 22, 1),
    (3, 5, 6),
    (7, 4, 14),
]


def get_patterns(lines):
    nums = []
    for line in lines:
        maybe = line.strip()
        maybe = re.sub("^(#.*)|(\s*)$", "", maybe)
        if maybe.strip() == "":
            nums.append("\n")
        else:
            num = int(line)
            nums.append(num)

    verses = [
        list(y)
        for x, y in itertools.groupby(nums, lambda z: z == "\n")
        if not x
    ]

    return verses


bad_line_beginning_suffixes = [
    "이",
    "가",
    "을",
    "를",
    "은",
    "는",
    "이다",
    "다",
    "과",
    "와",
    "음",
    "싶다",
    "으면",
    "면",
    "고",
]


def has_uncomfortable_feeling_lines(verse_lyrics):
    verse_lines = verse_lyrics.split("\n")
    for line in verse_lines:
        for suffix in bad_line_beginning_suffixes:
            if line.startswith(suffix + " "):
                return True


def generate_sentences_until_it_fits(verse_length):
    found_lyrics = ""
    found_matches = False
    phrases = {}
    while True:
        phrase = sentence_gen(random.choice(sequences))
        no_whitespace = phrase.replace(" ", "")
        phrases[no_whitespace] = phrase
        phrase_keys = phrases.keys()
        phrases_lengths = (lambda x: [len(i) for i in x])(phrase_keys)

        for i, number in enumerate(phrases_lengths):
            complementary = verse_length - number
            if complementary in phrases_lengths[i:]:
                for p in phrase_keys:
                    if len(p) == number:
                        found_lyrics += phrases[p] + " "
                        break
                for p in phrase_keys:
                    if len(p) == complementary:
                        found_lyrics += phrases[p] + " "
                found_matches = True
                break

        if found_matches is True:
            break

    return found_lyrics


def re_split_verse_lines(verse, verse_l):
    verse_lyrics = verse_l
    res = []
    start = 0

    for idx, line in enumerate(verse):
        inner_res = ""
        if line == 0:
            res.append(res[idx - 1])
        else:
            for hangul_char in verse_lyrics[start:]:
                if len(inner_res.replace(" ", "").strip()) == line:
                    res.append(inner_res.strip())
                    break
                if hangul_char.isspace():
                    start += 1
                inner_res += hangul_char
            start += line

    return "\n".join(res)


def build_verse(verse):
    sylls = sum(verse)
    verse_lyrics = generate_sentences_until_it_fits(sylls)
    formatted_verse_lyrics = re_split_verse_lines(verse, verse_lyrics)
    return formatted_verse_lyrics


def replace_pattern(verses):
    song_lyrics = ""

    for verse in verses:
        formatted_verse_lyrics = build_verse(verse)
        while has_uncomfortable_feeling_lines(formatted_verse_lyrics):
            formatted_verse_lyrics = build_verse(verse)
        song_lyrics += formatted_verse_lyrics + "\n\n"

    return song_lyrics.strip()
