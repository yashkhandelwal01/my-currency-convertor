import requests

API_key="LR05788T4FU1TY3P"
a={"AED":"United Arab Emirates Dirham",
"AFN":"Afghan Afghani",
"ALL":"Albanian Lek",
"AMD":"Armenian Dram",
"ANG":"Netherlands Antillean Guilder",
"AOA":"Angolan Kwanza",
"ARS":"Argentine Peso",
"AUD":"Australian Dollar",
"AWG":"Aruban Florin",
"AZN":"Azerbaijani Manat",
"BRL":"Brazilian Real",
"CAD":"Canadian Dollar",
"CHF":"Swiss Franc",
"CNH":"Chinese Yuan Offshore",
"CNY":"Chinese Yuan",
"COP":"Colombian Peso",
"CUP":"Cuban Peso",
"CZK":"Czech Republic Koruna",
"DJF":"Djiboutian Franc",
"DKK":"Danish Krone",
"EGP":"Egyptian Pound",
"EUR":"Euro",
"GBP":"British Pound Sterling",
"HKD":"Hong Kong Dollar",
"HRK":"Croatian Kuna",
"HUF":"Hungarian Forint",
"IDR":"Indonesian Rupiah",
"ILS":"Israeli New Sheqel",
"INR":"Indian Rupee",
"IRR":"Iranian Rial",
"ISK":"Icelandic Krona",
"JPY":"Japanese Yen",
"KHR":"Cambodian Riel",
"KMF":"Comorian Franc",
"KPW":"North Korean Won",
"KRW":"South Korean Won",
"KWD":"Kuwaiti Dinar",
"LKR":"Sri Lankan Rupee",
"LRD":"Liberian Dollar",
"LSL":"Lesotho Loti",
"LYD":"Libyan Dinar",
"MAD":"Moroccan Dirham",
"MUR":"Mauritian Rupee",
"MVR":"Maldivian Rufiyaa",
"MWK":"Malawian Kwacha",
"MXN":"Mexican Peso",
"MYR":"Malaysian Ringgit",
"NOK":"Norwegian Krone",
"NPR":"Nepalese Rupee",
"NZD":"New Zealand Dollar",
"OMR":"Omani Rial",
"PAB":"Panamanian Balboa",
"PEN":"Peruvian Nuevo Sol",
"PHP":"Philippine Peso",
"PKR":"Pakistani Rupee",
"PLN":"Polish Zloty",
"PYG":"Paraguayan Guarani",
"QAR":"Qatari Rial",
"RON":"Romanian Leu",
"RSD":"Serbian Dinar",
"RUB":"Russian Ruble",
"RUR":"Old Russian Ruble",
"RWF":"Rwandan Franc",
"SAR":"Saudi Riyal",
"SEK":"Swedish Krona",
"SGD":"Singapore Dollar",
"SZL":"Swazi Lilangeni",
"THB":"Thai Baht",
"TJS":"Tajikistani Somoni",
"TRY":"Turkish Lira",
"TWD":"New Taiwan Dollar",
"UAH":"Ukrainian Hryvnia",
"USD":"United States Dollar",
"UYU":"Uruguayan Peso",
"UZS":"Uzbekistan Som",
"VND":"Vietnamese Dong",
"VUV":"Vanuatu Vatu",
"WST":"Samoan Tala",
"XAF":"CFA Franc BEAC",
"XCD":"East Caribbean Dollar",
"XDR":"Special Drawing Rights",
"XOF":"CFA Franc BCEAO",
"XPF":"CFP Franc",
"YER":"Yemeni Rial",
"ZAR":"South African Rand",
"ZMW":"Zambian Kwach",
"ZWL":"Zimbabwean Dollar",}

print("welcome to my python project")
print("in this you can convert a currency into an another currency at live exchange rates")

print("choose a currency from below")
for k,v in a.items():
    print(k,v)
print("choose the currency you wanted to convert")
print("while entering the currency use it initails like INR")
b=input()
#the currency that needed to be converted
if b not in a.keys():
    print("Invalid input")
else:
    print("Now enter the currency you want to convert")
    c=input()
    # currency in which it needed to convert
    if c not in a.keys():
        print("Invalid input")
    else:
        base_url="https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
        main_url=base_url+"&from_currency="+b+"&to_currency="+c+"&apikey="+API_key
        e=requests.get(main_url)
        f=e.json()
        #trying to get realtime information from website
        g=f["Realtime Currency Exchange Rate"]
        rate=g['5. Exchange Rate']
        #realtime rate
        h='1'+" "+b+"="+rate+" "+c
        print("this is realtime exchange rate")
        print(h)
        #realtime rate
        print("enter the amount you want to convert")
        print("give only integer values")
        d=int(input())#amount converted
        j=float(rate)*(d)#required conversion
        l="="
        print(d,b,l,j,c)#this will print our required result
        print("thankyou for using this program")