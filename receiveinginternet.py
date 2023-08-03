import urllib.request
def main():
     weburl1 = urllib.request.urlopen("http://www.google.com")
     print("result code:" , weburl1.getcode())
     data = weburl1.read()
     print(data)
     
if __name__ == "__main__" :
    main()    