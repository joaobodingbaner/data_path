# Datalake
```
 Datalake são dados não estruturados, pode-se fazer uma analogia com o s3

 Block storage - Um arquivão que não dá pra mexer, se quiser alterar será deletar e escrever denovo

 Existem datalake que são montados em cima de datastorage (Azure)

 No datalake não é possivel abrir o dado de uma forma simples, fácil ou boa.
```

# Datawarehouse
```
Datawarehouse são vários bancos de dados com estruturas diferentes,

Basicamente subir um banco de dados local na maquina, linkado a file storage

Row format, basicamente backend
```

# LakeHouse
```
Misto de Datalake com DataWarehouse, dá uma cara de DataWarehouse para o Datalake.

Coloca uma abstração em cima do datalake, por exemplo Apache Hudi. Que faz com que não seja necessário repetição de ação (query não rodar por conta da tabela estar atualizando)

Camada de metadados em cima dos dados.

```


# Niveis de dados
```
A ponto de otimização de custo, a niveis de storage tem 3 tiers: hot, cold, archive:

hot - ssd
cold - hd
archive - fita

Hot e Cold acessa o dado diretamente, Archive já não dá pra acessar diretamente.

Isso é utilizado para regra de governança de dados.

```

# Metadados
```
É um termo generico, basicamente são informações sobre informações, que podem ser utilizadas.

Formato Parquet - Dados colunares, performatico e otimiza a consulta dos arquivos.

Ao ler a informação será lido somente os bytes necessários e ao fazer o download será limitado ao que é necessário.

## Estrutura Parquet
pip install parquet-tools

Dentro de um unico arquivo Parquet posso ter grupos de informações.

Parquet sempre guarda metadado de seus dados, vai ter por exemplo, o valor maximo e minimo da coluna.

```
# Delta e Hudi
```
É um framekwork de projeto para fazer um LakeHouse

delta.io

Questão de dado e metadado passa a se tornar muito proximo... É criado um JSON ou Parquet de metadado falando paths, estatisticas etc.

Isso otimiza consulta e trás informações sobre os dados.

Caso seja necessário apagar uma informação de um arquivo, será ajustado a nivel do parquet especifico que contém a informação.

Assim a tabela fica o tempo todo disponivel, e por conta de haver histórico, é possivel resgatar informações do passado.

Data Skipping --> A nivel de dado colunar isso fica mais facil
```

## Pontos interessantes
```
Amundsen é opensource

Elastic Search --> Exemplo google, amazon, em que começa a tentar prever o que será digitado


```


