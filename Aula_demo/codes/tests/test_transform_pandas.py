import pytest
import os 
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

print (currentdir)
print (parentdir)

from transform.process_local_pandas import TransformLocal

a = TransformLocal(account_number="asdasd")
print (a.dir_path)

a.read_json_local_file("example_bitcoin.json")

# @pytest.fixture
# def restaurante_fila_vazia():
#     return Restaurante("Pizzaria X")


# @pytest.fixture
# def restaurante_com_um_pedido_na_fila():
#     return Restaurante("Pizzaria X", 1)


# def test_pedidos_na_fila_valor_inicial_padrao_igual_a_zero(restaurante_fila_vazia):
#     assert restaurante_fila_vazia.pedidos_na_fila == 0


# def test_pedidos_na_fila_valor_inicial_maior_que_zero(restaurante_com_um_pedido_na_fila):
#     assert restaurante_com_um_pedido_na_fila.pedidos_na_fila == 1


# def test_pedidos_na_fila_valor_inicial_menor_que_zero():
#     with pytest.raises(ValueError):
#         Restaurante("Pizzaria X", -1)


# def test_adiciona_um_pedido_na_fila(restaurante_com_um_pedido_na_fila):
#     restaurante_com_um_pedido_na_fila.adiciona_pedido()
#     assert restaurante_com_um_pedido_na_fila.pedidos_na_fila == 2


# def test_remove_um_pedido_na_fila(restaurante_com_um_pedido_na_fila):
#     restaurante_com_um_pedido_na_fila.remove_pedido()
#     assert restaurante_com_um_pedido_na_fila.pedidos_na_fila == 0


# def test_remove_um_pedido_na_fila_vazia(restaurante_fila_vazia):
#     restaurante_fila_vazia.remove_pedido()
#     assert restaurante_fila_vazia.pedidos_na_fila == 0


# @pytest.mark.parametrize("inicial,final", [(0,0), (1,0), (3,1)])
# def test_remocao_de_pedidos(inicial,final):
#     restaurante = Restaurante("Pizzaria X", inicial)
#     restaurante.remove_pedido()
#     assert restaurante.pedidos_na_fila == final
