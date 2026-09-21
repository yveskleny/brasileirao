**Confirmando as alterações**
Após realizar os ajustes, inserções, edições ou quaisquer outras mudanças no seu projeto
adicione essas alterações com o comando
<git add .>     Para adicionar em lote (ou seja todos os arquivos de uma vez)
    ou
<git add "arquivo_especifico">      Caso não queria adicionar todos ao seu Stage

O add é um comando para deixar na "fila" das confirmações.

Ou seja antes de fazer um commit
<commit> é um comando de **confirmação** 

Ao realizar <git commit> estamos confirmando no nosso repositório git local que aceitamos/queremos as alterações feitas

    -m é a mensagem obrigatório que o git espera. Geralmente escrevemos uma ideia geral caso haja muitas mudanças, ou uma ideia específica. 
    Por exemplo:
    
<git commit -m "deleta_pastas"> ou ainda
<git commit -m "atualiza_funcoes_e_adiciona_novos_parametros">

Sempre com aspas duplas " "

Após isso seguimos com a operação de PUSH para levar as mudanças locais para o repositório online (no caso o GitHub)
conforme vimos em [Boas Práticas](../estatisticas/liga_inglesa/boas%20praticas.md)