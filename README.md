## Infra as a Code: Docker

_I Semana da DIATINF_

__Minicurso - Infra as a Code: Docker__

Aqui você aprenderá do zero a implementar uma Aplicação Web minimamente sofisticada, hospedada em Containers Docker! A ideia é que use-se apenas um comando para subir toda a Infraestrura Lógica das aplicações que o está neste projeto. Vai ser TOP!

Além disso, você terá um norte teórico e prático de como implementar qualquer outra aplicação em Containers Docker!

---

### Dependências

- Docker

- Docker Compose

- Python

---

### Docker

É o que vai fazer a mágica acontecer! O Docker em si, pode ser instalado em vários Sistemas Operacionais. Para saber mais sobre ele, basta acessar o [Site Oficial do Docker](https://www.docker.com/). Para Instalação, vá neste Link [Aqui!]((https://docs.docker.com/engine/install/)). Também é possível adquirir um gerenciamente gráfico do Docker, para instalar, vá neste outro link [Aqui!]((https://docs.docker.com/desktop/)).

Lembre-se de tentar sempre manter o Docker atualizado, assim ele estará executando da melhor forma possível e vai te ajudar.

---

### Docker Compose

O Docker Compose está dentro do Docker e é quem vai a parte mais legal de ver no final das contas, porque ele pode juntar tudo e subir toda a Infraestrutura de uma vez só, com a maioria ou todas as configurações já pré-estabelecidas. Instale [Aqui!]((https://docs.docker.com/compose/install/)).

Também procure manter o Docker Compose atualizado, isso com certeza te ajudará. De cara, pode ser mais complexo, porém com o tempo, você não vai largar o pé dele, e mal vai querer saber do "docker run".

---

### Python

Uma das linguagens mais simples e flexiveis para todas as demandas tecnológicas da vida. Foi utilizada neste projeto pela maior possibilidade de ter em qualquer máquina (SO), porém caso não a tenha, basta instalar bem [Aqui!](https://www.python.org/downloads/).

Mais uma vez, busque manter o Python atualizado também, ele te entregará muitas possibilidades. Neste Projeto, ele será usado para automatizar algumas demandas e verificações.

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

- Não é uma dependência estritamente, mas é algo de extrema ajuda, use o Git, seja utilizando o GitHub, GitLab ou outro como repositório, mas use. De cara, aconselho utilizar o GitHub para seu próprio marketing e o  GitLab para algo mais profissional e restrito. 

- Pra executar este projeto, é importante que todas as dependências estejam atualizadas, que você tenha acesso as configurações da máquina hospedeira.

- Todos os Links são dos sites oficiais, para de acordo com seu SO, efetuar os downloads e instalações. 

- Ao final, quando se manda parar, abortar a execução, o Python pode acusar erro, mas não será um problema, pois foi ele quem iniciou a Infraestrutura. Erro: "KeyboardInterrupt". Caso queira retirar isso, passe o arqumento ``-d`` no final do comando na linha 34 do programa Python. Da seguinte forma: ``docker compose up -d``. No programa ficaria assim: ``os.system('docker compose up -d')``.



### Não deixe ficar só nesse minicurso...

Se gostou do conteúdo e deseja ampliar seus conhecimentos, temos algumas indicações para vocês continuarem a jornada de aprendizado( P.S. **TUDO NA FAIXA...**)

    

1.  Livro: [Pro Git - Scott Chacon](https://git-scm.com/book/pt-br/v2)

2. Livro: [Descomplicando o Docker](https://livro.descomplicandodocker.com.br/chapters/chapter_00.html)

3. Treinamento: [Descomplicando o Docker - Linux Tips ](https://www.linuxtips.io/course/descomplicando-o-docker)
   
   
