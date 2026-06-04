# Reflexión Final y Ejercicios Escritos

## Ejercicio 5. Crítica técnica de una solución generada automáticamente

La solución propuesta por la herramienta automática afirma que para atender estudiantes en orden de llegada se puede usar una pila, donde cada estudiante se inserta con push y se atiende con pop. El argumento es que esto "garantiza que el primero en llegar sea el primero en salir". Esta afirmación es incorrecta en su fundamento conceptual.

El error central es confundir dos principios de organización opuestos. Una pila funciona bajo el principio LIFO, que significa que el último elemento insertado es el primero en ser retirado. Una cola funciona bajo el principio FIFO, que significa que el primer elemento insertado es el primero en ser atendido. Ambas estructuras pueden parecer similares desde afuera porque ambas almacenan elementos en secuencia, pero su comportamiento interno es radicalmente diferente y no son intercambiables en un problema de atención por orden de llegada.

Un ejemplo concreto ilustra el fallo. Si tres estudiantes llegan en el orden A, B y C, y se insertan en ese orden en una pila, la estructura interna queda con C en la cima. Al ejecutar pop, se retira C primero, luego B, y finalmente A. El resultado es C, B, A, que es exactamente el orden inverso al de llegada. Si el objetivo es que el primero en llegar sea el primero en ser atendido, este resultado es incorrecto. Una cola produce el orden A, B, C, que sí respeta el criterio del problema.

La corrección adecuada del problema requiere reemplazar la pila por una cola. En Python esto se implementa de forma eficiente con deque de la librería collections. Los estudiantes se agregan con append al final de la cola, y se atienden con popleft desde el frente, garantizando el orden FIFO en tiempo O(1) por operación.

La razón por la que una respuesta generada automáticamente puede parecer correcta aunque no lo sea es que la herramienta construyó una explicación con terminología técnica coherente. La frase "primero en llegar, primero en salir" fue incluida en el texto, pero la estructura de datos seleccionada implementa exactamente lo contrario. Esto ocurre porque los modelos de generación automática producen texto que suena plausible basándose en patrones lingüísticos, no porque hayan ejecutado mentalmente el algoritmo paso a paso. Una solución puede estar redactada con confianza y claridad aparente y al mismo tiempo contener un error conceptual grave que solo se detecta al rastrear la lógica con un ejemplo concreto. Por eso es indispensable que el estudiante verifique siempre el comportamiento real de la estructura elegida antes de aceptar una sugerencia, especialmente cuando la justificación parece demasiado breve o demasiado general.

## Ejercicio 6. Defensa técnica de la solución del validador de trazas

El problema resuelto en el ejercicio 2 consiste en determinar si una secuencia de acciones realizadas por un estudiante durante una evaluación virtual es coherente. Las acciones posibles son abrir una pregunta, responder una pregunta, guardar una respuesta, volver al estado anterior y enviar la evaluación. Una traza es inválida si, por ejemplo, se intenta responder una pregunta que no es la que está actualmente abierta, se ejecuta una acción de volver cuando no hay ningún contexto activo, o se intenta enviar con preguntas aún abiertas.

Las dos estructuras de datos centrales en la solución son una cola y una pila. La cola almacena todas las acciones de la traza antes de procesarlas, y garantiza que se examinen en el orden exacto en que llegaron. La pila registra el contexto de navegación activo, es decir, qué pregunta está abierta en cada momento. Cuando se abre una pregunta, su número se apila. Cuando se ejecuta un VOLVER, el número en la cima se desapila. Cuando se intenta responder o guardar, se verifica que el número indicado coincida con el elemento en la cima de la pila.

La cola fue elegida porque el problema exige respetar estrictamente el orden de llegada de las acciones, lo que es exactamente la propiedad que garantiza la estructura FIFO. Usar una lista y acceder por índice habría sido posible, pero menos expresivo y con mayor costo en la operación de extracción por el frente. La pila fue elegida porque el contexto de navegación tiene una naturaleza anidada: abrir una pregunta crea un nuevo nivel de contexto, y volver regresa al nivel anterior. Esto corresponde exactamente al comportamiento LIFO de una pila.

