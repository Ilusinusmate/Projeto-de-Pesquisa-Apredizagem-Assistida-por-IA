# Análise de Impacto da Inteligência Artificial no Ensino de Python

## Descrição do Projeto
Este repositório contém os dados e materiais utilizados em uma pesquisa experimental para avaliar o impacto do uso da Inteligência Artificial (IA) no ensino de Python. O estudo foi conduzido ao longo de quatro meses com estudantes do Instituto Federal da Paraíba (IFPB) e da Escola Cidadã Integral Técnica (ECIT) Braulio Maia Júnior. Durante esse período, os alunos participaram de aulas semanais sobre programação em Python, abrangendo desde conceitos básicos de entrada e saída de dados até estruturas de dicionários.

## Metodologia
A pesquisa seguiu um modelo de teste A/B, no qual os alunos foram divididos em dois grupos:
- **Grupo IA**: teve acesso a ferramentas de Inteligência Artificial durante as aulas e atividades.
- **Grupo Sem IA**: não teve acesso a ferramentas de Inteligência Artificial durante o aprendizado.

Cada turma foi dividida ao meio e posicionada fisicamente de forma separada dentro da mesma sala de aula, garantindo que ambos os grupos recebessem as instruções ao mesmo tempo, sem influência mútua.

### Turmas e Distribuição
- **Turma 1** - IFPB (Dividida em Grupo IA e Grupo Sem IA)
- **Turma 2** - IFPB (Dividida em Grupo IA e Grupo Sem IA)
- **Turma 3** - ECIT Braulio Maia Júnior (Dividida em Grupo IA e Grupo Sem IA)

### Avaliação dos Participantes
Antes do início do experimento, os alunos foram submetidos a dois testes diagnósticos para medir seu conhecimento prévio em Python. Com base nos resultados, foram classificados nos seguintes níveis:
- **Básico**
- **Médio**
- **Avançado**

Os testes foram respectivamente:
- ***1º teste***: Receba um número inteiro que representa a idade de um indivíduo e imprima na tela se ele é maior ou menor de idade.

- ***2º teste***: Receba 6 inteiros separados por " " e imprima os indices dos inteiros maiores ou iguais à 18.

Esses dados foram utilizados para garantir uma estratificação equitativa entre os grupos, buscando minimizar a influência de conhecimento prévio na comparação dos resultados.

## Conteúdo Ministrado
O curso seguiu uma estrutura progressiva de ensino, cobrindo os topicos mediante o seguinte cronograma de aulas:

1. Entrada de dados e Saída de dados & Variáveis e Tipoes
2. Entrada de dados e Saída de dados & Variáveis e Tipos
3. Operadores e Estruturas Condicionais
4. Operadores e Estruturas Condicionais
5. Operadores e Estruturas Condicionais
6. Estruturas de Repetição (WHILE)
7. Estruturas de Repetição (FOR)
8. Estruturas de Repetição (Revisão)
9. 1º Avaliação Geral
10. Correção da Prova em sala e Revisão Geral
11. Listas (Arrays) & Métodos de Listas
12. Listas (Arrays) & Métodos de Listas
13. Manipulação de Strings & Métodos de Strings
14. Manipulação de Strings & Métodos de Strings
15. Dicionários
16. Revisão
17. 2º Avaliação Geral



## Coleta de Dados

### Formulários 
- **Feedback de Aula**: Após o final de cada aula, todos os alunos deveriam preencher um google forms com diversas perguntas, relacionada ao uso de IA, aprendizado, etc. 
- **Periodo em Casa**: Antes do início de cada aula, os alunos deveriam preencher um google forms com perguntas relacionas ao uso de IA no período que permaneceu em casa, seu estudo como autodidata, se procorou resolver as atividades, etc.

- **Feedback de Avaliação**: Após a realização de cada avaliação, todos os alunos deveriam responder um google forms à respeito da avaliação, se estudaram para esta, se acreditam que a IA auxiliaria, etc. 

### Atividades
- **Sala**: Atividades realizadas no The Huxley, passadas para os alunos em sala, conforme o conteúdo aprendido no período em questão. Os alunos com IA, poderiam utilizar IA para resolver as atividades, enquanto os alunos sem IA, não poderiam. As atividades tinham o período restrito, ou seja, só podiam ser realizadas durante à aula.

