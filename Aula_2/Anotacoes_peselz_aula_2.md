# Docker

O Docker é uma ferramenta para se criar containers a partir de imagens.

Containers são virtualizações a nivel de sistema operacional. São isolados um dos outros e agrupam seus próprios softwares, bibliotecas e arquivos de configuração.

Util para empacotar uma aplicação e suas dependências dentro de um recipiente virtual (container) que pode ser executado dentro de qualquer servidor linux. Permite flexibilidade e portabilidade de um aplicativo.

Permite pegar uma maquina e conseguir quebrar a nivel de memória em possiveis pedaços que rodam na aplicação. Haverá a infraestrutura da maquina, o sistema operacional e o Docker que conversa direto com o sistema operacional.

Teoricamente para rodar NiFi você precisaria de diversas coisas a nivel de framework, mas com docker não é necessário, pois o container já traz as informações necessárias na imagem.

WSL2 = Simula Linux no Windows

Trabalha com abstrações para isolar.

# Nifi

NiFi é uma ferramenta de Ingestão, pegar dados de fontes externas e ingerir os dados e colocar em algum lugar.

Meme do Patrick

NiFi tem caixinhas que se chamam processors que realizam as funcionalidades.

A documentação do NiFi pode ser encontrada em: 
```
https://nifi.apache.org/docs.html
```

Na sessão que tenho:
```
Username: 2d569334-922a-462f-b5f8-e42504852bc6
Password: hlweifMGSwG2P41XYsPh5d6E9FhoGMzJ
```


# Spark
framework mais forte atualmente pra big data

no mercado há serviços de nuvem que oferecem spark já configurado e gerenciado


Cada vez mais os serviços estão indo mais em direção ao Spark

O que tem sido muito utilizado é o Databricks que oferece plataforma com serviço para rodar em nuvem que oferece o spark

Modelo lakehouse que existe hoje é muito vendido pelo Databricks

A otimização que fazem é muito boa, sem precisar muita configuração

Spark possui RDD e Lazy Evaluation


"Tunar" -- 
Shuffle partition faz com que dê pra ajustar o volume de troca de informação entre as partições







