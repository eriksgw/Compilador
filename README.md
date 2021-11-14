### Alunos
- Bruno Duarte Barreto Borges (18100519)
- Erik Kazuo Sugawara (18100528)
- Fábio Oliveira de Abreu (18100529)

### Requisitos 
- python3

### Instalação
A instalação pode ser feita a partir do Makefile executando o comando `make install`
com isso serão instaladas as seguintes dependencias
- pip3 (Se já não estiver instalado) é o gerenciador de pacotes padrão do python3 (Requer privilégio de super usuário)
- ply será instalado a partir do pip3

### Execução
Após instalação o programa pode ser executado da seguinte forma `make run file='tmp/program_1.lcc'` em que `program_1.lcc`é um exemplo de arquivo `lcc` dentro da pasta `tmp` que pode ser passado ao parser como entrada

### Remoção
Para remover as dependências de instalação podemos executar o comando `make clean`