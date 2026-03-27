# my-tools
A collection of tools that I wrote for my help or study.

## PTH files and Compromised LiteLLM related

### Pt-BR
Estas tools eu desenvolvi para aprendizado, ou seja, deve ter formas muito melhores de fazer o mesmo e nem tão pouco são voltadas a serem ferramentas de varredura completa do ataque em busca de persistências já bem mapeadas e conhecidas. 

#### >> **litellm-scan.sh**

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

#### >> **pth-scan.py**
Mas mesmo com a remoção da biblioteca litellm, outra que dependa dela, ou mesmo a atualização de todo o sistema, arquivos .pth comprometidos podem ter sido deixados no sistema, então entra em cena o `pth-scan.py` , para verificar a existência de arquivos `.pth` que possuam execução de código. 

### EN
I developed these tools for learning purposes. This means there are likely much better ways to achieve the same results, and they are not intended to be comprehensive scanning tools for detecting well-known, pre-mapped persistence mechanisms.

#### >> **litellm-scan.sh**
Checking for the presence of the litellm library, as well as libraries that depend on it, is an obvious step to easily detect a possible compromise and identify which specific library is involved.

The litellm-scan.sh script handles this role. It verifies if the litellm library is installed and checks its version to identify direct compromise. Additionally, it scans all installed libraries to see if any of them list litellm as a dependency.

Now, why check other libraries if litellm isn't installed? Wouldn't that already rule out the compromise? Not necessarily. Removing litellm does not automatically remove the libraries that depend on it. Furthermore, a developer might install a package using --no-deps for testing; while this wouldn't install litellm immediately, it leaves the system ready to pull it in during a future update.

To test:
```
$ python3 -m venv /tmp/test-env
$ source /tmp/test-env/bin/activate
$ pip install --no-deps litellm-cost-tracker
$ ./litellm-scan.sh
```

#### >> **pth-scan.py**
Even after removing the litellm library, its dependencies, or updating the entire system, compromised .pth files might still remain on the system. This is where pth-scan.py comes in: it scans for the existence of .pth files that contain executable code.


