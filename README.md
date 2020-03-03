## Duan Rafael Ribeiro - Questionário

1. Qual(is). distribuição(ões) de linux você utiliza e/ou tem experiência?
   * Ubuntu 18.04 LTS
2. Em ambientes de produção, é recomendado que os usuários não executem
comandos utilizando o usuário root. Explique o por que desta recomendação.
   * O “root” é um usuário que tem total controle de todo o Linux e é o administrador do sistema. Ou seja, isso torna root perigoso e somente usuários avançados que entendem as implicações devem usá-lo. Pelo risco envolvido, o melhor a fazer é desativar a conta de root.
3. Qual o propósito do serviço ssh?
    * SSH ou Cápsula de Segurança é um protocolo de administração remota que permite aos usuários controlar e modificar seus servidores pela Internet. 
4. Já utilizou algum sistema de controle de versão (git, svn, cvs, TVFC, etc..)?
    * Git e Bitbucket
5. Quais linhas de comando você utilizaria para os seguintes procedimentos:
    * Obter o ip do endereço www.gocache.com.br.
        * ``ping www.gocache.com.br``
    * Verificar se o texto “gocache” aparece em um arquivo de texto chamado log.txt
        * ``grep -R gocache log.txt``
6. Quais são as diferenças entre os protocolos de rede TCP e UDP?
    * Em termos práticos, o protocolo TCP é mais robusto e mais pesado. Deve ser usado em situações que você quer garantir a integridade ou a ordem absoluta da informação transmitida, como por exemplo, ao fazer o download de um arquivo.
    * Já o UDP é mais leve, porém essa leveza vem do fato que ele tolera perdas de pacotes. Deve ser usado em situações onde isso não seja um grande problema, como jogos online, streaming de vídeo e de voz.
7. Explique como verificar se o servidor web no ip 10.0.0.1 está ligado e funcionando?
    * ``ping 10.0.0.1``
8. Usando o banco de dados Redis:
     * Qual comandos/instruções você usaria para inserir os seguintes valores em
    uma lista chamada “numeros”:
    2,7,1,8,2,8,1,8,2,8,4,6
    * Qual comando/instrução você usaria para exibir somente os 4 primeiros
    elementos 


# Teste prático
Crie um programa (pode ser em texto descritivo ou em qualquer linguagem de
programação) que:
1. Conecte em um servidor na porta tcp 8000 do ip 127.0.0.1.
2. Após a conexão, este programa deverá enviar o texto “OK” (sem aspas) para o
servidor.
3. Após o envio do texto “OK”, o programa deverá apenas receber os dados enviados
pelo servidor e imprimir na tela os dados recebidos.
4. Se o programa receber o byte zero (0x00), o programa deverá desconectar do
servidor e se finalizar.


# Resposta
The project structure is based on the official [Scaling your project](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-apis-with-reusable-namespaces) doc with some adaptations (e.g `v1` folder to agroup versioned resources).
1. Run the server-side Flask app in one terminal window:

    ```sh
    $ python3.7 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ python3 wsgi.py
    ```

    Navigate to [http://127.0.0.1:8000/api/v1/main](http://127.0.0.1:8000/api/v1/main)
    
    If you like to send any data to server, just add the query parameter "?data=yourdata":
    *  ``http://127.0.0.1:8000/api/v1/main?data=exampletest``
     
    
2. The API is self documented using Swagger.

    Navigate to [http://127.0.0.1:8000/api/v1/docs](http://127.0.0.1:8000/api/v1/docs)

