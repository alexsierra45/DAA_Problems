# Problema

En tiempos antiguos, esos cuando los edificios se derrumbaban por mal tiempo y la conexión mágica era muy lenta, los héroes del reino se aventuraban en el legendario laberinto, un intrincado entramado de pasillos, cada uno custodiado por una bestia mágica. Los pasillos sólo podían caminarse en un sentido pues un viento muy fuerte no te dejaba regresar. Se decía que las criaturas del laberinto, uniendo sus fuerzas mágicas (garras y eso), habían creado ciclos dentro de este, atrapando a cualquiera que entrara a ellos en una especie de montaña rusa sin final en la que un monstruo se reía de ti cada vez que le pasabas por al lado, una locura.

El joven héroe Juan Carlos, se enfrentaba a una prueba única: desmantelar los ciclos eternos y liberar los pasillos del laberinto para que su gente pudiera cruzarlo sin caer en los bucles infinitos de burla y depravación.

Cada vez que el héroe asesinaba cruelmente (no importa porque somos los buenos) a la criatura que cuidaba una un camino, este se rompía y desaparecía. Juan Carlos era fuerte, pero no tanto, debía optimizar bien a cuántos monstruos enfrentarse. Ayude al héroe encontrando la mínima cantidad de monstruos que debe matar para eliminar todas las montañas rusas de burla y depravación.

## Abstracción

De nuestro problema se puede crear la siguiente representación:

Tenemos un grafo $G(V,E)$ dirigido en el cual debemos encontrar la cantidad mínima de aristas a eliminar tal que el grafo resultante sea acíclico. Esto es un conocido problema NP-completo conocido en la literatura como **Minimum Feedback Arc Set**.

Nuestro siguiente paso será demostrar que nuestro problema es NP-completo mediante una reducción polinómica desde el problema de **Minimum Vertex Cover (MVC)** visto en clases, que es NP-completo. Para hacerlo, transformaremos nuestro problema en un problema de decisión, y una instancia de MVC a una instancia de nuestro problema, de tal forma que resolverlo permita resolver MVC.

Primero, demostraremos que el problema pertenece a la clase NP:

Dado un grafo y una posible solución, es fácil verificar en tiempo polinomial si el conjunto de aristas dado al ser eliminado da como resultado un grafo acíclico. Solo es necesario hacer un recorrido DFS para verificar la no existencia de aristas de retroceso, lo cual indica que se está intentando regresar a un nodo ya visitado, de donde el grafo resultante tendría al menos un ciclo.

## Definición

1. **Minimum Vertex Cover (MVC)**: Dado un grafo no dirigido $G = (V, E)$ y un número $ k $, el problema consiste en determinar si existe un subconjunto $ C \subseteq V $ de tamaño a lo sumo $ k $, tal que al menos una de las dos terminales de cada arista en $ E $ esté en $ C $.

2. **Minimum Feedback Arc Set (MFAS)**: Dado un grafo dirigido $ G = (V, E) $ y un número $ k $, el problema es determinar si existe un subconjunto $ F \subseteq E $ de tamaño a lo sumo $ k $, tal que al eliminar las aristas en $ F $, el grafo resultante sea acíclico.

## Descripción de la Reducción

Dada una instancia de **Minimum Vertex Cover** con:

- Un grafo $ G = (V, E) $
- Un número $ k $,

nuestro objetivo es decidir si existe un conjunto de vértices de tamaño a lo sumo $ k $ que cubra todas las aristas del grafo.

Debemos construir un grafo $ G' = (V', E') $ que sea una instancia del problema de **Minimum Feedback Arc Set**. En este grafo, resolver el problema MFAS será equivalente a resolver la instancia original de MVC.

### Construcción del Grafo $ G' $ para MFAS

1. **Toma el grafo original**: Partimos del grafo $ G = (V, E) $ de la instancia de MVC.

2. **Transformación a un grafo para MFAS**:
   - Para cada nodo $ u \in V $, reemplaza el nodo con 2 nuevos nodos $ u_1, u_2 $ y una arista dirigida $ e = (u_1, u_2) $ (llamémosle aristas directas a las aristas de este tipo).
   - Para cada arista $ e = (u, v) \in E $, se reemplaza la arista $ (u, v) $ con las aristas dirigidas $ (u_2, v_1) $ y $ (v_2, u_1) $. (llamémosle aristas indirectas a las aristas de este tipo).

3. **Propiedad**: Cada ciclo creado en $ G' $ corresponde a una arista en el grafo original $ G $. En particular, cada arista en $ G $ crea un ciclo de 4 vértices en $ G' $.

4. **Propiedad**: Todos los nodos de $G'$ del tipo $x_1$ tienen outdegree 1, mientras que todos los nodos del tipo $x_2$ tienen indegree 1.

5. **Propiedad**: En $G'$ no hay aristas entre nodos del tipo $x_1$ y tampoco entre nodos del tipo $x_2$.

6. **Observación**: Dada una solución factible de **Minimum Feedback Arc Set** donde se hayan usado aristas indirectas se puede obtener una solución usando solo aristas directas:
   - Demostración: Sea $C$ el conjunto de aristas de la solución factible, sea $(v_2, u_1)$ una arista indirecta que pertenece a $C$. Pero por construcción, $outdegree(v_2) = indegree(u_1) = 1$, de donde podemos inferir que si $(v_2, u_1)$ pertenece a algún ciclo, entonces $(v_1, v_2)$ y $(u_1, u_2)$ también pertencen. Por tanto se puede eliminar a $(v_2, u_1)$ de $C$ y añadir a $(v_1, v_2)$. Notemos que esta arista no pertenece previamente a $C$, debido a que, al ser el conjunto de ciclos que contienen a $(v_2, u_1)$ subconjunto del conjunto de ciclos que contienen a $(v_1, v_2)$, se podría simplemente eliminar $(v_2, u_1)$ y seguiría siendo una solución factible, entrando en contradicción con la minimalidad de $C$ supuesta inicialmente. Finalmente, estamos eliminando una arista indirecta y añadiendo otra directa, siguiendo iterativamente el algoritmo descrito será posible obtener una solución usando solo aristas directas.

