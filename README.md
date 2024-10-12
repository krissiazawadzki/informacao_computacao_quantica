# Introdução à Teoria da Informação Quântica

Este repositório oferece recursos computacionais para a disciplina de Introdução à Teoria da Informação Quântica [SFI5903](https://uspdigital.usp.br/janus/componente/disciplinasOferecidasInicial.jsf?action=4&sgldis=SFI5903&ofe=3) oferecida no programa de pós graduação do Instituto de Física de São Carlos. O lançamento desse repositório acompanha o oferecimento da disciplina no segundo semestre de 2024.

Os exemplos de simulação (clássica e quântica) de sistemas quânticos são apresentados em notebooks desenvolvidas nas linguagens Python e Mathematica. Os códigos são baseados em pacotes especiais:

- [Numpy](https://numpy.org/): biblioteca de computação científica do Python. Conta com recursos para manipular vetores e matrizes de forma eficiente.
- [Matplotlib](https://matplotlib.org/): biblioteca de visualização do Python. Permite produzir gráficos e animações em 2D e 3D com alta qualidade.
- [Jupyter](https://jupyter.org/): ferramenta de desenvolvimento permitindo combinar texto e código com interface web. Tem suporte para Python, Julia, R e muitas outras linguagens.
- [QuTip](https://qutip.org/): biblioteca de informação quântica do Python. Orientada a objeto, oferece classes e métodos para simular sistemas quânticos fechados e abertos, dependente ou não do tempo, e calcular suas propriedades.
- [Melt](https://melt1.notion.site/): biblioteca de informação quântica do Mathematica desenvolvida pelo Prof. Gabriel G. T. Landi. Oferece diversas funcionalidades para tratar simbolicamente problemas com poucos ou muitos qubits ou até cadeias de spin. 

- [Qiskit](https://qiskit.org/): biblioteca para computação quântica em Python com interface para computadores quânticos da IBM. Permite executar um algoritmo quântico tanto localmente com emuladores do hardware NISQ da IBM como remotamente com alocação de recursos.

As versões mais estáveis desses pacotes e suas dependências são listadas abaixo:

| :gift: Pacote | :white_check_mark: Versão | :exclamation: Dependências | :information_source: Instalação recomendada | 
| --- | --- | --- | --- |
| NumPy | 2.0 | Python (3+) | pip ou conda |
| Matplotlib | 3.9 | Python | pip ou conda |
| Jupyter | 7.2.2 | instaladas automaticamente | pip |
| QuTip | 4.0 | Python, NumPy, Scipy, Matplotlib, Cython, GCC, headers| pip ou conda|
| Melt | 1.0 | Mathematica (14.0)| load |
| Qiskit | 1.0 | instaladas automaticamente| pip ou conda|



## Conteúdo do curso

### Aula 1
Teoria Quântica: Definições, Notação, Operador Densidade

[Operador_densidade](./Operador_densidade.ipynb)

### Aula 2
Postulados da Teoria Quântica, Medidas e Distinguibilidade de estados

[Evolucao_operador_densidade_sistema_fechado](./Evolucao_operador_densidade_sistema_fechado.ipynb)

[Distinguibilidade_medidas](./Distinguibilidade_medidas.ipynb)

## Aula 3 e 4 
Correlações quânticas, Emaranhamento e Teletransporte Quântico

[Estado_puro_de_sistema_bipartido_e_emaranhamento](./Estado_puro_de_sistema_bipartido_e_emaranhamento.ipynb)

[Teletransporte_quantico](./Teletransporte_quantico.ipynb)


## Aulas 5 
Medidas de emaranhamento, separabilidade e SVD

[Emaranhamento_e_separabilidade](./Emaranhamento_e_separabilidade.ipynb)


## Aulas 7 
Equações mestras - solução de Lindblad

[Equacao_mestra_de_Lindblad](./Equacao_mestra_de_Lindblad.ipynb)

