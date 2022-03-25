'''Este é o Módulo Principal'''
import ecomerce.produtos
from ecomerce.pagamentos.paypal import  Paypal

def main():
    produto = ecomerce.produtos.Produto()
    print(produto)
    Paypal()

if __name__=="__main__":
    main()