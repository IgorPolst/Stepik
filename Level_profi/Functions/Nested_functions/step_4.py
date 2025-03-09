from datetime import date


def date_formatter(country_code):
    def format(date):
        d = {
            "ru": "%d.%m.%Y",
            "us": "%m-%d-%Y",
            "ca": "%Y-%m-%d",
            "br": "%d/%m/%Y",
            "fr": "%d.%m.%Y",
            "pt": "%d-%m-%Y",
        }
        return date.strftime(d[country_code])

    return format


date_ru = date_formatter("ru")
today = date(2015, 12, 7)
print(date_ru(today))
