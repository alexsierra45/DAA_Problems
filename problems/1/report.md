## Problema 1

De nuestro problema se puede crear la siguiente representación:

Tenemos un grafo \( G (V,E) \) dirigido en el cual debemos encontrar la cantidad mínima de aristas a eliminar tal que el grafo resultante sea acíclico.

Nuestro siguiente paso será demostrar que nuestro problema es NP-hard mediante una reducción polinómica desde el problema de **Minimum Vertex Cover (MVC)** visto en clases, que es NP-completo. Para hacerlo, transformaremos nuestro problema en un problema de decisión, y una instancia de MVC a una instancia de nuestro problema, de tal forma que resolverlo permita resolver MVC.

Primero, demostraremos que el problema pertenece a la clase NP:

Dado un grafo y una posible solución, es fácil verificar en tiempo lineal si el conjunto de aristas dado al ser eliminado da como resultado un grafo acíclico, simplemente haciendo un recorrido DFS para verificar la no existencia de aristas de retroceso, lo cual indica que el grafo resultante es acíclico.

### Definición

1. **Minimum Vertex Cover (MVC)**: Dado un grafo no dirigido \( G = (V, E) \) y un número \( k \), el problema consiste en determinar si existe un subconjunto \( C \subseteq V \) de tamaño a lo sumo \( k \), tal que al menos una de las dos terminales de cada arista en \( E \) esté en \( C \).

2. **El Laberinto (EL)**: Dado un grafo dirigido \( G = (V, E) \) y un número \( k \), el problema es determinar si existe un subconjunto \( F \subseteq E \) de tamaño a lo sumo \( k \), tal que al eliminar las aristas en \( F \), el grafo resultante sea acíclico.

### Descripción de la Reducción

Dada una instancia de **Minimum Vertex Cover** con:

- Un grafo \( G = (V, E) \)
- Un número \( k \),

nuestro objetivo es decidir si existe un conjunto de vértices de tamaño a lo sumo \( k \) que cubra todas las aristas del grafo.

