def sourcetemplate(url):
    def query_string(**kwargs):
        text = url + "?"
        for key, value in sorted(kwargs.items()):
            text += f"{key}={value}&"
        return text[:-1]

    return query_string

url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))