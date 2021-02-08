from notification.locales import ptBR, enUS

locales = {
    'enUS': enUS.locale,
    'ptBR': ptBR.locale
}


def get_translation(lang_id, comp, msg_id):
    if lang_id in locales and comp in locales[lang_id] and msg_id in locales[lang_id][comp]:
        return locales[lang_id][comp][msg_id]
    else:
        return locales['enUS'][comp][msg_id]





