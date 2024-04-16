import pinyin_jyutping

from style_bert_vits2.nlp.symbols import PUNCTUATIONS
from pyjyutping import jyutping

from typing import List

j = pinyin_jyutping.PinyinJyutping()


INITIALS = [
    "aa",
    "aai",
    "aak",
    "aap",
    "aat",
    "aau",
    "ai",
    "au",
    "ap",
    "at",
    "ak",
    "a",
    "p",
    "b",
    "e",
    "ts",
    "t",
    "dz",
    "d",
    "kw",
    "k",
    "gw",
    "g",
    "f",
    "h",
    "l",
    "m",
    "ng",
    "n",
    "s",
    "y",
    "w",
    "c",
    "z",
    "j",
    "ong",
    "on",
    "ou",
    "oi",
    "ok",
    "o",
    "uk",
    "ung",
]

def get_jyutping(text: str) -> List[str]:
    converted_text = j.jyutping(text, tone_numbers=True, spaces=True)
    converted_words = converted_text.split()

    for i, word in enumerate(converted_words):
        if set(word) <= set(text) - set(PUNCTUATIONS):
            from style_bert_vits2.nlp.chinese.jyutping_local_mapping import local_mapping

            converted_word = local_mapping.get(word, word)
            if converted_word == word:
                converted_word = jyutping.convert(word)
            converted_words[i] = converted_word
    jyutping_sentence = " ".join(converted_words)

    for symbol in PUNCTUATIONS:
        jyutping_sentence = jyutping_sentence.replace(symbol, " " + symbol + " ")
    jyutping_array = jyutping_sentence.split()

    return jyutping_array


def jyuping_to_initials_finals_tones(jyuping_syllables: List[str]) -> tuple[List[str], List[int], List[int]]:
    initials_finals: List[str] = []
    tones: List[int] = []
    word2ph: List[int] = []

    for syllable in jyuping_syllables:
        if syllable in PUNCTUATIONS:
            initials_finals.append(syllable)
            tones.append(0)
            word2ph.append(1)  # Add 1 for punctuation
        elif syllable == "_":
            initials_finals.append(syllable)
            tones.append(0)
            word2ph.append(1)  # Add 1 for underscore
        else:
            try:
                tone = int(syllable[-1])
                syllable_without_tone = syllable[:-1]
            except ValueError:
                tone = 0
                syllable_without_tone = syllable

            for initial in INITIALS:
                if syllable_without_tone.startswith(initial):
                    if syllable_without_tone.startswith("nga"):
                        initials_finals.extend(
                            [
                                syllable_without_tone[:2],
                                syllable_without_tone[2:] or syllable_without_tone[-1],
                            ]
                        )
                        tones.extend([tone, tone])
                        word2ph.append(2)
                    else:
                        final = syllable_without_tone[len(initial) :] or initial[-1]
                        initials_finals.extend([initial, final])
                        tones.extend([tone, tone])
                        word2ph.append(2)
                    break
    assert len(initials_finals) == len(tones)
    return initials_finals, tones, word2ph

def g2p(text: str) -> tuple[List[str], List[int], List[int]]:
    word2ph: List[int] = []
    jyuping = get_jyutping(text)
    # print(jyuping)
    phones: List[str]
    tones: List[int]
    phones, tones, word2ph = jyuping_to_initials_finals_tones(jyuping)
    print(phones, tones, word2ph)
    phones = ["_"] + phones + ["_"]
    tones = [0] + tones + [0]
    word2ph = [1] + word2ph + [1]
    print(phones, tones, word2ph)
    return phones, tones, word2ph


if __name__ == "__main__":
    from style_bert_vits2.nlp.chinese.bert_feature import extract_bert_feature
    from style_bert_vits2.nlp.chinese.normalizer import normalize_text

    text = "啊！但是《原神》是由,米哈游自主，  [研发]的一款全.新开放世界.冒险游戏"
    text = normalize_text(text)
    print(text)
    phones, tones, word2ph = g2p(text)
    bert = extract_bert_feature(text, word2ph, "cuda")

    print(phones, tones, word2ph, bert.shape)


# 示例用法
# text = "这是一个示例文本：,你好！这是一个测试...."
# print(g2p_paddle(text))  # 输出: 这是一个示例文本你好这是一个测试
