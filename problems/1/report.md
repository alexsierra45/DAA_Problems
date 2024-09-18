## Prbolema 1

De nuestro problema se puede crear la siguiente representacion:

Tenemos un grafo G (V,E) dirigido en el cual debemos encontrar la cantidad minima de aristas a eliminar tal que el grafo resultante sea aciclico.

Nuestro siguiente paso sera demostrar que nuestro problema es NP-hard mediante una reducción polinómica desde el problema de **Minimum Vertex Cover (MVC)** visto en clases, que es NP-completo. Para hacerlo, transformaremos nuestro problema en un problema de decision, y una instancia de MVC a una instancia de nuestro problema, de tal forma que resolverlo permita resolver MVC.

### Definicion

1. **Minimum Vertex Cover (MVC)**: Dado un grafo no dirigido \( G = (V, E) \) y un número \( k \), el problema consiste en determinar si existe un subconjunto \( C \subseteq V \) de tamaño a lo sumo \( k \), tal que al menos una de las dos terminales de cada arista en \( E \) esté en \( C \).

2. **El Laberinto (EL)**: Dado un grafo dirigido \( G = (V, E) \) y un número \( k \), el problema es determinar si existe un subconjunto \( F \subseteq E \) de tamaño a lo sumo \( k \), tal que al eliminar las aristas en \( F \), el grafo resultante sea acíclico.

### Paso 1: Descripción de la Reducción

Dada una instancia de **Minimum Vertex Cover** con:

- Un grafo \( G = (V, E) \)
- Un número \( k \), 

nuestro objetivo es decidir si existe un conjunto de vértices de tamaño a lo sumo \( k \) que cubra todas las aristas del grafo.

Debemos construir un grafo \( G' = (V', E') \) que sea una instancia del problema de **El Laberinto**. En este grafo, resolver el problema EL será equivalente a resolver la instancia original de MVC.

### Paso 2: Construcción del Grafo \( G' \) para EL

1. **Toma el grafo original**: Partimos del grafo \( G = (V, E) \) de la instancia de MVC.

2. **Transformación a un grafo para EL**:
   - Para cada nodo \( u \in V \), reemplaza el nodo con 2 nuevos nodos \(u1, u2\) y una arista dirigida \( e = (u1, u2) \) (llamemosle aristas de tipo 1 a las aristas de este tipo)
   - Para cada arista \( e = (u, v) \in E \), reemplaza la arista \( u, v \) con las aristas dirigidas \( u2, v1 \) y \( v2, u1 \). (llamemosle aristas de tipo 2 a las aristas de este tipo)
   INSERTAR IMAGEN
   - El nuevo grafo \( G' = (V', E') \) contiene estos ciclos, y cada arista en \( E \) del grafo original se transforma en un ciclo en \( G' \).

3. **Propiedad**: Cada ciclo creado en \( G' \) corresponde a una arista en el grafo original \( G \). En particular, cada arista en \( G \) crea un ciclo de 5 vértices en \( G' \).

4. **Colorario**: Notese que de los nodos u1 en \( G' \) solo sale la arista \( e = (u1, u2) \), por lo que a los ciclos a los que pertenecen las aristas de tipo 2 \( v2, u1 \) tambien pertenecen las aristas de tipo 1. 

5. **Colorario**: Dada una solucion factible de **El Laberinto** donde se hayan usado aristas de tipo 2 se puede obtener una solucion usando solo aristas de tipo 1 sustituyendo cada arista \( v2, u1 \) por \( (u1, u2) \) por el colorario anterior.

### Paso 3: Relación entre los Conjuntos

1. **Vertex Cover a El Laberinto**:
   - Si en el grafo original \( G \), un vértice \( u \in C \) está en el conjunto de vértices de cobertura mínima, entonces en \( G' \), eliminaremos la arista \( u1, u2 \), eliminando todos los ciclos en los que esta esta presente. 
   - Supongamos que luego de eliminar las aristas mencionadas anteriormente (las que representan a los vertices de la cobertura minima) queda algun ciclo creado en la construccion de \( G' \). Como este ciclo representa una arista en \( G \) podemos decir que esta no estaba cubierta por ninguno de los vertices del conjunto de cobertura minima(Contradiccion).
   - Supongamos que pueda existir un ciclo distinto a los creados en la construccion, sin que exista uno de estos. (u1, u2, v1, v2... u1)
   Notese que si de u2 hay una arista a v1 significa que en \( G \) existe la arista \(u, v\) y que las aristas \((u1, u2), (v1, v2)\) no han sido eliminadas. Como no se eliminan aristas de tipo 2, el ciclo (u1, u2, v1, v2, u1) creado en la construccion de \( G' \) aun existe(Contradiccion).

   Luego la eliminacion de las aristas correspondientes en \( G' \) al conjunto de vertices de cobertura minima de \( G \) no deja ciclos en \( G' \).

2. **El Laberinto a Vertex Cover**:
   - Eliminar un ciclo de los que se crearon en la construccion de \( G' \) es equivalente a cubrir una arista en \( G \), ya que seleccionamos una arista de tipo 1 presente en dicho ciclo para eliminar, lo que representa seleccionar un vértice que cubre la arista original en \( G \).
   - Si eliminamos aristas de \( G' \) de manera que no queden ciclos  en \( G' \), esto corresponde a haber seleccionado un conjunto de vértices en \( G \) que cubren todas las aristas.

### Paso 4: Correspondencia de Tamaños

Encontrar una solución de EL en \( G' \) de tamaño a lo sumo \( k \) corresponde a encontrar una solución de Vertex Cover en \( G \) de tamaño a lo sumo \( k \). Dado que eliminamos una arista de cada ciclo creado en la construccion para romper el ciclo, esto es equivalente a cubrir una arista en el grafo original.

### Paso 5: Conclusión

Si podemos resolver el **EL Laberinto (EL)** en el grafo \( G' \), entonces podemos resolver el **Minimum Vertex Cover (MVC)** en el grafo original \( G \). La transformación de \( G \) a \( G' \) se realiza en tiempo polinómico, y por lo tanto, hemos demostrado que EL es NP-hard.
   