Debemos construir un grafo \( G' = (V', E') \) que sea una instancia del problema de **El Laberinto**. En este grafo, resolver el problema EL será equivalente a resolver la instancia original de MVC.

### Construcción del Grafo \( G' \) para EL

1. **Toma el grafo original**: Partimos del grafo \( G = (V, E) \) de la instancia de MVC.

2. **Transformación a un grafo para EL**:
   - Para cada nodo \( u \in V \), reemplaza el nodo con 2 nuevos nodos \( u1, u2 \) y una arista dirigida \( e = (u1, u2) \) (llamémosle aristas de tipo 1 a las aristas de este tipo).
   - Para cada arista \( e = (u, v) \in E \), reemplaza la arista \( u, v \) con las aristas dirigidas \( u2, v1 \) y \( v2, u1 \). (llamémosle aristas de tipo 2 a las aristas de este tipo).
   - El nuevo grafo \( G' = (V', E') \) contiene estos ciclos, y cada arista en \( E \) del grafo original se transforma en un ciclo en \( G' \).

3. **Propiedad**: Cada ciclo creado en \( G' \) corresponde a una arista en el grafo original \( G \). En particular, cada arista en \( G \) crea un ciclo de 5 vértices en \( G' \).

4. **Observación**: Nótese que de los nodos \( u1 \) en \( G' \) solo sale la arista \( e = (u1, u2) \), por lo que a los ciclos a los que pertenecen las aristas de tipo 2 \( v2, u1 \) también pertenecen las aristas de tipo 1.

5. **Observación**: Dada una solución factible de **El Laberinto** donde se hayan usado aristas de tipo 2 se puede obtener una solución usando solo aristas de tipo 1 sustituyendo cada arista \( v2, u1 \) por \( (u1, u2) \) por la observación anterior.

### Relación entre los Conjuntos

#### Dado un grafo no dirigido \( G = (V, E) \), un conjunto \( C \) de vértices es de cobertura si y solo si el conjunto de aristas asociadas a dichos vértices es solución (no necesariamente mínima) de la instancia de EL Laberinto correspondiente a dicho grafo \( G \).

#### Demostración:

1. **Vertex Cover a El Laberinto**:
   - Si en el grafo original \( G \), un vértice \( u \in C \) está en el conjunto de vértices de cobertura, entonces en \( G' \), eliminaremos la arista \( u1, u2 \), eliminando todos los ciclos en los que esta está presente.
   - Supongamos que luego de eliminar las aristas mencionadas anteriormente (las que representan a los vértices de la cobertura) queda algún ciclo creado en la construcción de \( G' \). Como este ciclo representa una arista en \( G \), podemos decir que esta no estaba cubierta por ninguno de los vértices del conjunto de cobertura mínima (Contradicción).
   - Supongamos que pueda existir un ciclo distinto a los creados en la construcción, sin que exista uno de estos. (\(u1, u2, v1, v2... u1 \))
   Nóteses que si desde \( u2 \) hay una arista a \( v1 \), significa que en \( G \) existe la arista \( u,v \) y que las aristas \((u1,u2), (v1,v2)\) no han sido eliminadas. Como no se eliminan aristas de tipo 2, el ciclo (\(u1,u2,v1,v2,u1\)) creado en la construcción de \( G' \) aún existe (Contradicción).

   Luego la eliminación de las aristas correspondientes en \( G' \) al conjunto de vértices de cobertura mínima de \( G \) no deja ciclos en \( G' \).

2. **El Laberinto a Vertex Cover**:
   - Eliminar un ciclo de los que se crearon en la construcción de \( G' \) es equivalente a cubrir una arista en \( G \), ya que seleccionamos una arista de tipo 1 presente en dicho ciclo para eliminar, lo que representa seleccionar un vértice que cubre la arista original en \( G \).
   - Si eliminamos un conjunto de aristas de \( G' \) de manera que no queden ciclos  en \( G' \), esto corresponde a haber seleccionado un conjunto de vértices en \( G \) que cubren todas las aristas.

### Correspondencia de Tamaños

**El Laberinto >= Minimum Vertex Cover:**

Si tenemos un algoritmo que resuelve **Vertex Cover** dado un grafo \( G = (V, E) \) y un entero \( k \), entonces podemos saber si la instancia de **El Laberinto** asociada a \( G \) tiene solución de tamaño menor  o igual que \( k \).

**El Laberinto <= Minimum Vertex Cover:**
Si tenemos un algoritmo que resuelve la instancia de **El Laberinto** asociada a un grafo \( G = (V, E) \) dado un entero \( k \), entonces podemos saber si **Minimum Vertex Cover** de \( G \) tiene solución de tamaño menor o igual que \( k \).


### Conclusión

Este análisis demuestra que aunque
no sabemos cómo resolver nuestro problema o la cobertura de vértices de manera eficiente, dada una solución eficiente para uno de los problemas podemos resolver el otro y por lo tanto se establecen niveles relativos de dificultad entre estos problemas.

La transformación de \( G \) a \( G' \) se realiza en tiempo polinómico, y por lo tanto hemos demostrado que **El Laberinto** es NP-hard.

### Solución Exacta:

Una solución exacta para este problema consiste en comprobar cada uno de los subconjuntos posibles de aristas, buscando el menor tamaño tal que el grafo quede acíclico luego de eliminar dichas aristas. Esta solución posee una complejidad temporal $$O(2^n n^2)$$

#### Optimización con Búsqueda Binaria

Para optimizar la búsqueda del tamaño mínimo del conjunto de aristas a eliminar, podemos emplear una estrategia combinando fuerza bruta con búsqueda binaria. La idea es usar búsqueda binaria sobre el tamaño del conjunto de aristas a eliminar.

Este enfoque permite reducir significativamente el espacio de búsqueda al enfocarse en tamaños específicos y verificar su viabilidad mediante un algoritmo adaptado.