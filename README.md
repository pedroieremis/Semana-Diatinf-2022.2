## Semana-Diatinf-2022.2

#### Minicurso da Semana DIATINF - Infra as a Code: Docker

Neste minicurso, aprenderemos a provisionar uma infraestrutura, utilizando Docker, a partir do zero.

Utilizaremos, para fins didáticos, uma stack LAMP(Linux, MySQL, Apache e PHP) para disponibilizarmos uma aplicação CMS (Wordpress) para os usuários.

Toda a infraestrutura seguirá a abordagem IaC (Infra as Code - Infraestrutura como Código, em bom português).

Para realizarmos nossas atividades, utilizaremos a solução de conteinerização Docker. Então sem mais delongas, vamos pôr a mão na massa, digo nos códigos....

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