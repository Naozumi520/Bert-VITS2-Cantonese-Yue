# Punctuations
PUNCTUATIONS = ["!", "?", "…", ",", ".", "'", "-"]

# Punctuations and special tokens
PUNCTUATION_SYMBOLS = PUNCTUATIONS + ["SP", "UNK"]

# Padding
PAD = "_"

# Chinese symbols
ZH_SYMBOLS = [
    "a",
    "aa",
    "aai",
    "aak",
    "aam",
    "aan",
    "aang",
    "aap",
    "aat",
    "aau",
    "ai",
    "ak",
    "am",
    "an",
    "ang",
    "ap",
    "at",
    "au",
    "b",
    "c",
    "d",
    "e",
    "ei",
    "ek",
    "eng",
    "eoi",
    "eon",
    "eot",
    "eu",
    "em",
    "en",
    "ep",
    "et",
    "f",
    "g",
    "gw",
    "h",
    "i",
    "ik",
    "im",
    "in",
    "ing",
    "ip",
    "it",
    "iu",
    "j",
    "k",
    "kw",
    "l",
    "m",
    "n",
    "ng",
    "o",
    "oe",
    "oek",
    "oeng",
    "oi",
    "ok",
    "on",
    "ong",
    "ot",
    "ou",
    "p",
    "s",
    "sil",
    "sp",
    "spl",
    "t",
    "u",
    "ui",
    "uk",
    "un",
    "ung",
    "ut",
    "w",
    "yu",
    "yun",
    "yut",
]
NUM_ZH_TONES = 6

# Japanese
JP_SYMBOLS = [
    "N",
    "a",
    "a:",
    "b",
    "by",
    "ch",
    "d",
    "dy",
    "e",
    "e:",
    "f",
    "g",
    "gy",
    "h",
    "hy",
    "i",
    "i:",
    "j",
    "k",
    "ky",
    "m",
    "my",
    "n",
    "ny",
    "o",
    "o:",
    "p",
    "py",
    "q",
    "r",
    "ry",
    "s",
    "sh",
    "t",
    "ts",
    "ty",
    "u",
    "u:",
    "w",
    "y",
    "z",
    "zy",
]
NUM_JP_TONES = 2

# English
EN_SYMBOLS = [
    "aa",
    "ae",
    "ah",
    "ao",
    "aw",
    "ay",
    "b",
    "ch",
    "d",
    "dh",
    "eh",
    "er",
    "ey",
    "f",
    "g",
    "hh",
    "ih",
    "iy",
    "jh",
    "k",
    "l",
    "m",
    "n",
    "ng",
    "ow",
    "oy",
    "p",
    "r",
    "s",
    "sh",
    "t",
    "th",
    "uh",
    "uw",
    "V",
    "w",
    "y",
    "z",
    "zh",
]
NUM_EN_TONES = 4

# Combine all symbols
NORMAL_SYMBOLS = sorted(set(ZH_SYMBOLS + JP_SYMBOLS + EN_SYMBOLS))
SYMBOLS = [PAD] + NORMAL_SYMBOLS + PUNCTUATION_SYMBOLS
SIL_PHONEMES_IDS = [SYMBOLS.index(i) for i in PUNCTUATION_SYMBOLS]

# Combine all tones
NUM_TONES = NUM_ZH_TONES + NUM_JP_TONES + NUM_EN_TONES

# Language maps
LANGUAGE_ID_MAP = {"ZH": 0, "JP": 1, "EN": 2}
NUM_LANGUAGES = len(LANGUAGE_ID_MAP.keys())

# Language tone start map
LANGUAGE_TONE_START_MAP = {
    "ZH": 0,
    "JP": NUM_ZH_TONES,
    "EN": NUM_ZH_TONES + NUM_JP_TONES,
}


if __name__ == "__main__":
    a = set(ZH_SYMBOLS)
    b = set(EN_SYMBOLS)
    print(sorted(a & b))
