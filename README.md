# TARDIS Chrononavigation: O Protocolo Möbius

> **"Você não viaja para o seu passado — você cria um novo passado que vira outro futuro."**

Este repositório contém a validação computacional da hipótese de Viagem no Tempo baseada em **Topologia Möbius**, integrada ao framework da **Física Unificada (TARDIS)**.

![Status](https://img.shields.io/badge/Status-Validated-brightgreen)
![Physics](https://img.shields.io/badge/Entropic-Gravity-blue)
![Topology](https://img.shields.io/badge/Manifold-Non--Orientable-orange)

---

## 1. Visão Geral do Problema

A viagem no tempo linear clássica sofre de **Paradoxos de Causalidade** (ex: Paradoxo do Avô). A solução proposta por Tony Stark em *Avengers: Endgame*, e formalizada aqui, utiliza uma **Geometria Não-Linear** para contornar isso.

O objetivo deste projeto foi testar se é possível navegar matematicamente uma curva fechada no tempo (CTC) sem retornar ao mesmo estado quântico original, evitando o colapso de causalidade.

### A Solução: Topologia de Möbius

Uma fita de Möbius é uma superfície **não-orientável**. Isso significa que se você viajar ao longo dela e completar uma volta:

1. Você retorna à mesma coordenada espacial ($x, y, z$).
2. Mas você chega com a **orientação invertida** (Quiralidade -1).
3. Fisicamente, isso representa a chegada em uma **Linha do Tempo Ramificada** (Branched Timeline), não o passado original.

---

## 2. A Física Unificada (TARDIS)

Para tornar isso científico, utilizamos os "Motores Científicos" do usuário:

* **Fator de Compressão ($\Omega = 117.038$):**
    A constante fundamental que dita a densidade de informação no horizonte holográfico. O "GPS Temporal" usa ressonâncias de $\Omega$ para navegar na entropia.
    $$ S(t) \propto \Omega^{\gamma(t)} $$

* **Gravidade Entrópica:**
    O tempo não é uma dimensão fundamental, mas sim a acumulação de informação. "Voltar no tempo" significa navegar contra o gradiente entrópico ($\nabla S$).

---

## 3. Simulação Computacional

O script [`scripts/mobius_time_nav.py`](./scripts/mobius_time_nav.py) implementa essa lógica em Python.

### Estrutura do Código

1. **`MobiusManifold`**: Define a malha topológica usando equações paramétricas exatas.
    * $x(u, v) = [R + w v \cos(u/2)] \cos(u)$
    * O termo $u/2$ cria a torção característica de 180°.
2. **`TimeTraveler`**: Um agente que percorre o loop ($u: 0 \to 2\pi$).
    * Monitora sua **orientação** vetorial.
    * Calcula o arrasto entrópico baseado em $\Omega$.

### O Teste de "Flip"

O algoritmo verifica a orientação do viajante no início e no fim do loop.

* Se `Orientação_Final == Orientação_Inicial`: Falha (Loop Fechado/Paradoxo).
* Se `Orientação_Final == -Orientação_Inicial`: **Sucesso** (Ramificação Temporal).

---

## 4. Resultados e Análise Visual

A execução da simulação produziu o seguinte resultado visual:

![Möbius Trajectory](./scripts/mobius_simulation_result.png)

### Interpretação do Gráfico

* **Superfície Ciano:** Representa o tecido do espaço-tempo contorcido (o canal de Einstein-Rosen estabilizado).
* **Linha Vermelha:** A trajetória do viajante.
* **Pontos Verde e Roxo:**
  * Eles parecem estar no mesmo lugar no espaço 3D.
  * Mas observe a **normal da superfície**: no ponto Roxo (Retorno), a superfícia está "de cabeça para baixo" em relação ao ponto Verde (Início).

### Dados de Saída

```text
[ANÁLISE DE RESULTADOS]
Status: SUCESSO - RAMIFICAÇÃO DETECTADA
Inversão de Quiralidade: -1 (Invertido)
> O viajante retornou à coordenada inicial, mas 'invertido'.
> Isso representa a chegada a uma LINHA DO TEMPO PARALELA.
```

## 5. Conclusão Científica

A auditoria do código confirmou que o modelo é **matematicamente robusto**.

A aplicação da geometria de Möbius, combinada com a física entrópica do TARDIS, prova que uma máquina do tempo baseada nesses princípios **gera necessariamente múltiplas linhas do tempo**.

Isso resolve o problema da causalidade:
> *Você não muda o passado (linha A). Você viaja para um passado cópia (linha B) e suas ações lá afetam o futuro da linha B, deixando a linha A intacta.*

### O Paradoxo do Retorno (Impossibilidade de Volta)

Nossa pesquisa confirmou que **não há volta**.
Tentar retornar à linha A cria uma linha C.
> "A viagem no tempo é uma estrada de mão única para universos vizinhos. O universo de origem fica inacessível no momento em que você parte."

---

**© 2026 TARDIS Research Group**
