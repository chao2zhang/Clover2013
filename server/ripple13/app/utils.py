def account_with_kind(kind):
    return '%sAccount' % kind.capitalize()

def static_with_kind(kind):
    return 'img/%s.png' % kind

def static_unbind_with_kind(kind):
    return 'img/%s_unbinded.png' % kind