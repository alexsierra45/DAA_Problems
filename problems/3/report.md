# Problema

Cuba tiene inicialmente $N$ ciudades aisladas, donde la $i$-ésima ciudad tiene una significancia de $A_i$. Alex, el Presidente de Cuba quiere conectar todas las ciudades. Él puede construir una carretera bidireccional de longitud $L$ $(L > 0)$ desde la ciudad $X$ a la ciudad $Y$ si $(A_X$ & $A_Y$ & $L) = L$, donde & representa el operador AND bit a bit.

¿Cuál es la longitud total mínima de las carreteras que tiene que construir para conectar todas las ciudades en Cuba? Imprime $-1$ si es imposible.

Nota:

Se dice que la ciudad $X$ y la ciudad $Y$ están conectadas si existe una secuencia de ciudades $C_1, C_2, \dots, C_K$ $(K \geq 1)$ tal que $C_1 = X$, $C_K = Y$, y existe una carretera desde $C_i$ a $C_{i+1}$ $(1 \leq i < K)$. Todas las ciudades en Cuba se dicen conectadas cuando cada par de ciudades en Cuba está conectado.

## Abstracción del problema

Sea G = (V, E) un multigrafo no dirigido tal que para cada ciudad del problema inicial tenemos un nodo en V, con un valor $A_i$ asociado al $i$-ésimo nodo. Entre los nodos $i$ y $j$ existe una arista de peso $(L > 0)$ si $(A_X$ & $A_Y$ & $L) = L$. Hallar el Árbol Abarcador de Costo Mínimo, a partir de ahora MST (Minimum Spanning Tree), de G.

## Observaciones

- La ecuación $A$ & $x$ = $x$, con $x > 0$ se satisface cuando $x$ es la representación de cualquier combinación de bits activos en $A$, a excepción de la combinación vacía. Escrito mas formalmente, sea $f(A, i) = 1$ si el $i$-ésimo bit de $A$ esta activo, 0 en otro caso, entonces las soluciones de $A$ & $x$ = $x$, con $x > 0$ pertenecen al conjunto $\{x | x = \sum f(A, i) \cdot g(i) \cdot 2 ^i, g(i) \in \{0, 1\} \land \sum g(i) \geq 1\}$.
- Podemos considerar a G como un grafo simple y no un multigrafo ya que como el objetivo es hallar el MST de G, lo optimo siempre sera, si se va a tomar una arista de $i$ a $j$, tomar la de menos peso que sera exactamente la relativa al bit activo menos significativo de $A_i$ & $ A_j$, arista que evidentemente pertenece al conjunto mencionado previamente.
- En el árbol resultante de hallar el MST a G, para toda secuencia de nodos que forman un camino, se cumple que para cualquier par consecutivo de ellos tienen al menos un bit activo en común. Para una lista A definamos $OR(A)$ como el resultado de aplicar la operación OR bit a bit de los elementos de $A$, es decir $f(OR(A), i) = 1$ si y solo si alguno de los elementos de $A$ tiene el $i$-ésimo bit activo. De la definición y el resultado anterior se desprende que si existe una partición $A, B$ de los nodos de G, tal que $OR(A)$ & $OR(B)$ = 0, entonces no existiría ninguna arista entre los nodos de $A$ y $B$, por lo que no existiría el MST de G.

## Solución naive

Armar un grafo G con un nodo por cada ciudad, cada nodo $i$ con un valor asociado $A_s$. Luego pasar por cada par de nodos y construir una arista de peso igual al bit activo menos significativo entre ellos. Luego usar algún algoritmo clásico como Kruskal o Prim para hallar el MST del grafo. Para G se tiene que $|V| = O(n)$ y $|E| = O(n^2)$, de donde la complejidad de esta solución es $O(n^2 \log n)$.

## Teoría de arista liviana que cruza el corte

### Definiciones

- Un corte $(S, V-S)$ de $G=(V,E)$ no dirigido es una partición de los vértices del conjunto V.
- Una arista $<u,v>$ cruza el corte $(S, V-S)$ si uno de los extremos de la misma está en $S$ y el otro en $V-S$.
- Un corte, respeta un conjunto de aristas $A$, si no existen aristas en $A$ que crucen el corte .
- Una arista es liviana cruzando el corte, si tiene el menor peso entre todas las que lo cruzan .

### Teorema

- Sea $G=(V,E)$ un grafo conexo, no dirigido y ponderado.
- Sea $A \sube E$ incluido en algún MST de G.
- Sea $(S, V-S)$ un corte de G que respeta A.
- Sea $<u,v> \in E$ una arista liviana que cruza el corte $(S, V-S)$.

Entonces, $<u,v>$ es segura para $A$. Esto significa que $A \cup \{<u, v>\} \sube T$, donde $T$ es un MST de G.

## Solución

### Algoritmo

Nuestro algoritmo recibe como entrada una lista $L$ de los valores asociados a cada una de las $n$ ciudades. Sea $m = max(L)$. Primeramente nuestro algoritmo instancia una variable $ans = 0$, luego por cada $0 \leq i \leq m - 1$ realizara la siguiente secuencia de pasos:

