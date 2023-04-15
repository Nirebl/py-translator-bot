from translators import translate_text as ts


def get_translation(text):
    # ru = str(ts.google(text, to_language='ru'))
    # en = str(ts.google(text, to_language='en'))
    # it = str(ts.google(text, to_language='it'))
    # ru = ts(text, translator='google', to_language='ru')
    ru = ts(text, to_language='ru')
    en = ts(text, to_language='en')
    it = ts(text, to_language='it')

    ans = ru + '\n' + en + '\n' + it
    return ans
