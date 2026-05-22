import re

def has_keyword(config,keyword):
    return keyword in config

def interface_has_keyword(config,interface,keyword):
    pattern = rf"{interface}.*{keyword}"
    return bool(re.search(pattern, config, re.DOTALL))