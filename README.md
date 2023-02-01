## Infra as a Code: Docker

_I Semana da DIATINF_

__Minicurso - Infra as a Code: Docker__

Aqui você aprenderá do zero a implementar uma Aplicação Web minimamente sofisticada, hospedada em Containers Docker! A ideia é que se use apenas um comando para subir toda a Infraestrutura Lógica das aplicações que o estão neste projeto. Vai ser TOP!

Além disso, você terá um norte teórico e prático de como implementar qualquer outra aplicação usando Containers Docker!

---

### Dependências

- Docker

- Docker Compose

- Python

---

### Docker

É o que vai fazer a mágica acontecer! Pode ser instalado em vários Sistemas Operacionais. Para saber mais sobre ele, basta acessar o [Site Oficial do Docker](https://www.docker.com/). Para Instalação, vá neste Link [Aqui!](https://docs.docker.com/engine/install/). Também é possível adquirir um gerenciamento gráfico do Docker, conhecido como Docker Desktop. Para instalar ele, vá neste outro link [Aqui!](https://docs.docker.com/desktop/).

---

### Docker Compose

O Docker Compose está sob p Docker, é quem vai fazer a parte mais legal de se ver no final das contas, porque ele pode juntar tudo e subir toda a Infraestrutura de uma vez só, todos os containers em poucas linhas de código, e já com a maioria, ou todas as configurações pré-estabelecidas. Instale [Aqui!](https://docs.docker.com/compose/install/).De cara, o Compose pode ser mais complexo, porém com o tempo, você não vai largar o pé dele, e mal vai querer saber o que é "docker run".

---

### Python

Uma das linguagens mais simples e flexiveis para todas as demandas tecnológicas da vida. Foi utilizada neste projeto pela maior possibilidade de ter em qualquer máquina (SO), porém caso não a tenha, basta instalar bem [Aqui!](https://www.python.org/downloads/). Neste Projeto, ele será usado para automatizar algumas demandas, como verificações e  configurações.

---

### Instruções

Então sem mais delongas, vamos pôr a mão na massa, digo nos códigos....

1. O primeiro passo, será efetuar a clonagem desse repositório para seu ambiente de trabalho local. Para isso, será necessário ter o cliente git instalado. Caso esteja utilizando o MS Windows, procure, no menu iniciar,  por **git bash**. No Linux, apenas abra um novo terminal. Vamos clonar nosso repositório:
   
   ```shell
   git clone https://github.com/pedroieremis/Semana-Diatinf-2022.2.git
   ```

2. Agora, vamos adentrar ao diretório do nosso repositório:
   
   ```shell
    cd Semana-Diatinf-2022.2/
   ```

3. Para subir a infra, usaremos o docker compose:
   
   ```shell
   docker compose up
   ```

4. Para parar a infra:
   
   ```shell
   docker compose down
   ```

5. Subindo tudo de uma forma automatizada:
   
   Linux:
   
   ```shell
   python3 auto-infra.py
   ```

   Windows:

```shell
python auto-infra.py
```

### Considerações Finais

- - Pra executar este projeto, é importante que todas as dependências estejam __atualizadas__ e que você tenha acesso as configurações da máquina hospedeira.

- Não é de extrema dependência, mas é de grande ajuda que se tenha o Git para este projeto. E pra vida também, seja utilizando o GitHub, GitLab ou outro como repositório, mas use. De cara, aconselho utilizar o GitHub para seu próprio marketing e o GitLab para algo mais profissional e restrito.

- Na instalação do Docker, é comum que se seguir a documentação, também se obtenha o Docker Compose, não havendo a neccessidade de instalar fora a parte. Para Windows, no Docker Desktop, também vem integrado o Compose.

- Ao final, quando se aborta a execução, o Python pode acusar erro, mas não será um problema, pois foi ele quem iniciou a Infraestrutura. Erro: "KeyboardInterrupt". Caso queira retirar isso, passe o arqumento ``-d`` no final do comando na linha 34 do programa em Python. Da seguinte forma: ``docker compose up -d``. No programa ficaria assim: ``os.system('docker compose up -d')``.

- Caso o Script de Automatização capture o IP ``127.0.0.1``, recomendo colocar manualmente o IP da máquina nos arquivos do DNS, de acordo com a rede em que a máquina se encontra, assim as outras máquinas da rede poderão te alcançar.


### Não deixe ficar só nesse minicurso...

Se gostou do conteúdo e deseja ampliar seus conhecimentos, temos algumas indicações para vocês continuarem a jornada de aprendizado( P.S. **TUDO NA FAIXA...**)

    

1. Livro: [Pro Git - Scott Chacon](https://git-scm.com/book/pt-br/v2)

2. Livro: [Descomplicando o Docker](https://livro.descomplicandodocker.com.br/chapters/chapter_00.html)

3. Treinamento: [Descomplicando o Docker - Linux Tips ](https://www.linuxtips.io/course/descomplicando-o-docker)
