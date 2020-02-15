<div align="center">

# Sitio Web - PyCon Colombia 2021

<a href="https://github.com/PyConColombia">
  <img width="150" src="img/opimage.jpg">
</a>

[![Build Status][build-badge]][build]
[![MIT License][license-badge]][LICENSE]
[![Python Status](https://img.shields.io/badge/Python-%33.7-blue.svg?longCache=true&style=flat-square)](https://www.python.org/)
[![PRs Welcome][prs-badge]][prs] 
[![GitHub issues](https://img.shields.io/github/issues/PyConColombia/website-2019.svg?style=flat-square)](https://github.com/PyConColombia/website-2021/issues)
[![Twitter PyCon Colombia](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/pyconcolombia)

Este es el repositorio del sitio web de la PyCon Colombia 2021 servido por
[Github](https://pyconcolombia.github.io/website-develop/), y
construido utilizando [lektor](https://www.getlektor.com). Diseño original por [Edwin Jerez (El Hijo)
](https://github.com/soyelhijo).
</div>

# 🔀 Flujo de trabajo

Hay 2 ramas de git, `develop` y `production`.

## ⤴️ Develop

Es la rama por defecto y se despliega a través de gh-pages con Lektor a
https://pyconcolombia.github.io/website-develop/
(en http://develop.pycon.co)

## ⤴️ Production

Después de que se han ejecutado las pruebas de calidad (QA), los cambios
realizados en la rama `develop` se unen con la rama `production` y son
desplegados a través de gh-pages con Lektor a 
https://pyconcolombia.github.io/website-production/
(pronto en http://www.pycon.co)

# 🛠 Desarrollo local

## ✅ (Opcional) Entorno Virtual

### Instalación

* Instalar [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

* ⚠️️ Requiere previa instalación de Python ⚠️

### Crear entorno virtual

```
$ virtualenv <nombre_entorno>
```

### Activar entorno virtual

#### Windows

```
$ <nombre_entorno>\Scripts\activate
```

#### Linux

```
$ source <nombre_entorno>/bin/activate
```

## ✅ Instala Lektor

### Usando pip:
```
$ pip install -U Lektor unidecode
```

### Usando conda:

```
$ conda install lektor unidecode -c conda-forge
```

## ✅ Instala (reinstala) los `plugins` locales

```
$ lektor plugins reinstall
```

## ✅ Corre el servidor local

```
$ lektor server
```

## ⁉️ Problemas comunes

* 🔴 Si en algun momento luego de instalar python3 y crear tu virtualenv. haces `lektor server` y ves este error:

```
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCIas encoding for the environment.  Consult http://click.pocoo.org/python3/for mitigation steps.
```
Haz esto adentro de tu virtualenv:
```
export LC_ALL=en_us.UTF-8
export LANG=en_us.UTF-8
```

* 🔴 Si ves `jinja2.exceptions.UndefinedError: 'estimate_reading_time' is undefined` significa que necesitas instalar o reinstalar los `plugins` de lektor. Puedes hacer esto ejecutando

```
$ lektor plugins reinstall
```

# 🚀 Despliegue

Gracias a _Lektor Bot_ (Plugin de lektor conectado a Github), podemos desplegar nuestra web estática en diferentes repositorios (en la rama seleccionada en configuración - `gh-pages` en nuestro caso).

La configuración de dichos repositorios se encuentra en `python-colombia.lektorproject`

## ✔️ Desarrollo

```
$ lektor deploy
```

Se desplegará el contenido de la rama `develop` en `develop.pycon.co`

## ✔️✔️ Producción

```
$ lektor deploy production
```

Se desplegará el contenido de la rama `production` en `pycon.co`

___
<div align="center">

💪 Colaboradores

| [<img src="https://avatars3.githubusercontent.com/u/14989202?s=400&v=4" width="100px;"/><br /><sub><b>Alejandro E. Rendon</b></sub>](https://github.com/arendondiosa) | [<img src="https://avatars2.githubusercontent.com/u/5959590?s=400&v=4" width="100px;"/><br /><sub><b>Jonathan Vallejo Muñoz</b></sub>](https://github.com/jonathanvm13) | 
| :---: | :---: |

</div>

[build-badge]: https://img.shields.io/travis/PyConColombia/website-2021.svg?style=flat-square
[build]: https://travis-ci.org/PyConColombia/website-2021
[license-badge]: https://img.shields.io/npm/l/all-contributors.svg?style=flat-square
[license]: https://github.com/PyConColombia/website-2021/blob/develop/LICENSE
[prs-badge]: https://img.shields.io/badge/Issues-welcome-brightgreen.svg?style=flat-square
[prs]: https://github.com/PyConColombia/website-2021/issues/new