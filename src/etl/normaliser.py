def normalize_year(year):
    year = int(year)

    if year < 1900 or year > 2100:
        raise ValueError("Invalid year")

    return year


def normalize_ticker(ticker):
    if ticker is None:
        return None

    return str(ticker).strip().upper()