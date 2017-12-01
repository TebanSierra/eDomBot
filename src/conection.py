import requests, json

VALID_RESOURCES = ["citizen", "citizenship", "party", "laws", "newspaper", "articles", "article", "map", "travel",
                   "resources", "battles", "milranks"]
URL_BASE = "https://www.edominations.com/en/api2"
RESOURCE=""
ID=""


def request_res(res, id):
    RESOURCE=res
    ID=id
    URL= URL_BASE + "/" + RESOURCE + "/" + ID

    r = requests.get(URL)

    ans = json.loads(r.text)

    print("Ans: \n")
    print(ans)

res = input("Ingrese el recurso a consultar: ")
id = input("Ingrese el ID del recurso: ")
valid_res = False

while(not valid_res):
    if(res in VALID_RESOURCES):
        valid_res = True
    else:
        print("Recurso solicitado no valido.")
        res = input("Ingrese el recurso a consultar:")

request_res(res, id)
