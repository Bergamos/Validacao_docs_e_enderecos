from tkinter import N
from cpf_cnpj import Documento
from telefones_br import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

#Documentos
cpf = '10769223680'
cnpj = '02836337000169'
doc_pf = Documento.criar_novo(10769223680)
doc_pj = Documento.criar_novo('02836337000169')
print(doc_pf)
print(doc_pj)

#Telefones
telefone = '05521972841996'
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

#Datas
data_cadastro = DatasBr()
print(data_cadastro.tempo_cadastro())

#Cep
cep = 36037550
objeto_cep = BuscaEndereco(cep)
logradouro, bairro, localidade, uf = objeto_cep.acessa_via_cep()
print(f'{logradouro}, {bairro}, {localidade}-{uf}')