La complejidad temporal de la solución es O(n), donde n es el número de acciones en la traza. Cada acción se extrae de la cola exactamente una vez y se procesa en tiempo constante. La complejidad espacial también es O(n) en el peor caso, cuando todas las acciones son aperturas de preguntas sin ningún VOLVER, lo que hace que la pila crezca hasta almacenar n elementos.

El caso límite más importante fue el de intentar responder una pregunta cuando el contexto activo en la pila es diferente. Este es el caso que separa este problema del problema clásico de paréntesis balanceados. En el de paréntesis, basta con verificar que la pila no esté vacía. Aquí es necesario verificar también que el número en la cima corresponda exactamente a la acción que se quiere ejecutar, lo que añade una capa semántica al control estructural.

Si el tamaño de entrada creciera diez veces, la solución seguiría siendo eficiente porque su complejidad es lineal y no depende de estructuras que degraden su rendimiento con el volumen. El único riesgo teórico sería que la pila creciera demasiado si hubiera miles de preguntas abiertas simultáneamente sin ningún VOLVER, pero eso correspondería a un escenario de datos de entrada anómalo más que a un problema algorítmico.

La parte más vulnerable a errores en esta solución es el parsing de las cadenas de texto para extraer el número de pregunta. Si el formato de la acción varía, por ejemplo si los paréntesis son diferentes o hay espacios adicionales, la extracción del número fallará. Esta fragilidad podría resolverse con expresiones regulares o con un parser más robusto que valide el formato antes de intentar interpretarlo. En el contexto del parcial, el formato fue asumido como fijo, pero en un sistema real esto requeriría validación adicional.

## Reflexión final

El ejercicio más difícil fue el de backtracking. La dificultad no estuvo en entender el concepto sino en manejar correctamente el estado compartido de la lista de asignaciones a lo largo de las llamadas recursivas. En un primer intento, la lista no se restauraba correctamente al retroceder, lo que producía resultados incorrectos en los casos donde no había solución. La corrección consistió en asegurarse de que cada pop correspondiera exactamente a cada append, de modo que al explorar una rama inválida el estado volviera a ser exactamente el mismo que antes de entrar a esa rama.

La estructura de datos que quedó más clara durante el parcial fue la pila. El ejercicio 2 mostró de manera muy concreta cómo la propiedad LIFO sirve para modelar contextos anidados, y el ejercicio 5 reforzó por contraste por qué no se puede sustituir por una cola cuando el orden importa en la dirección opuesta.

Un error cometido durante el desarrollo fue no incluir inicialmente el caso de ENVIAR con preguntas abiertas en el validador. La primera versión retornaba "Valida" al encontrar la acción ENVIAR sin verificar si la pila tenía elementos. Al construir los casos de prueba se detectó este vacío y se corrigió agregando una verificación explícita.

La inteligencia artificial fue útil para revisar la estructura general de las funciones recursivas y para confirmar el comportamiento esperado de deque. Sin embargo, en el ejercicio de backtracking generó una versión que usaba una variable global para las asignaciones, lo cual hacía el código difícil de probar de manera aislada. Esa parte fue reescrita para pasar el estado como argumento.

Lo más importante aprendido en este parcial es que obtener una respuesta y comprender una solución son dos cosas distintas. Una herramienta puede producir código que funcione en el caso de prueba visible y falle en un caso límite que no se consideró. La comprensión es lo que permite anticipar esos casos antes de que ocurran en producción.

## Declaración de uso de herramientas externas

Se utilizó asistencia de inteligencia artificial durante el desarrollo del parcial.

Se utilizó para revisar la estructura de las funciones recursivas del ejercicio 3 y para confirmar el comportamiento de deque en el ejercicio 2.

Las partes modificadas o corregidas fueron la implementación del backtracking, que fue reescrita para eliminar el uso de variable global, y el validador de trazas, al que se le agregó el caso de ENVIAR con contexto activo no vacío.

La limitación encontrada fue que en el ejercicio 4 la sugerencia usaba una lista global mutable que no se reseteaba entre pruebas, lo que causaba que el segundo caso de prueba heredara el estado del primero y produjera resultados incorrectos.
