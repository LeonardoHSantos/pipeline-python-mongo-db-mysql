# Objetivo do projeto: criar um pipeline utilizando Python + MongoDB + MySQL
<p>Trata-se de um pipeline simples, porém, aborda conceitos importantes de banco de dados NoSQL e processamentos de dados com a biblioteca Pandas do Python</p>

# #EXEMPLOS DE OPERADORES PARA UTILIZAR COM O MÉTODO FIND
<h3>Reforçanfo os conhecimentos sobre REGEX (fonte: curso de Pipeline Alura).</h3><br>
<p>$gt: encontra documentos onde o "Preço" é superior a 500.</p>
<pre>
query = {"Preço": {"$gt": 500}}
</pre>

<p>$lt: busca documentos onde a "Quantidade de parcelas" é menor</p>
<pre>
query = {"Quantidade de parcelas": {"$lt": 3}}
</pre>

<p>$lt: busca documentos onde a "Quantidade de parcelas" é menor que 3.</p>
<pre>
query = {"Quantidade de parcelas": {"$lt": 3}}
</pre>

<p>$lte: seleciona documentos em que o "Frete" seja menor ou igual a 50.</p>
<pre>
query = {"Frete": {"$lte": 50}}
</pre>

<p>$ne: localiza documentos em que o "Tipo de pagamento" não seja "cartao_credito".</p>
<pre>
query = {"Tipo de pagamento": {"$ne": "cartao_credito"}}
</pre>

<p>$in: filtra documentos nos quais a "Categoria do Produto" seja "esporte e lazer" ou "eletrônicos".</p>
<pre>
query = {"Categoria do Produto": {"$in": ["esporte e lazer", "eletronicos"]}}
</pre>

<p>$nin: busca documentos nos quais a "Categoria do Produto" não seja nem "esporte e lazer" nem "eletrônicos".</p>
<pre>
query = {"Categoria do Produto": {"$nin": ["esporte e lazer", "eletronicos"]}}
</pre>

<p>$regex: encontra todos os vendedores cujos nomes começam com "Ma".</p>
<pre>
query = {"Vendedor": {"$regex": "^Ma"}}
</pre>