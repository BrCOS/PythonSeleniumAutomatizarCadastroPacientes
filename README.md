#  PythonSeleniumAutomatizarCadastroPacientes

Surgiu a necessidade de cadastrar 13 mil pessoas que estavam em uma tabela do Excel, em um site para um consultório médico.

Para isso foi utilizado o Python juntamente com Selenium para automatizar esse cadastro que estava, até então, sendo feito de forma manual por uma pessoa.

O cadastro consistia no nome, telefone com ddd, e-mail e data de nascimento.

Esses dados foram tratados utilizando o Pandas, tudo foi padronizado e os campos obigatórios foram tratados na cópia da tabela criada durante no tratamento, valores nulos foram dropados.

Em um dia, a pessoa conseguia cadastrar cerca de 50 pessoas manualmente e com o script funcionando corretamente, foi possível cadastrar todas as pessoas em 4 dias inteiros, lembrando que existem delays propositais para que o script acabe não quebrando durante sua execução. O Script estava executando algo entre de 1 pessoa a cada 30 segundos ou a cada 1 mintuo, durante 24 horas por 4 dias seguidos.

Todos as informações variam, pois em certos horários o site funcionava mais rapidamente do que outros, então os delays eram variandos entre 6 de 5 segundos cada ou 6 de 10 segundos cada.
