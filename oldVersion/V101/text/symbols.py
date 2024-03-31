punctuation = ["!", "?", "…", ",", ".", "'", "-"]
pu_symbols = punctuation + ["SP", "UNK"]
pad = "_"

# chinese
zh_symbols = [
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
num_zh_tones = 6

# japanese
ja_symbols = [
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
num_ja_tones = 2

# English
en_symbols = [
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
num_en_tones = 4

# combine all symbols
normal_symbols = sorted(set(zh_symbols + ja_symbols + en_symbols))
symbols = [pad] + normal_symbols + pu_symbols
sil_phonemes_ids = [symbols.index(i) for i in pu_symbols]

# combine all tones
num_tones = num_zh_tones + num_ja_tones + num_en_tones

# language maps
language_id_map = {"ZH": 0, "JP": 1, "EN": 2}
num_languages = len(language_id_map.keys())

language_tone_start_map = {
    "ZH": 0,
    "JP": num_zh_tones,
    "EN": num_zh_tones + num_ja_tones,
}

if __name__ == "__main__":
    a = set(zh_symbols)
    b = set(en_symbols)
    print(sorted(a & b))
