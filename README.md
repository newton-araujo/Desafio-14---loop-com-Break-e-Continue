<h1>Desafio 14 - Loop com Braak e Continue</h1>

<p>
Este projeto em Python destina-se a fornecer uma compreensão prática do uso de estruturas de controle de fluxo, especificamente break e continue em loops. Através de exemplos interativos, você explorará como essas instruções afetam o comportamento dos loops, permitindo um controle mais granular sobre a execução do código. Ao compreender esses conceitos, você estará mais bem equipado para desenvolver lógica condicional eficiente em seus projetos Python.
</p>

<h2>Código Interativo:</h2>
<h3>1° Loop com o <b> ` Break `: </b></h3>
Terminal:

    for contador in range(1, 11):
    if contador == 5:
        break
    print(contador)
<ul>
<h3><li>Explicação:</li></h3>
<ul>
<li>O primeiro loop (for) itera de 1 a 10.</li>
<li>O bloco condicional (if) verifica se o contador é igual a 5.</li>
<li>Se a condição for verdadeira, o comando continue é acionado, fazendo com que o loop pule para a próxima iteração.</li>
<li>A saída esperada imprimirá os números de 1 a 4 e de 6 a 10.</li>
</ul>
</ul>

<h3>2° Loop com o <b> `continue` </b>:</h3>
Terminal:

    for contador in range(1, 11):
    if contador == 5:
        continue
    print(contador)

<ul>
<h3><li>Explicação:</li></h3>
<ul>
<li>O segundo loop (for) também itera de 1 a 10.</li>
<li>O bloco condicional (if) verifica se o contador é igual a 5.</li>
<li>Se a condição for verdadeira, o comando continue é acionado, fazendo com que o loop pule para a próxima iteração.</li>
<li>A saída esperada imprimirá os números de 1 a 4 e de 6 a 10.</li>
</ul>
</ul>