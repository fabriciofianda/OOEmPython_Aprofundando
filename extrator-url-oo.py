import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    def valida_url(self):
        if not self.url:
            raise ValueError("The URL is empty.")
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("Your URL is not Valid.")
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        print("Domain Name [ {} ] ".format(url_base))
        return url_base
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros
    def get_valor_parametro(self, parametro_de_busca):
        indice_parametro = self.get_url_parametros().find(parametro_de_busca)
        indice_valor = indice_parametro + len(parametro_de_busca) + 1
        indice_e = self.get_url_parametros().find('&', indice_valor)

        if indice_e == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e]
        return valor
    def __len__(self):
        return len(self.url)
    def __str__(self):
        return self.url + "\n" + "Parameters - " + self.get_url_parametros() + "\n" + "Domain name - " + self.get_url_base()
    def __eq__(self, other):
        return self.url == other.url

extrator_url = ExtratorURL("http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
extrator_url2 = ExtratorURL("http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
print("The size of URL is: {}".format(len(extrator_url)))
print(extrator_url)
print(extrator_url == extrator_url2)

#valor_quantidade = extrator_url.get_valor_parametro("quantidade")
#print(valor_quantidade)