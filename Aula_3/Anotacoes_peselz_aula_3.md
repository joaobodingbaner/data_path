# Aula 03 - Orquestração e Fluxo de Dados

## Fluxo de dados padrão:
Ingestão: O que fizemos com NiFi
Storage: Armazenar em algum lugar
Processamento: Transformação dos dados
Distribuição: Análise de Dados de mostrar os dados


Orquestração permeia tudo.

Automatizar um fluxo não significa que está orquestrado. Só que está rodando automatico, sem alguma inteligencia ou lógica

Orquestração significa que há uma garantia que o fluxo possui uma inteligencia, com alertas e data quality.

## Ferramentas
Há varias ferramentas que realizam orquestração, é utilizado bastante:
- Airflow
- KubeFlow


### Airflow
OpenSource, roda em cima de python e é amigável a nível de orquestração com plugins (conectores)

- Operators: deixa mais abstraido na hora de criar pipelines. Um dos mais famosos é do quinto andar que possui um esquema de código com DAG que faz a orquestração com outros processamentos e pipelines.

O maior desafio da orquestração é a questão de achar pessoas capacitadas e governança para manter o fluxo de dados confiável.

Garantir que os dados estejam confiáveis torna a parte de orquestração a mais complexa.

O Airflow é bem visual, pelo visual dá para ver se o fluxo rodou, qual horário irá rodar novamente, etc...

#### Arquitetura Aiflow
Funciona a nivel de DAG (Direct Acycle Graph), cada caixa é uma função python que realiza algo.

Cada DAG é um código que representa um fluxo lógico.

Não é possível codar direto pelo interface do airflow.


#### Comandos
```
docker-compose up airflow-init

docker-compose up
```



# Links importantes
```
https://livebook.manning.com/book/data-pipelines-with-apache-airflow/welcome/v-5/

https://airflow.apache.org/docs/apache-airflow/stable/

```
























