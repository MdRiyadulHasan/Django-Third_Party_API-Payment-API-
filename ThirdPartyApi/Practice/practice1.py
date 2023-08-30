import pycountry

def get_full_country_name(short_code):
    try:
        country = pycountry.countries.get(alpha_2=short_code)
        if country:
            return country.name
        else:
            return "Country not found"
    except AttributeError:
        return "Invalid short code"

# Example usage
short_code = "BD"
full_name = get_full_country_name(short_code)
print(f"Full name for {short_code}: {full_name}")
