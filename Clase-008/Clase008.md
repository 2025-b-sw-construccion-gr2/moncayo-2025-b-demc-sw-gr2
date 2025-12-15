
# 🏛️ Taller Asincrónico

## SCM en el Mundo Real: De la Teoría al Caos Controlado

---

## 📌 Caso de Estudio

**Actualización de emergencia de Microsoft Windows – Patch Tuesday (Corrección de vulnerabilidad Zero-Day)**

---

## 1. Resumen del Caso

**Noticia / Evento:**
Microsoft lanzó una **actualización de seguridad de emergencia** dentro de su ciclo conocido como *Patch Tuesday*, con el objetivo de corregir una **vulnerabilidad Zero-Day** que estaba siendo explotada activamente en sistemas Windows.

**Fuente:**
Notas oficiales de seguridad de Microsoft (Microsoft Security Response Center – MSRC).

**Problema identificado:**
Se detectó una vulnerabilidad crítica que permitía a atacantes ejecutar código malicioso de forma remota sin autorización. Esta falla ponía en riesgo la confidencialidad, integridad y disponibilidad de millones de sistemas a nivel mundial, incluyendo entornos empresariales y gubernamentales.

---

## 2. Clasificación del Mantenimiento

El mantenimiento aplicado corresponde **principalmente a un Mantenimiento Correctivo**.

### Justificación:

* La vulnerabilidad ya existía en el software liberado.
* Estaba siendo explotada activamente (no era solo teórica).
* Requería una corrección inmediata para evitar daños mayores.

### Clasificación secundaria:

También puede considerarse **Preventivo**, ya que el parche reduce la probabilidad de futuros ataques similares al fortalecer la seguridad del sistema.

---

## 3. Procesos de SCM Involucrados

### 🔧 Control de Versiones

* Microsoft mantiene múltiples ramas del sistema operativo para distintas versiones de Windows (Windows 10, 11, versiones Enterprise).
* Se desarrolló el parche en **ramas específicas de emergencia**, aisladas del desarrollo regular.
* Esto permitió corregir el problema sin afectar nuevas funcionalidades en desarrollo.

### 📋 Gestión de Cambios

* El cambio fue tratado como **crítico y urgente**, acelerando su aprobación.
* Se documentó el impacto, la solución aplicada y las versiones afectadas.
* Se liberaron **boletines de seguridad oficiales** detallando el cambio, cumpliendo con la trazabilidad requerida por SCM.

---

## 4. Impacto en el Ciclo de Vida del Desarrollo de Software (SDLC)

Este evento afectó varias fases del SDLC:

### 🔹 Desarrollo

* Se modificó código del núcleo del sistema operativo para cerrar la vulnerabilidad.
* Se priorizó la corrección sobre nuevas funcionalidades.

### 🔹 Pruebas

* Se realizaron **pruebas de regresión aceleradas** para garantizar que el parche no rompiera funciones críticas.
* Se enfocaron en escenarios de seguridad y estabilidad.

### 🔹 Despliegue

* El despliegue fue **urgente y global**, mediante Windows Update.
* En entornos empresariales, los administradores debieron aplicar el parche de forma controlada pero rápida.

### 🔹 Mantenimiento

* Se monitorearon los sistemas tras la actualización para detectar fallos colaterales.
* Se emitieron correcciones adicionales en caso de incompatibilidades.

---

## 5. Beneficios del SCM en este Caso

La correcta implementación de SCM permitió:

* **Trazabilidad completa:** Identificar exactamente qué versiones de Windows eran vulnerables.
* **Control del riesgo:** Aplicar el parche sin introducir errores adicionales.
* **Recuperación rápida:** Posibilidad de revertir el cambio en caso de fallos.
* **Coordinación global:** Sincronizar equipos de desarrollo, pruebas y despliegue.
* **Confianza del usuario:** Garantizar actualizaciones seguras y documentadas.

Sin SCM, una corrección de esta magnitud habría generado caos, inconsistencias y posibles fallas masivas.

---

## ✅ Conclusión

Este caso demuestra que la **Gestión de Configuración de Software (SCM)** es esencial para manejar situaciones críticas en sistemas reales. Gracias a SCM, Microsoft pudo responder de forma rápida, organizada y segura ante una amenaza global.

El mantenimiento correctivo, apoyado por procesos sólidos de control de versiones y gestión de cambios, permitió proteger millones de sistemas sin comprometer la estabilidad del software.

En conclusión, SCM no es solo una práctica técnica, sino un pilar fundamental para la **seguridad, sostenibilidad y confiabilidad** del software moderno.
