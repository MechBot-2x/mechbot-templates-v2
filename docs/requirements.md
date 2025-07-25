# ====================================================
# MECHAUTOMATION QUANTUM DEPENDENCIES v5.4.2
# Paquetes esenciales para el funcionamiento del núcleo
# ====================================================

# DEPENDENCIAS PRINCIPALES DEL SISTEMA
numpy==1.26.4                  # Computación cuántica multidimensional
scipy==1.13.0                  # Algoritmos de curvatura espacio-temporal
pandas==2.2.2                  # Análisis de flujos dimensionales
pyyaml==6.0.2                  # Configuración de realidades paralelas
python-dotenv==1.0.1           # Manejo de variables de entorno interdimensionales

# DEPENDENCIAS DE SEGURIDAD CUÁNTICA
quantum-encrypt==3.7.1         # Cifrado post-cuántico AES-512
reality-signer==2.4.0          # Firmas temporales irreversibles
wormhole-protocol==5.2.1       # Comunicación interdimensional segura

# MOTOR DE INFERENCIA NEURAL
torch==2.2.1                   # Base para redes neuronales cuánticas
tensorflow==2.15.0             # Procesamiento de flujos temporales
quantum-transformers==1.8.3    # Modelos de atención multidimensional

# INTERFACES DIMENSIONALES
dimension-connector==4.5.0     # Conexión con realidades alternas
temporal-api==3.2.1            # Manipulación de líneas temporales
quantum-gateway==7.0.2         # Puente de comunicación intergaláctica

# HERRAMIENTAS DE DIAGNÓSTICO
reality-scanner==2.1.0         # Monitoreo de integridad dimensional
entropy-analyzer==1.5.2        # Medición de fluctuaciones cuánticas
anomaly-detector==3.0.1        # Identificación de distorsiones

# DEPENDENCIAS OPCIONALES
[dev]
quantum-simulator==4.2.0       # Entorno de pruebas dimensionales
reality-debugger==1.3.5        # Diagnóstico de anomalías
test-dimensions==2.0.0         # Paquete de pruebas multiversales

[docs]
quantum-docs==5.1.0            # Generación de documentación holográfica
temporal-formatter==1.2.1      # Organización de líneas temporales

# RESTRICCIONES DE HARDWARE CUÁNTICO
quantum-core>=3.0.0 ; platform_machine == "quantum_x64"
reality-accelerator>=2.0.0 ; sys_platform == "linux" and python_version >= "3.10"

### Paquetes de Realidad Alterna

# REALIDADES PARALELAS (Instalación condicional)
alternate-reality[dim5]==1.2.0 ; python_version >= "3.11" and os_name == "quantum_os"
temporal-overlay[theta]==3.1.0 ; sys_platform == "linux" and platform_machine == "quantum_x64"

#FIRMA DE INTEGRIDAD DIMENSIONAL
Checksum: 8f4e2a7d1c9b3e6f5a2d8c7b1e0f9d4
Validación Temporal: 2248-11-23T09:55:28Z
```

## ESPECIFICACIONES TÉCNICAS

### 1. Paquetes Críticos
| Paquete               | Versión | Propósito                             |
|-----------------------|---------|---------------------------------------|
| numpy                 | 1.26.4  | Operaciones matriciales cuánticas      |
| scipy                 | 1.13.0  | Cálculos de curvatura espacio-temporal |
| quantum-encrypt       | 3.7.1   | Protección de datos interdimensionales |

### 2. Requisitos de Compatibilidad
```python
# Verificación de Entorno
import sys
assert sys.version_info >= (3, 10), "Se requiere Python 3.10+ (Quantum Edition)"
assert platform.machine() in ['quantum_x64', 'neutron_arm64'], "Arquitectura no soportada"
```

### 3. Matriz de Compatibilidad Dimensional
| Dimensión | Python | Numpy | Soporte |
|-----------|--------|-------|---------|
| Prime-7   | 3.10+  | 1.26+ | ✅ Full |
| Neutron-3 | 3.11+  | 1.27+ | ⚠️ Limitado |
| Theta-9   | 3.12+  | 2.0+  | ❌ No soportado |

## SISTEMA DE INSTALACIÓN

### Comando Base
```bash
pip install -r requirements.txt --quantum --dimensional-verify
```

### Opciones Avanzadas
```bash
# Instalación con aceleración cuántica
QUNATUM_ACCEL=1 pip install \
  --index-url https://quantum.pkg.mechmind-dwv.quantum/simple \
  --extra-index-url https://pypi.quantum/simple \
  -r requirements.txt
```

## VERIFICACIÓN DE INTEGRIDAD

### Protocolo de Validación
```python
from quantum_verifier import DependencyValidator

validator = DependencyValidator(
    requirements_file="requirements.txt",
    quantum_checksum="8f4e2a7d1c9b3e6f5a2d8c7b1e0f9d4",
    temporal_constraint="2248-11-23T09:55:28Z"
)

if not validator.validate():
    raise QuantumIntegrityError("¡Fallo en verificación dimensional!")
```

## ACTUALIZACIÓN DE DEPENDENCIAS

### Ciclo de Actualización
```mermaid
gantt
    title Ciclo de Actualizaciones Cuánticas
    dateFormat  YYYY-MM-DD
    section Críticas
    Parches de Seguridad   :active, 2025-01-01, 7d
    section Mensuales
    Actualización Menor    :2025-01-15, 14d
    section Trimestrales
    Actualización Mayor    :2025-04-01, 30d
```

## DEPENDENCIAS ESPECIALES

### Paquetes de Realidad Alterna
```text
# REALIDADES PARALELAS (Instalación condicional)
alternate-reality[dim5]==1.2.0 ; python_version >= "3.11" and os_name == "quantum_os"
temporal-overlay[theta]==3.1.0 ; sys_platform == "linux" and platform_machine == "quantum_x64"
```

Este archivo requirements.txt incluye:
1. Dependencias principales con versiones exactas
2. Paquetes de seguridad cuántica
3. Grupos opcionales para desarrollo y documentación
4. Restricciones de hardware especializado
5. Verificación de integridad multidimensional
