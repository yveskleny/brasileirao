adiciona informações na branch local da liga inglesa sem alterar as demais
O repositório online principal (branch main/master) ou qualquer outro nome dado permanece inalterado
Boa prática
O repositório local branch main/master não precisa nem deve ser alterado diretamente.


Antes: Faça um pull no terminal chamando a branch online com o seguinte comando:
    <git pull>

Em seguida crie uma branch local separada da main, alterne para essa branch para fazer suas alterações por ela e não pela main com o comando:
    <git branch "nome_da_sua_branch_local">

Depois faça o comando:
    <git switch nome_da_sua_branch_local>

Agora sim, vc pode alterar a vontade o que precisar.

E como atualizar o que fiz sem perder nada do que os outros já fizeram? 

O comando pull quando executado toda vez antes de voce iniciar seus trabalhos ja previnem isso,
mas se ainda tiver dúvida, execute o comando de pull na sua main, depois troque p/ a branch local e em seguida faça o merge com o comando:
    <git merge main> ATENÇÃO: nesse caso você está trazendo da main todos os commits para a branch que voce está no momento

**Finalizando o trabalho e enviando para o repositório online do github**

Adicione as alterações pelos comandos add e commit -- detalhados em [commit](../estatisticas/liga_inglesa/commit.md)


realize o comando:
<git push origin nome_da_sua_branch_local> 
Assim voce lança no repositório online uma branch igual a sua local
Ao fazer isto, podemos juntar através de um PR (Pull Requests) as versões de cada colaborador na main online



OBS: para criar uma nova branch e já mudar para ela diretamente use o comando:
<git switch -c nome_da_branch>
Isso evita que a gente esqueça de alternar entre branches e fazer alterações inadivertidas na main por exemplo.