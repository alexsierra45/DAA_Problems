# Problema

Javier está pasando un curso de Diseño y Análisis de Algoritmos. Este año, por primera vez en la historia, los profesores han decidido evaluar el curso mediante un examen final y Javier se ha dado cuenta de que, a grandes rasgos, está frito. A pesar de ser un poco barco, es de hecho un muchacho inteligente y rápidamente se da cuenta de que su única forma de aprobar era hacer trampa. El día de la prueba, Javier se sentó en el asiento que estaba entre Hansel y Elena para fijarse, con la esperanza de que, uniendo las preguntas respondidas por cada uno, se pudiera formar un examen correcto.

El examen tiene $n$ preguntas, ordenadas en la hoja. Elena y Hansel pueden no ser capaces de responder cada uno el examen entero, pero todas las preguntas que responden están correctas. Se conoce cuáles preguntas respondió cada uno y se reciben como dos listas ordenadas de enteros entre $1$ y $n$. Javier tiene $p$ oportunidades para mirar hacia la izquierda (hoja de Hansel) o hacia la derecha (hoja de Elena) y su agilidad mental le alcanza para ver las respuestas de $k$ preguntas consecutivas (en cualquier posición) cada vez que echa una mirada a un examen.

Ayude a Javier a saber la cantidad máxima de preguntas que puede responder con su (tramposa) estrategia.


# Abstraccion


Sean tambien las funciones $a_i$ y $b_i$ con $i\isin [1,n]$ tal que:
$
a_i =
\begin{cases}
1 & \text{si Elena tiene la respuesta de la pregunta i} \\
0 & \text{si no la tiene}\\
\end{cases}
$

$
b_i =
\begin{cases}
1 & \text{si Hansel tiene la respuesta de la pregunta i} \\
0 & \text{si no la tiene}\\
\end{cases}
$

Dedominemos una observacion $q_{iP}\isin 2^\N$ al conjunto de los indices de las preguntas respondidas por la persona P desde la posicion $i$ hasta la posicion $i+k-1$. Diremos que una observacion es hacia A si es hacia Elena y es hacia B si es hacia Hansel.


Sea S un conjunto de observaciones, entonces llamaremos costo de S a la funcion $c(S)=|\bigcup S|$ 

El problema consiste en encontrar $max$ $c(S)$ $s.a.$ $|S|=p$


# Solucion Naive.

Existen $2n$ posibles observaciones y queremos exactamente $p$ de estas. Por lo que el total de casos validos seria $
\begin{pmatrix}
2n \\
p
\end{pmatrix}
$. Por cada combinacion, por cada oportunidad tengo que contar $k$ problemas en el futuro. Por lo que la complejidad final seria $
\begin{pmatrix}
2n \\
p
\end{pmatrix}
pk$.

## Correctitud

Estamos explorando todas las posibilidades. Sea $S$ la respuesta correcta, esta tiene que tener una combinacion de observaciones.

# Enfoque 2: Programacion dinamica

### Lema 1

Si existe una solucion óptima $S$ con $c(S)\neq0$, entonces existe una solucion optima S' tal que 
$\forall i:q_{iA}\isin S'$ => $a_i=1$ $\wedge$ $q_{iB}\isin S'$ => $b_i=1$.

**Demostracion:**

Sea $S$ una solucion optima tal que $c(S)\neq0$ que no cumpla $\forall i:q_{iA}\isin S$ => $a_i=1$ $\wedge$ $q_{iB}\isin S$ => $b_i=1$. Asumamos sin perdida de generalidad que: 
$q_{iA}\isin S$ $\wedge$ $a_i=0$ .

Si $q_{iA}=\{\}$, entonces $|\bigcup S|=|\bigcup S/q_{iA}|$

Como $c(S)\neq0$, $\exist j:a_j=1$ $\vee$ $b_j=1$. Sin perdida de generalidad asumamos que $b_j=1$. Luego,
$$|\bigcup S/q_{iA}|\leq|\bigcup S/q_{iA}\cup q_{jB}|=|\bigcup S'|$$

Luego, $c(S)\leq c(S')$, pero como $S$ es optimo: $c(S)= c(S')$

Si $q_{iA}\neq\{\}$, entonces $\exist x_1, x_2...x_r$ con $r<k,$ $x_r<k$, $\forall j,h:j<h$ => $x_j<x_h$ tal que:

