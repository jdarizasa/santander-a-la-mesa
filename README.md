[![Dev Environment Prebuilds](https://github.com/jdarizasa/Integration_ColombianPublicDatasets/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/jdarizasa/Integration_ColombianPublicDatasets/actions/workflows/codespaces/create_codespaces_prebuilds)

# Sistemas alimentarios, territorio y vulnerabilidad en Santander: un análisis reproducible con datos abiertos.

🌱 Sobre este proyecto
Este es un proyecto personal de ciencia de datos que busca entender cómo funciona el sistema alimentario de Santander, Colombia: qué se produce, por dónde circula, a qué precio llega, y quién queda por fuera. La motivación nace de una idea sencilla: la comida no es un commodity neutro que aparece en la mesa. Es el resultado de una cadena de decisiones, infraestructuras, climas y desigualdades que rara vez se analizan en conjunto.

La lectura de Ciudades hambrientas de Carolyn Steel fue el detonante. Su argumento de que la comida es el hilo que conecta geografía, poder y cultura me hizo querer trasladar esa mirada a un territorio concreto. Santander - Colombia, con el contraste entre su área metropolitana y provincias, ofrece un laboratorio natural para explorar esas tensiones.

🔍 Preguntas que guían el análisis
- ¿Los municipios productores de alimentos básicos tienen menores precios de canasta básica que los municipios consumidores? ¿La mala conectividad vial anula esa ventaja?

- ¿Los municipios con mayor variabilidad climática tienen mayor prevalencia de inseguridad alimentaria? ¿La infraestructura de riego amortigua ese efecto?

- ¿Los municipios con mayor pobreza multidimensional son también los de menor diversidad productiva, y por tanto más vulnerables a shocks de precios o clima?

- ¿El estado de las vías terciarias predice la inseguridad alimentaria municipal, incluso controlando por pobreza y producción?

- ¿La inversión pública en infraestructura vial y agropecuaria sigue a la necesidad, o responde a otras lógicas?

Estas preguntas son hipótesis de trabajo, no un plan cerrado. El proyecto es exploratorio por diseño: la dirección puede ajustarse a medida que los datos revelen lo que no esperábamos.

📚 Fuentes de datos
Todas las fuentes son de acceso público y abierto. La intención es integrarlas en una capa de datos armonizada a nivel municipal

Cada fuente se documenta en docs/data_dictionary.md y se extrae mediante un script reproducible en src/extraction/. Los datos crudos nunca se versionan en el repositorio; se reconstruyen desde los scripts.

🛠️ Enfoque técnico
El proyecto se construye en GitHub Codespaces con:

- Python para extracción (APIs de Socrata, requests, sodapy), transformación (pandas, DuckDB) y modelado (scikit-learn).

- R para análisis espacial (sf), visualización (ggplot2, leaflet) y, potencialmente, publicación (Quarto).

- DuckDB como motor de consulta local para manejar datos de tamaño medio sin cargar todo en memoria.

La infraestructura es la prioridad. Antes de construir cualquier visualización, el objetivo es tener un pipeline reproducible.

📤 Estrategia de comunicación
La intención es un enfoque híbrido:

Un pipeline reproducible que extrae, limpia y armoniza las fuentes. Es el esqueleto del proyecto y su principal activo técnico.

Un dashboard interactivo que permita explorar los cruces entre producción, vías, clima y pobreza. El prototipo inicial será en Streamlit por su rapidez; la versión final podría consolidarse como Quarto Dashboard, que permite integrar narrativa y exploración en un mismo documento y publicarse en GitHub Pages sin costo.

Un reporte narrativo que explique los hallazgos, las decisiones metodológicas y sus limitaciones. 

El formato final no está cerrado. Se definirá cuando el análisis exploratorio revele qué vale la pena comunicar y a quién.

🧭 Estado y filosofía del proyecto
Este es un proyecto personal, sin presupuesto, sin deadlines y sin presión externa. Su valor no está en la velocidad de entrega, sino en la calidad del proceso: la trazabilidad de las decisiones, la reproducibilidad del pipeline y la honestidad sobre los límites de los datos.

El repositorio sigue algunas prácticas deliberadas:

- ADRs (docs/decisions/) para registrar decisiones metodológicas y técnicas.

- Bitácora (docs/journal.md) con entradas fechadas sobre lo que funcionó, lo que no y lo que se aprendió.

- Issues para tareas y preguntas abiertas, incluso en solitario.

- Commits pequeños y descriptivos, para que el historial cuente la historia del proyecto.

No hay una fecha de finalización. Hay una dirección: entender mejor cómo se alimenta Santander, y hacerlo de una forma que otros puedan reproducir, cuestionar y extender.
