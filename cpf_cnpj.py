from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def criar_novo(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return Doccpf(doc_str)
        elif len(doc_str) == 14:
            return Doccnpj(doc_str)
        elif len(doc_str) == 20:
            pass
        else:
            raise ValueError('Documento inválido')
      
class Doccpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido.')

    def __str__(self):
        return self.format()

    def valida(self, documento):
        if len(documento) == 11:
            validador_cpf = CPF()
            return validador_cpf.validate(documento)
        else:
            return ValueError('Número de digitos inválido.')

    def format(self):
       mascara = CPF()
       return mascara.mask(self.cpf)

class Doccnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido.')

    def __str__(self):
        return self.format()

    def valida(self, documento):
        if len(documento) == 11:
            validador_cnpj = CNPJ()
            return validador_cnpj.validate(documento)
        else:
            return ValueError('Número de digitos inválido.')

    def format(self):
       mascara = CNPJ()
       return mascara.mask(self.cnpj)




    