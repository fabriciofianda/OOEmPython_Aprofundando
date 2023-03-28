
# Entendendo Orientação a Objetos em Python

Esse repositório contém o código utilizado no curso de Orientação a Objetos em Python, onde aprendemos sobre os principais conceitos da programação orientada a objetos utilizando a linguagem Python.


## Conteúdo

No código presente neste repositório, criamos uma classe Conta que representa uma conta bancária. Através desta classe, podemos realizar diversas operações bancárias, como depósitos, saques, transferências e consultas de saldo.
## Métodos e Atributos

Na criação da classe Conta, utilizamos os seguintes métodos e atributos:
## Atributos

- __numero: número da conta bancária (privado)
- __titular: nome do titular da conta bancária (privado)
- __saldo: saldo atual da conta bancária (privado)
- __limite: limite de crédito da conta bancária (privado)
- __codigo_banco: código d
# Resumo

O código em questão é uma classe chamada ExtratorURL que é utilizada para extrair informações de uma URL. Ele possui três métodos principais:

- O método sanitiza_url é utilizado para remover espaços desnecessários de uma URL.
- O método valida_url é utilizado para verificar se a URL é válida, ou seja, se ela corresponde a um padrão definido (neste caso, a URL deve começar com "http://" ou "https://", seguido de "www." (opcional), seguido de "bytebank.com" (opcionalmente com ".br" no final), e terminando com "/cambio").
- O método get_valor_parametro é utilizado para obter o valor de um parâmetro específico na URL.

O código utiliza a biblioteca re para trabalhar com expressões regulares e verificar se a URL corresponde ao padrão definido.


## Detalhamentos

O código começa com a definição da classe ExtratorURL. A classe possui um construtor que recebe uma URL como parâmetro e chama o método sanitiza_url para remover espaços desnecessários da URL. Em seguida, o método valida_url é chamado para verificar se a URL é válida. Se a URL não for válida, uma exceção do tipo ValueError é lançada.

O método sanitiza_url recebe uma URL como parâmetro e verifica se o tipo da URL é str. Se a URL for uma string, o método remove espaços desnecessários utilizando o método strip() e retorna a URL sanitizada. Se a URL não for uma string, o método retorna uma string vazia.

O método valida_url verifica se a URL é válida utilizando expressões regulares. O padrão definido na expressão regular é: a URL deve começar com "http://" ou "https://", seguido de "www." (opcional), seguido de "bytebank.com" (opcionalmente com ".br" no final), e terminando com "/cambio". Se a URL não corresponder ao padrão definido, o método lança uma exceção do tipo ValueError com a mensagem "A URL não é válida".

O método get_valor_parametro recebe como parâmetro o nome de um parâmetro na URL e retorna o valor deste parâmetro. O método utiliza o método find para encontrar o índice do parâmetro na URL e em seguida encontra o índice do valor do parâmetro. Se houver mais de um parâmetro na URL, o método utiliza o método find novamente para encontrar o próximo parâmetro e utiliza o índice encontrado como limite para extrair o valor do parâmetro atual. Se não houver mais parâmetros na URL, o método extrai o valor do parâmetro até o final da URL.

O código finaliza criando uma instância da classe ExtratorURL com uma URL válida e chamando o método get_valor_parametro para obter o valor do parâmetro "quantidade". O valor retornado é então impresso na tela.

Gostaria de expressar minha gratidão pelo trabalho e dedicação como professor no curso de Python. Professor Gabriel Corte Real Saldanhao banco da conta bancária (privado)

## Metodos

- extrato(): exibe o saldo da conta bancária e o nome do titular
- depositar(valor): adiciona um valor ao saldo da conta bancária
- __pode_retirar(valor_de_saque): verifica se é possível realizar um saque na conta bancária
- retirar(valor): realiza um saque na conta bancária
- transferir(valor, origem, destino): transfere um valor de uma conta bancária para outra
- @property
- @property.setter
- @staticmethod
## Funcionamento do código

Ao criar uma instância da classe Conta, é possível realizar diversas operações bancárias. Além disso, também podemos consultar informações da conta, como saldo e número da conta, utilizando os métodos saldo() e numero().

Também é possível modificar o limite de crédito da conta bancária utilizando o método limite().
## Agradecimentos

Agradecimentos ao professor Nico Steppat do curso de Python: entendendo a Orientação a Objetos
Da plataforma Alura