### Relación entre los Conjuntos

Dado un grafo no dirigido $ G = (V, E) $, un conjunto $ C $ de vértices es de cobertura si y solo si el conjunto de aristas asociadas a dichos vértices es solución de la instancia de Minimum Feedback Arc Set correspondiente a dicho grafo $ G $.

#### Demostración

1. **Vertex Cover a Minimum Feedback Arc Set**:
   - Si en el grafo original $ G $, un vértice $ u \in C $ está en el conjunto de vértices de cobertura, entonces en $ G' $, eliminaremos la arista $ (u_1, u_2) $, eliminando todos los ciclos en los que esta está presente.
   - Supongamos que luego de eliminar las aristas mencionadas anteriormente (las que representan a los vértices de la cobertura), queda algún ciclo creado en la construcción de $ G' $. Como este ciclo representa una arista en $ G $, podemos decir que esta no estaba cubierta por ninguno de los vértices del conjunto de cobertura mínima. Contradicción.
   - Supongamos que existe un ciclo $(x_{1,1}, x_{2, 1}, x_{1, 2}, x_{2, 2}, \dots, x_{1, 1})$ en $G'$ distinto a los asociados a aristas de $G$. Tomemos una secuencia cualquiera de 4 nodos $S = (x_{1, j}, x_{2, j}, x_{1, j + 1}, x_{2, j + 1})$ y veamos que existe la arista indirecta $(x_{2, j}, x_{1, j + 1})$, de donde entre los nodos $x_j, x_{j + 1}$ existe una arista en $G$, además en $G'$ no han sido eliminadas ni $(x_{1, j}, x_{2, j})$ ni $(x_{1, j + 1}, x_{2, j + 1})$. De esto podemos inferir que $S$ contiene al menos un ciclo de los asociados con aristas de $G$, las cuales no estarían cubiertas. Contradicción.

   Luego de la eliminación de las aristas correspondientes en $ G' $ al conjunto de vértices de cobertura mínima de $ G $ no deja ciclos en $ G' $, por tanto $|MVC(G)| \geq |MFAS(G')|$.

2. **Minimum Feedback Arc Set a Vertex Cover**:
   - Eliminar un ciclo de los que se crearon en la construcción de $ G' $ es equivalente a cubrir una arista en $ G $, ya que eliminar una arista directa presente en dicho ciclo representa seleccionar un vértice que cubre la arista original en $ G $.
   - Si eliminamos un conjunto de aristas de $ G' $ de manera que no queden ciclos  en $ G' $, esto corresponde a haber seleccionado un conjunto de vértices en $ G $ que cubren todas las aristas.

   Luego de seleccionar los nodos en $G$ relativos a las aristas eliminadas en $G'$, todas las aristas de $G$ quedan cubiertas, de donde $|MFAS(G')| \geq |MVC(G)|$.

Queda claro entonces que $|MVC(G)| = |MFAS(G')|$.

<!-- ### Correspondencia de Tamaños

**El Laberinto >= Minimum Vertex Cover:**

Si tenemos un algoritmo que resuelve **Vertex Cover** dado un grafo $ G = (V, E) $ y un entero $ k $, entonces podemos saber si la instancia de **El Laberinto** asociada a $ G $ tiene solución de tamaño menor  o igual que $ k $.

**El Laberinto <= Minimum Vertex Cover:**
Si tenemos un algoritmo que resuelve la instancia de **El Laberinto** asociada a un grafo $ G = (V, E) $ dado un entero $ k $, entonces podemos saber si **Minimum Vertex Cover** de $ G $ tiene solución de tamaño menor o igual que $ k $. -->

### Conclusión

Este análisis demuestra que aunque no sabemos cómo resolver nuestro problema o la cobertura de vértices de manera eficiente, si existiera una solución eficiente para **Minimum Feedback Arc Set** podríamos resolver eficientemente cualquier instancia de **Minimum Vertex Cover** y por tanto el MFAS es al menos tan difícil como MVC.

 <!-- uno de los problemas podemos resolver el otro y por lo tanto se establecen niveles relativos de dificultad entre estos problemas. -->

La transformación de $ G $ a $ G' $ se realiza en tiempo polinómico, finalmente queda demostrado que **Minimum Feedback Arc Set** es NP-completo.

### Solución Exacta

Una solución exacta para este problema consiste en comprobar cada uno de los subconjuntos posibles de aristas, buscando el menor tamaño tal que el grafo quede acíclico luego de eliminar dichas aristas. Esta solución posee una complejidad temporal $O(2^{|E|} \cdot (V + E))$

#### Optimización con Búsqueda Binaria

Para optimizar la búsqueda del tamaño mínimo del conjunto de aristas a eliminar, podemos emplear una estrategia combinando fuerza bruta con búsqueda binaria. La idea es usar búsqueda binaria sobre el tamaño del conjunto de aristas a eliminar.

Este enfoque permite reducir significativamente el espacio de búsqueda al enfocarse en tamaños específicos y verificar su viabilidad mediante un algoritmo adaptado.
