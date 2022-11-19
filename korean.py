# 12593~12622
# ㄱㄲㄳㄴㄵㄶㄷㄸㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅃㅄㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ

# 12623~12643
# ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ

# (ord(t) - 44032) // 588 -> 초성
# ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ
# 가 44032
# 까 44620
# 나 45208
# 다 45796
# 따 46384

# ((ord(t) - 44032) % 588) // 28 -> 중성
# 가개갸걔거게겨계고과괘괴교구궈궤귀규그긔기
# 가 44032
# 개 44060
# 갸 44088
# 걔 44116
# 거 44144

# ((ord(t) - 44032) % 588) % 28 -> 종성
# 가각갂갃간갅갆갇갈갉갊갋갌갍갎갏감갑값갓갔강갖갗갘같갚갛

cho = (
    "ㄱ",
    "ㄲ",
    "ㄴ",
    "ㄷ",
    "ㄸ",
    "ㄹ",
    "ㅁ",
    "ㅂ",
    "ㅃ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅉ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
)

joong = (
    "ㅏ",
    "ㅐ",
    "ㅑ",
    "ㅒ",
    "ㅓ",
    "ㅔ",
    "ㅕ",
    "ㅖ",
    "ㅗ",
    "ㅘ",
    "ㅙ",
    "ㅚ",
    "ㅛ",
    "ㅜ",
    "ㅝ",
    "ㅞ",
    "ㅟ",
    "ㅠ",
    "ㅡ",
    "ㅢ",
    "ㅣ",
)

jong = (
    None,
    "ㄱ",
    "ㄲ",
    "ㄳ",
    "ㄴ",
    "ㄵ",
    "ㄶ",
    "ㄷ",
    "ㄹ",
    "ㄺ",
    "ㄻ",
    "ㄼ",
    "ㄽ",
    "ㄾ",
    "ㄿ",
    "ㅀ",
    "ㅁ",
    "ㅂ",
    "ㅄ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
)

ja = (
    "ㄱ",
    "ㄲ",
    "ㄳ",
    "ㄴ",
    "ㄵ",
    "ㄶ",
    "ㄷ",
    "ㄸ",
    "ㄹ",
    "ㄺ",
    "ㄻ",
    "ㄼ",
    "ㄽ",
    "ㄾ",
    "ㄿ",
    "ㅀ",
    "ㅁ",
    "ㅂ",
    "ㅃ",
    "ㅄ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅉ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
)

mo = joong


def divide(char):
    ord_ = ord(char)

    if ord_ < 44032 or ord_ > 55203:
        return [char]

    ord_ -= 44032

    return [
        cho[ord_ // 588],
        joong[(ord_ % 588) // 28],
        jong[(ord_ % 588) % 28],
    ]


def has_batchim(char):
    return 0 != ((ord(char) - 44032) % 588) % 28


# chars -> [cho, joong, jong]
def combine(chars):
    if len(chars) == 1:
        return chars[0]
    if type(chars) == tuple:
        chars = list(chars)
    if len(chars) == 2:
        chars.append(None)

    return chr(
        cho.index(chars[0]) * 588
        + joong.index(chars[1]) * 28
        + jong.index(chars[2])
        + 44032
    )
