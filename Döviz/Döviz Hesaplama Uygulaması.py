import requests

# Popüler döviz birimleri
POPULAR_CURRENCIES = ["USD", "EUR", "TRY", "GBP", "JPY", "CAD", "AUD", "CHF"]

def get_exchange_rate(base_currency, target_currency):
    api_key = "API_KEY23HYBF0UH1X6G2CY5Z8NUN3U8BN8W433"  # Finage API anahtarınızı buraya girin
    url = f"https://api.finage.co.uk/last/forex/{base_currency}{target_currency}?apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        exchange_rate = data["bid"]
        return float(exchange_rate)
    else:
        return None

def show_currencies():
    print("Kullanılabilir döviz kurları:")
    for currency in POPULAR_CURRENCIES:
        print(currency)

def main():
    print("Döviz Hesaplama Uygulaması")
    show_currencies()
    
    base_currency = input("Hangi dövizden çevirmek istersiniz: ").upper()
    target_currency = input("Hangi dövize çevirmek istersiniz: ").upper()

    if base_currency in POPULAR_CURRENCIES and target_currency in POPULAR_CURRENCIES:
        amount = float(input(f"{base_currency} miktarını girin: "))
        exchange_rate = get_exchange_rate(base_currency, target_currency)

        if exchange_rate is not None:
            converted_amount = amount * exchange_rate
            print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            print("Döviz kurları alınamadı. Lütfen tekrar deneyin.")
    else:
        print("Geçersiz döviz birimi girdiniz. Lütfen sadece kullanılabilir döviz birimlerini girin.")

if __name__ == "__main__":
    main()
