import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
remuneracao = list()
data = ["2019-08", "2019-09", "2019-10", "2019-11", "2019-12", "2020-01", "2020-02", "2020-03", "2020-04", "2020-05",
      "2020-06", "2020-07", "2020-08", "2020-09", "2020-10", "2020-11", "2020-12", "2021-01", "2021-02", "2021-03",
      "2021-04", "2021-05", "2021-06", "2021-07"]
for i in data:
    url = "https://www.al.sp.gov.br/repositorio/folha-de-pagamento/folha-{}-detalhada.html".format(i)
    pg_deputado = requests.get(url)
    salario = bs(pg_deputado.content, "html.parser")
    tbody = salario.find("tbody")
    for tr in tbody.find_all("tr"):
        dicio = dict()
        dicio["data"] = i
        dicio["servidor"] = tr.find_all("td")[0].text
        dicio["remuneracao_rruta"] = tr.find_all("td")[1].text
        dicio["remuneracao_liquida"] = tr.find_all("td")[2].text
        dicio["tributos"] = tr.find_all("td")[3].text
        dicio["abono_de_permanencia"] = tr.find_all("td")[4].text
        dicio["ferias_desconto"] = tr.find_all("td")[5].text
        dicio["ferias_liquida"] = tr.find_all("td")[6].text
        dicio["13_bruto"] = tr.find_all("td")[7].text
        dicio["13_desconto"] = tr.find_all("td")[8].text
        dicio["13_liquido"] = tr.find_all("td")[9].text
        dicio["retroativo_bruto"] = tr.find_all("td")[10].text
        dicio["retroativo_descontoo"] = tr.find_all("td")[11].text
        dicio["retroativo_liquido"] = tr.find_all("td")[12].text
        dicio["outros_bruto"] = tr.find_all("td")[13].text
        dicio["outros_desconto"] = tr.find_all("td")[14].text
        dicio["indenizacao"] = tr.find_all("td")[15].text
        remuneracao.append(dicio)
print(remuneracao)
df = pd.DataFrame.from_dict(remuneracao)
df.to_csv("trabalho_final.csv", index=False)
