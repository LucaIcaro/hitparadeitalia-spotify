import grabber

def main():
    urlPrefix = "https://hitparadeitalia.it/hp_yends/hpe"
    urlSuffix = ".htm"
    yearsRange = range(1947, 2023, 1)
    for year in yearsRange:
        print("*************************")
        print("YEAR ", year)
        print(grabber.grab_songs(urlPrefix + str(year) + urlSuffix))

if __name__ == "__main__":
    main()