$q_{iA}=\{i+x_1,i+x_2,...,i+x_r\}$

Sean $j=i+x_1$ y $y_h=x_{h+1}-x_1$. Sustituyendo

$q_{iA}= \{j,j+y_1,...,j+y_{r-1}\}$

=> $q_{iA}\subseteq q_{jA}$

=> $c(S)\leq c(S')$

Con $S'=S/q_{iA}$  $\cup$ $\{q_{jA}\}$

Pero como $S$ es optimo: $c(S)= c(S')$

Usando este razonamiento y aplicando induccion queda demostrado.

### Lema 2

Si una solucion optima $S$ contiene las observaciones $q_{iA}$ y $q_{iB}$, existe otra solucion optima que o no contiene a $q_{iA}$ o no contiene a $q_{iB}$.

**Demostracion:**

Usando el lema 1, partamos de una solucion donde todas las observaciones comiencen con una pregunta respondida. Luego, $b_i=a_i=1$

Llamemos:
$
X_i =
\begin{cases}
\{i\} & \text{si } b_i=1\\
\{\} & \text{si no la tiene}\\
\end{cases}
$

Luego:
$$c(S)=|\bigcup S|=|(\bigcup (S/q_{iB}))\cup q_{iB}|$$

$$=|(\bigcup (S/q_{iB}))\cup (\bigcup_{j=i}^{i+k-1} X_j)|$$

$$=|(\bigcup (S/q_{iB}))\cup X_i \cup (\bigcup_{j=i+1}^{i+k-1} X_j)|$$

$$\leq |(\bigcup (S/q_{iB}))\cup X_i \cup (\bigcup_{j=i+1}^{i+k} X_j)|$$

$$= |(\bigcup (S/q_{iB}))\cup X_i \cup q_{(i+1)B}|$$

$$= |(\bigcup (S'))\cup X_i|$$

Donde $S'=(S/q_{iB}) \cup q_{(i+1)B}$

Como $a_i=1$ y $q_{iA} \subseteq S'$ entonces $i \isin S'$, por lo que:

$$|(\bigcup (S'))\cup X_i|=|(\bigcup (S'))|$$

Luego:$$c(S)\leq c(S')$$

Pero $S$ es optimo, por lo que: $$c(S)= c(S')$$

Y optenemos una solucion optima diferente.

## Idea de la solucion

Por el lema 1 y lema 2, descartamos soluciones que partan de indices iguales o partan de indices que no posean solucion. Luego, dado una posicion $i$ hay 3 posibles acciones que pueden tomarse:
1- Ignorar la posicion
2- Tomar el intervalo que empieza en ella en A (tomar $q_{iA}$)
3- Tomar el intervalo que empieza en ella en B (tomar $q_{iA}$)

Solo hay 3 factores que pueden afectar la toma de esta decision:
1- La cantidad de intervalos vistos
2- Si el indice pertenece a un intervalo de A tomado con anterioridad
3- Si el indice pertenece a un intervalo de B tomado con anterioridad

La primera no afecta si no se ha tomado ningun intervalo, la segunda y la tercera no afecta al primer indice, pues el unico intervalo que incluye al primer indice es al que empieza en este.

Luego, la solucion del problema puede verse como

$$
S = max
\begin{cases} \text{Mejor solucion dado que tomaste }q_{1A} \\
\text{Mejor solucion dado que tomaste }q_{1B}\\
\text{Mejor solucion no tomando 1}
\end{cases}
$$

Luego, esto se puede ver de forma recursiva tomando cada indice teniendo en cuenta la cantidad de oportunidades restantes (entre 0 y p), cual es la distancia a el ultimo intervalo que empieza en A y B respectivamente (entre 1 y k).

Por lo que cada caso se puede ver como la tupla $(i,A,B,p)$ donde $i$ es la posicion del array, $A$ y $B$ son el maximo entre 0 y $k-d$ donde $d$ es la diferencia entre los indices $i$ y el indice del primer valor del ultimo intervalo tomado de A y B respectivamente y p la cantidad de oportunidades que quedan por tomar.


## Complejidad temporal

Por cada tupla realizo O(1) operaciones, y tengo una tupla por cada problema, por cada tamaño de ventana de A y de B, y para cualquier numero de oportunidades.