- **Casa**: Atividades realizadas no The Huxley, passadas para os alunos em casa, conforme o conteúdo aprendido no período em questão. Os alunos não tinham restrição do uso de IA. As atividades tinham o período de uma aula até outra, ou seja, cerca de 1 semana.


### Atividades Avaliativas

#### Avaliações

- **Avaliação 1**: Realizada após a 8ª aula, está disponível neste repositório.
- **Avaliação 2**: Realizada após a 15ª aula, está disponível neste repositório.

***Avaliações Práticas***: [Clique aqui](./Avaliações%20Práticas/)
***Avaliações Teóriocas***: [Clique aqui](./Avaliações%20teóricas/)

#### Correção das Avaliações
 - As avaliações práticas foram corrigidas com o sistema de subtarefas e casos de teste, cada questão foi dividida em cerca de 4 subtarefas, cada uma destas contento X testes, Cada subtarefa vale o valor correspondente ao valor da questão dividido pelo número de subtarefas. Cada teste passado rende Valor da Subtarefa / X, ou seja, caso um aluno acerte 25 testes de 100 testes em uma subtarefa, ele terá 1/4 do valor total desta subtarefa.

 - Os critérios e pontuações para cada subtarefa estão especificados [Segunda Prova - Aqui](./correcao_das_avaliacoes_praticas/critérios.md) e [Primeira Prova - Aqui](./correcao_das_avaliacoes_praticas/critérios2.md)

 - As primeiras avaliações práticas com menor número de casos de teste, foram corrijidas utilizando o CPH Judge, já a segunda foi corrigida utilizando um sistema prórpio de correção, escrito em Dart [Aqui](./correcao_das_avaliacoes_praticas/avaliacao_02/gabarito/tester.dart).

 - Os casos de teste foram elaborados seguindo cada critério, na pasta de "casos_de_teste", há uma pasta para cada questão correspondente, com os casos de teste para cada subtarefa, cada input foi gerado de forma à respeitdas os critérios definidos e cada output esperado foi gerado com as questões corrigidas.

 - As questões corrigidas podem ser acessadas em [Av01 Prática](./correcao_das_avaliacoes_praticas/avaliação%2001/questões%20corrigidas/) ou [Av02 Prática](./correcao_das_avaliacoes_praticas/avaliacao_02/questões%20corrigidas/)

 - Cada teste (input e output) é separado por uma sequência de "\n\n\n" dentro do arquivo de cada subtarefa, para facilitar a leitura e a correção.

 - Para auditoria dos dados, basta buscar a submissão do aluno em [Submissões Av2](./correcao_das_avaliacoes_praticas/submissões-av02/) ou [Submissões Av1](./correcao_das_avaliacoes_praticas/submissões-av01/), colar na pasta gabarito e rodar o programa de correção, ele irá gerar um resumo do resultado, assim como o que está presente na pasta de submissão de cada aluno, até mesmo dos que não enviaram nenhum arquivo.

 No Linux
 
 ```
    sudo apt-get install dart
    dart ./tester.dart
 ```

No Windows

 ```
    .\tester.exe
 ```

 - Para mais informações de como rodar o programa, utilize a flag "--help"
 


## Dados Disponíveis no Repositório
- **Resultados dos Testes Diagnósticos**: Classificação dos alunos antes do início das aulas.
- **Materiais Didáticos**: Slides, exercícios e atividades utilizadas durante o curso. Slides [Acesse](./Slides/)
- **Dados de Desempenho**: Evolução dos alunos ao longo das aulas e comparações entre os grupos IA e Sem IA.
- **Análises Estatísticas**: Resultados do impacto da IA no aprendizado dos alunos.

- **Certificados de Conclusão**: Cada aluno que concluiu o curso recebeu um certificado de conclusão com 30h, devidamente assinado por cada professor, e coordenadores do projeto.

## Contribuição
Caso queira contribuir com a análise dos dados ou sugerir melhorias na metodologia, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está sob a licença Creative Commons Legal Code. Veja o arquivo LICENSE para mais detalhes.

