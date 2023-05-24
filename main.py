from Comprador import Comprador
from Lance import Lance
from Leilao import Leilao
from Produto import Produto
from funcoes_auxiliares import pegar_valor
import time

regras = {'tempo-de-lance': 10}

monalisa = Produto('Mona Lisa', 1_000, 0)
computador_de_isaque = Produto('Dell Inspiron', 2.50, 1)
todinho = Produto('Toddynho', 2_500, 2)

produtos = [monalisa, computador_de_isaque, todinho]

edilson = Comprador('Edilson Júnior', 69)
danilo = Comprador('Danilo Góis', 13)
davi = Comprador('Davi Lucas', 14)

compradores = [edilson, davi, danilo]

leilao = Leilao(produtos, compradores, regras)

comprador = None

for produto in leilao.produtos:
  print(f'O produto que está sendo leiloado é {produto.nome}')
  print(f'Valor inicial: R${produto.lance_inicial}')
  print('--=--' * 5, end='\n\n')

  leilao.resetar_lances(produto)

  while True:
    ultimo_lance = leilao.lances[-1].valor

    id_comprador = int(
      pegar_valor(lambda id_comprador, funcao: funcao(id_comprador) != None,
                  'Digite o número do comprador. ', leilao.pesquisar_id))

    novo_valor = float(
      pegar_valor(lambda novo_valor: novo_valor > ultimo_lance.valor,
                  'Digite o valor do novo lance. '))

    if leilao.checar_tempo_do_lance() == True:
      leilao.conceder_lance(ultimo_lance)
      break

    leilao.dar_lance(comprador, produto, novo_valor)

  print()

  if leilao.lances[-1].aceito:
    print(
      f'O produto {produto.nome} foi vendido para {comprador.nome}, de número {comprador.id}',
      end='\n\n')


def pegar_valor(condicao, mensagem, funcao):
  while True:
    valor = input(mensagem)

    if condicao(valor, funcao) == True:
      return valor
    else:
      print('-=-= Erro. Digite outro valor. =-=-')
  