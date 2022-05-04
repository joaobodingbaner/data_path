import pytest
from pandas.testing import assert_frame_equal
import pandas as pd

from transform.process_local_pandas import TransformLocal
from _utils import (
    get_df_bitcoin_trade
)

TransformLocal = TransformLocal()

@pytest.fixture
def dataframe_bitcoin_trade():
    return get_df_bitcoin_trade()


def test_dataframe_apenas_com_trades_buy(dataframe_bitcoin_trade):
    expected_df = pd.DataFrame({'amount': [0.0177606], 'date': [1501871387], 'price': [9735], 'tid': [739719], 'type': ["buy"]})
    result_df = TransformLocal.filter_df(df = dataframe_bitcoin_trade, type_column_name = "type", type_value = "buy")

    assert_frame_equal(result_df, expected_df)


def test_dataframe_apenas_com_trades_sell(dataframe_bitcoin_trade):
    expected_df = pd.DataFrame({'amount': [0.002], 'date': [1501871382], 'price': [9723], 'tid': [739718], 'type': ["sell"]})
    result_df = TransformLocal.filter_df(df = dataframe_bitcoin_trade, type_column_name = "type", type_value = "sell")

    assert_frame_equal(result_df, expected_df)



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
