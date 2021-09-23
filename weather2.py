import requests
import urllib.request
# setup to show connection to website openweathermap.org
webUrl = urllib.request.urlopen("http://openweathermap.org/")
print("result code: " + str(webUrl.getcode()) + "\n200 equals connected")

def get_web_data(zip=None, city=None):
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?units=imperial"
    # api id from email for openweathermap.org
    apiid = "eb1289af203d47ead9f0cc6b8c377926"

    # check for Zip or not
    if zip is not None:
        # us represents end id for usa country
        baseUrl += "&zip="+str(zip)+",us"

    else:
        baseUrl += "&q="+str(city)+",us"
    # connect API to website
    baseUrl += "&appid="+str(apiid)
    # make get requests using requests module
    r = requests.get(baseUrl)
    # return the response
    return r

# show data in readable format


def display(resp):
    # this shows read was successful
    if resp.status_code == 200:
        data = resp.json()
        print(f"""{data['name']} Weather Forecast:
        Type: {data['weather'][0]['description']}
        Wind Speed : {data['wind']['speed']} miles/hr
        Visibility : {data['visibility']} m
        Min. Temp : {data['main']['temp_min']} F
        Max Temp : {data['main']['temp_max']} F
        """)
    else:
        print("Request Failed, Error : ", resp.status_code)


def main():
    while True:
        # ask the user for choice
        choice = int(
        input("How do you want to search ? :\n1. By Zip Code\n2. By City Name\n3. Exit\n: "))

        if choice == 1:

            try:
                # for zip code
                zCode = int(input("Enter zip code : "))
                # fetch data from website
                resp = get_web_data(zCode, None)
                display(resp)
            except Exception as ex:
                print("Error : ", ex)
        elif choice == 2:
            try:
                cname = input("Enter city name : ")
                # make call to fetch data
                resp = get_web_data(None, cname)
                display(resp)
            except Exception as ex:
                print("Error : ", ex)
        elif choice == 3:
            break
        else:
            print("Invalid Choice..\n")


if __name__ == "__main__":
    main()