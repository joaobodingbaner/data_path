import pytest

from utils.populate import PopulateParquet

PopulateParquet = PopulateParquet()


def test_tipo_de_valor_diferente_de_buy_ou_sell():
    with pytest.raises(ValueError):
        PopulateParquet.create_parquet_file("asdasd")
