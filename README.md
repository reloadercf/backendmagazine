# Instrucciones para uso del backend 🚀
### `Consulta de Usuario en revista`
Para hacer una consulta referente a los perfiles registrados tiene que usar como elemento de busqueda en la api el nombreregistro-perfiles del usuario, su id de usuario, su nombre, su apellido o su id de la revista a la pertenece, para ello debes usar la siguiete url ( recuerda que el nombre de usuarios es el que se registro con la contraseña, el id de usuario es el identificador de cada perfil, el id de revista es el identificador de cada una de estas).
```
http://localhost:8000/accounts/registro-perfiles/?username=nombre_de_usuario_para_login``
http://localhost:8000/accounts/registro-perfiles/?iduser=identificador_de_usuario``
http://localhost:8000/accounts/registro-perfiles/?first=nombre_de_usuario``
http://localhost:8000/accounts/registro-perfiles/?last=apellido_de_usuario``
http://localhost:8000/accounts/registro-perfiles/?idrevista=identificador_de_la_revista``
```

### `Consulta de Revista - Usuario`
Debes entrar al siguiente endpoint:
Dentro de este endpoint se pueden filtrar las relación de revista y usuario por ir de usuario o id de la revista
(recuerda que idrevista es el numero que identifica a cada revista e iduser es el identificador de cada usuario)
```
http://localhost:8000/accounts/revista-usuario/?idrevista=identificador_de_la_revista``
http://localhost:8000/accounts/revista-usuario/?iduser=identificador_del_usuario``
```

### `Consulta de Datos del usuario con el que se inicio sesion`
Debes entrar al siguiente endpoint:
```
http://localhost:8000/my_user/``
```

### `Consulta de categorias`
Debes entrar al siguiente endpoint:
Dentro de este endpoint se pueden filtrar las categria por el identificador de cada categoria o el identificador de la revista
(recuerda que idcategoria es el numero que identifica a cada categoria e idrevista es el identificador de cada revista)
```
http://localhost:8000/revista/resgistro-de-categoria/?idcategoria=identificador_de_la_categoria``
http://localhost:8000/revista/resgistro-de-categoria/?idrevista=identificador_de_la_revista``
```

### `Consulta de revistas`
Debes entrar al siguiente endpoint:
Dentro de este endpoint se pueden filtrar las revistas por el identificador de cada revista, el plan de la revista, el país en al que pertenece la revista o el estado.
(recuerda que idrevista es el identificador de cada revista, idplan es el identificador del plan contratado por la revista, idpais es el identificador del pais al que pertenece la revista, idestado es el identificador del estado al que pertenece la revista)
````
http://localhost:8000/revista/registro-de-revista/?idrevista=identificador_de_la_revista``
http://localhost:8000/revista/registro-de-revista/?idplan=identificador_del_plan``
http://localhost:8000/revista/registro-de-revista/?idpais=identificador_del_pais``
http://localhost:8000/revista/registro-de-revista/?idestado=identificador_del_estado``
```

### `Consulta de artículos especiales`
Debes entrar al siguiente endpoint:
Dentro de este endpoint se pueden filtrar los articulos especiales por su categoria, subcategria, revista de origen, su slug, su posicion o su estatus
(recuerda que idrevista es el identificador de cada revista, idcategoria es el identificador de la categoria de ese articulo, idsubcategoria es el identificadr de la subcategoria a la que pertenece el articulo, slug es el titulo del articulo validado como slug, portada es el valor del checkbox, status es el valor que tiene el articulo)
```
http://localhost:8000/articulo/registros-de-especiales/?idrevista=identificador_de_la_revista``
http://localhost:8000/articulo/registros-de-especiales/?idcategoria=identificador_de_la_categoria``
http://localhost:8000/articulo/registros-de-especiales/?idsubcategoria=identificador_de_la_subcategoria``
http://localhost:8000/articulo/registros-de-especiales/?slug=slug_de_titulo
http://localhost:8000/articulo/registros-de-especiales/?portada=validación``
http://localhost:8000/articulo/registros-de-especiales/?status=vaidación``
```

### `Consulta de artículos`
Debes entrar al siguiente endpoint:
Dentro de este endpoint se pueden filtrar los articulos especiales por su categoria, subcategria, revista de origen, su slug o su fecha de finalizacion.
(recuerda que idrevista es el identificador de cada revista, idcategoria es el identificador de la categoria de ese articulo, idsubcategoria es el identificadr de la subcategoria a la que pertenece el articulo, slug es el titulo del articulo validado como slug, fin es la fecha hasta la cual durara el articulo)
```
http://localhost:8000/articulo/registros-de-articulos/?idrevista=identificador_de_la_revista``
http://localhost:8000/articulo/registros-de-articulos/?idcategoria=identificador_de_la_categoria``
http://localhost:8000/articulo/registros-de-articulos/?idsubcategoria=identificador_de_la_subcategoria``
http://localhost:8000/articulo/registros-de-articulos/?slug=slug_de_titulo``
http://localhost:8000/articulo/registros-de-articulos/?fin=fecha_limite_de_publicacion``
```

### `Registro de planes`
Debes entrar al siguiente endpoint:
Dentro de este endpoint se pueden filtrar los planes por su identificador
(recuerda que idplan es el identificador de cada plan creado)
```
http://localhost:8000/planes/registro-de-planes/?idplan=identificador_del_plan``
```

### `Registro de formas de pago`
```
http://localhost:8000/planes/registro-de-formas-de-pago/``
```

### `Consulta de Contratos`
Debes entrar al siguiente endpoint:
Dentro de este endpoint se pueden filtrar los contratos por su identificador, el identificador de la revista, el identificador de la forma de pago y la fecha en la que se inicio el contrato
(recuerda que idcontrato es el identificador de cada contrato, idrevista es el identificador de la revista a la que pertence el contrato, idpago es el identificador de la forma de pago establecida en el contrato, inicio es la fecha en la cual comenzara a correr el contrato)
```
http://localhost:8000/planes/registro-de-contratos/?idcontrato=identificador_de_contrato``
http://localhost:8000/planes/registro-de-contratos/?idrevista=identificador_de_la_revista``
http://localhost:8000/planes/registro-de-contratos/?idpago=identificador_de_la_forma_de_pago``
http://localhost:8000/planes/registro-de-contratos/?inicio=fecha_de_inicio_de_contrato``
```

### `Consulta de clientes`
Debes entrar al siguiente endpoint:
Dentro de este endpoint se pueden filtrar los clientes por su identificador o el identificador de la revista.
(recuerda que idcliente es el identificador de cada cliente, idrevista es el identificador de la revista a la que pertence)
````
http://localhost:8000/clientes/registros-de-clientes/?idcliente=identifiacador_de_cliente``
http://localhost:8000/clientes/registros-de-clientes/?idrevista=identificador_de_la_revista``
```

### `Endpoints pubicos`
Debes entrar al siguiente endpoint:
Dentro de estos endpoint se pueden filtrar de la misma manera que en los endpoints originales.
Cada endpoint tiene nombres relacionados con lo que hace cada uno.
(recuerda que cada tipo de endpoint tiene caracteristicas de filtrado diferentes)
````
http://localhost:8000/publicos``
```