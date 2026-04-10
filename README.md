
# Proyecto 6: Computer Vision

## Descripción

Este proyecto implementa un sistema básico de verificación facial utilizando la librería **DeepFace**. El objetivo es simular un inicio de sesión seguro donde se valida la identidad de un usuario comparando su rostro con una imagen previamente registrada.

El sistema analiza dos imágenes y determina si pertenecen a la misma persona, permitiendo o denegando el acceso.

---

## Instrucciones de uso

### 1. Clonar repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd nombre_del_repo
```

---

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

Activar entorno:

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / Mac:**

```bash
source .venv/bin/activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Ejecutar el proyecto

```bash
python app.py
```

---

## Uso del sistema

* Colocar una imagen del usuario registrado (ej. `usuario.jpg`)
* El sistema usará otra imagen (ej. `login.jpg`)
* Se realizará la comparación facial
* El sistema mostrará:

  * "Acceso permitido" si coincide
  * "Acceso denegado" si no coincide

---

## Tecnologías utilizadas

* Python
* DeepFace
* OpenCV

