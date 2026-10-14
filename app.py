from models.restaurantes import Restaurante
from models.cardapio.bebidas import Bebida
from models.cardapio.prato import Prato 

restaurante_praca = Restaurante('praca','gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho',2.0,'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_item(bebida_suco)
restaurante_praca.adicionar_item(prato_paozinho)
restaurante_praca.receber_avaliacao('Bozo',4)
restaurante_praca.receber_avaliacao('Vovo Mafalda',2)

def main():
    #restaurante_praca.exibir_cardapio
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
