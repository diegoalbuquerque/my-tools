# my-tools
A collection of tools that I wrote for my help or study.

## About PTH files and Compromised LiteLLM related

### Pt-BR
Estas tools eu desenvolvi para aprendizado, ou seja, deve ter formas muito melhores de fazer o mesmo e nem tão pouco são voltadas a serem ferramentas de varredura completa do ataque em busca de persistências já bem mapeadas e conhecidas. 

**litellm-scan.sh**
Procurar pela existência ou não da biblioteca litellm, assim como as bibliotecas que dela dependam, é uma ação óbvia que serve para detectarmos facilmente um possível comprometimento e através de qual biblioteca.

Para isso, o script `litellm-scan.sh` faz esse papel. Ele verifica se a biblioteca `litellm` está instalada e qual sua versão para verificar o comprometimento direto. Adicionalmente verifica para todas as bibliotecas instaladas se elas dependem da litellm. 

Bem, mas porque verificar outras bibliotecas se a `litellm` já não estaria instalada, o que já descartaria o comprometimento? Pois a remoção da `litellm` não implica na remoção da biblioteca que dependa dela e em uma atualização, ela pode vir a ser novamente instalada. 

Ou ainda o desenvolvedor por algum motivo, como testes, pode instalar um pacote com `--no-deps` o que não instalaria a litellm de imediato mas deixaria o sistema apto a instalar em um próximo update.

Para testar:

```
$ python3 -m venv /tmp/test-env
$ source /tmp/test-env/bin/activate
$ pip install --no-deps litellm-cost-tracker
$ ./litellm-scan.sh
```

**pth-scan.py**
Mas mesmo com a remoção da biblioteca litellm, outra que dependa dela, ou mesmo a atualização de todo o sistema, arquivos .pth comprometidos podem ter sido deixados no sistema, então entra em cena o `pth-scan.py` , para verificar a existência de arquivos `.pth` que possuam execução de código. 
