# Agencia de Viajes - Proyecto (Factory Method & Observer)

## Resumen
Este repositorio contiene un proyecto educativo que ilustra la aplicación de dos patrones de diseño:
- **Factory Method**: para la creación flexible de paquetes de viaje (económico, estándar, premium).
- **Observer**: para notificar a clientes y aplicaciones cuando la agencia publica promociones o actualiza reservas.

El objetivo es usar estos ejemplos como material de apoyo para la asignatura de Ingeniería de Software.

## Estructura del proyecto (sugerida)
agencia-viajes/
├─ README.md
├─ src/
│ ├─ factory/
│ │ ├─ paquete.py
│ │ └─ agencia.py
│ ├─ observer/
│ │ ├─ agencia_observer.py
│ │ └─ clientes.py
│ └─ main.py
├─ docs/
│ ├─ UML_Observer.png
│ └─ UML_FactoryMethod.png
└─ tests/
└─ test_agencia.py

markdown
Copiar código

> **Nota:** En este repositorio de ejemplo, el diagrama UML generado está disponible en:  
`/mnt/data/A_UML_class_diagram_in_digital_2D_illustration_ill.png`

## Contenido clave
- `src/factory/paquete.py`: define la interfaz `PaqueteViaje` y las implementaciones `PaqueteEconomico`, `PaqueteStandard`, `PaquetePremium`.
- `src/factory/agencia.py`: contiene la clase `AgenciaDeViajes` como Creator y sus subclases que implementan `crear_paquete()`.
- `src/observer/agencia_observer.py`: implementación del `Subject` (Agencia) con métodos `agregar_observador`, `eliminar_observador`, `notificar` y manejo de `promocion`.
- `src/observer/clientes.py`: clases observadoras `ClienteRegular`, `ClienteVIP`, y `AplicacionMovil`.
- `src/main.py`: script de ejemplo que muestra uso de ambos patrones juntos.

## Requisitos
- Python 3.8+ (o la versión que uses en el curso)
- (Opcional) pytest para pruebas unitarias
- (Opcional) ReportLab si quieres generar PDFs desde Python

## Ejecución de ejemplo
1. Clonar el repositorio:
```bash
git clone <url-del-repo>
cd agencia-viajes
Ejecutar el ejemplo principal:

bash
Copiar código
python src/main.py
Ejecutar pruebas (si hay):

bash
Copiar código
pytest
Ejemplo rápido de uso
python
Copiar código
from factory.agencia import AgenciaEconomica, AgenciaPremium
from observer.agencia_observer import AgenciaDeViajesObserver
from observer.clientes import ClienteRegular, ClienteVIP

# Factory: crear paquetes
ag_econ = AgenciaEconomica()
print(ag_econ.reservar())  # Reserva usando PaqueteEconomico

# Observer: notificar promociones
agencia = AgenciaDeViajesObserver()
juan = ClienteRegular("Juan")
maria = ClienteVIP("María")
agencia.agregar_observador(juan)
agencia.agregar_observador(maria)
agencia.nueva_promocion("50% en paquetes a Cartagena")