1) Instancia dos listas vacias $A$ y $B$.
2) Por cada elemento $v \in L$, si $f(v, i) = 1$, $A = A \cup \{v\}$, en otro caso $B = B \cup \{v\}$.
3) Si $A \ne \empty$, hacemos $ans += (|A| - 1) \cdot 2^i$ y $B = B \cup \{OR(A)\}$.
4) Actualizamos la lista de nuevos valores y hacemos $L = B$.

Finalmente, si $|L| = 1$ devolvemos $ans$, en otro caso -1.

### Explicación

El algoritmo en la $i$-ésima iteración selecciona todos los nodos cuyo valor tengan activo el $i$-ésimo bit y los agrega a la lista $A$, al resto los agrega a $B$. Luego usa exactamente $|A| - 1$ aristas de peso $2^i$ para conectar los nodos de $A$ con un camino que pase por todos. Una vez conectados, se considera que desde la nueva componente conexa puede salir una arista de peso $2^j$ si el $j$-ésimo bit esta activo para alguno de los valores de $A$, por tanto podríamos tomar un nuevo nodo con valor $OR(A)$ y agregarlo a la lista $B$ de nodos que no participaron en esta iteración, luego actualizamos $L$ con la nueva lista de valores para la proxima iteración. Veamos que no se arma el grafo explícitamente, sin embargo iterativamente se van sumando a la respuesta los pesos de las aristas que van siendo añadidas. Nótese que al inicio de cada iteración la lista $L$ solo contiene los valores de nodos que no están conectados entre ellos, por lo tanto añadir una arista nunca generara un ciclo.

La idea principal detrás de esta implementación es que, si entre un par de nodos existe un camino que solo use aristas de peso a lo sumo $2^i$, después de la $i$-ésima iteración dichos nodos van a quedar conectados. Probemos esto por inducción:

- **Caso Base**: Para $k = 0$. Luego de la primera iteración, todos los nodos con el primer bit activo, si hay alguno, quedan conectados por la forma en la que funciona el algoritmo.

- **Hipótesis**: Para $k = i$. Sean $x, y$ nodos entre los cuales existe al menos un camino con aristas de peso a lo sumo $2^i$, entonces luego de la $i$-ésima iteración, $x, y$ quedan conectados.

- **Tesis**: Para $k = i + 1$. Sean $x, y$ nodos entre los cuales existe al menos un camino con aristas de peso a lo sumo $2^{i + 1}$. Si todas las aristas tienen peso menor que $2^{i + 1}$, dichos nodos están conectados desde la iteración pasada del algoritmo por hipótesis de inducción. Supongamos entonces que hay exactamente una arista de peso $2^{i + 1}$ (el caso en el que hay mas de una es análogo), y sean $u, v$ los nodos adyacentes a dicha arista, sin perdida de generalidad digamos que en el recorrido de $x$ a $y$ se visita primero a $u$. Entonces $x$ esta conectado con $u$ y $L$ esta conectado con $y$ desde la iteración anterior por hipótesis de inducción debido a que todas las aristas en esos caminos son de peso a lo sumo $2^i$. Por tanto en la iteración $(i+1)$-ésimo quedan conectados $x, y$ luego de añadir al grafo la arista $<u, v>$, terminando con la demostración.

Si luego de concluir el algoritmo, la lista de valores $L$ quedo con mas de un elemento, hay al menos dos nodos que no pudieron ser conectados con caminos que usan aristas de a lo sumo el peso máximo de alguna arista del grafo. En otras palabras, no existía camino inicialmente entre ellos, por lo que la construcción de un MST sobre G es imposible, por tanto devuelve -1.

### Correctitud

Probemos ahora que el valor devuelto por el algoritmo corresponde con un MST de G:

- Como se vio anteriormente, las aristas se construyen entre nodos que estaban previamente desconectados, por tanto nunca se genera un ciclo. Ademas como la lista $L$ quedo con exactamente un elemento, y por cada elemento que se eliminaba se añadía exactamente una arista, el grafo resultante es acíclico y tiene $n -1$, de donde es un árbol abarcador.

- Supongamos que dicho árbol abarcador no es de costo mínimo. Eso implica que existe una arista $e$ de peso $2^p$ con $p > 0$ que no es segura en el corte $(A, V - A)$ que define, y por tanto, no es liviana. De donde existe una arista $<u, v>$ de peso $2^q$ con $u \in A \land v \in V - A$, que no esta siendo tomada en el árbol. Sin embargo en el momento en que se toma la arista $e$, y debido a que $q < p$, los nodos $u, v$ no pueden estar desconectados y por tanto no pueden estar en lados diferentes de un corte. Contradicción con lo asumido, el valor obtenido corresponde con el costo del MST de G.

### Complejidad Temporal

Por cada bit en la representación binaria de $m$ se recorre una lista que tendrá a lo sumo $n$ elementos. Complejidad $O(n \log m)$.
