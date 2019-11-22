# Instrucciones para uso del backend 🚀
## accounts 
### `Lista de usuarios`
Para hacer una consulta en la cual solo se podran saber los datos de los usuarios, se pueden filtrar estos usuarios con varios criterios como son nombre, apellido, username, revista o el tipo de usuario, para ello debera ingresar en la siguiente url, (recuerda que el username es el que se registro con la contraseña, el id de revista es el identificador de cada una de estas, el id de tipo de usuario variara segun el que se le asigne a cada usuario).
```
"nombre_servidor"/accounts/registro-perfiles/?nombre=username-o-nombre-o-apellido``
"nombre_servidor"/accounts/registro-perfiles/?idrevista=identificador_de_la_revista``
"nombre_servidor"/accounts/registro-perfiles/?idtipo=identificador_del_tipo_de_usuario``
```
### `Registro de usuarios`
Para hacer una consulta en la cual se podran revisar los datos de usuarios y ademas el ingreso de nuevos usuarios, en esta API se pueden filtrar por el id de cada usuario donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/accounts/Resgistro-de-usuario/identificador_del_usuario/``
```
### `Registro de perfiles`
Para hacer una consulta en la cual se podran revisar los datos de los perfiles de usuarios y ademas el ingreso de nuevos perfiles, en esta API se pueden filtrar por el id de cada perfil donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/accounts/Registro-de-perfiles/identificador_del_perfil/``
```
### `Registro de tipo_usuario`
Para hacer una consulta en la cual se podran revisar los datos de los tipos de usuarios y ademas el ingreso de nuevos tipos de usuarios, en esta API se pueden filtrar por el id de cada tipo de usuario donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/accounts/Resgistro-de-tipo_usuario/identificador_del_tipo_de_usuario/``
```
_____________________________________________________________________________________________________
## articulos
### `Lista de articulos`
Para hacer una consulta en la cual solo se podran saber los datos de los articulos, se pueden filtrar estos articulos con varios criterios como son categoria, subcategoria, revista, slug, la fecha en la que se termina el articulo(fin), la fecha en la que se inicio el articulo(inicio) o la validacion si esta en portada, la validacion del estado del articulo (publicado), para ello debera ingresar en la siguiente url, (recuerda que categoria se utiliza en base a su identificador, subcategoria se utiliza en base a su identificador, revista se utiliza en base a su identificador, slug se utiliza en base nombre modificado del articulo, fin se utiliza en base a la fecha en la cual se usara el formato aaaa-mm-dd, inicio se utiliza en base a la fecha en la cual se usara el formato aaaa-mm-dd, para la validacion si el articulo esta en portada se utilizaran los valores logicos True o False y para la validacion de estado (publicado) tambien se utilizaran valore logicos).
```
"nombre_servidor"/articulo/Lista-de-articulos/?slug=nombre-articulo``
"nombre_servidor"/articulo/Lista-de-articulos/?idrevista=identificador-de-la-revista``
"nombre_servidor"/articulo/Lista-de-articulos/?idcategoria=identificador-de-la-categoria``
"nombre_servidor"/articulo/Lista-de-articulos/?idsubcategoria=identificador-de-la-subcategoria``
"nombre_servidor"/articulo/Lista-de-articulos/?fin=aaaa-mm-dd``
"nombre_servidor"/articulo/Lista-de-articulos/?inicio=aaaa-mm-dd``
"nombre_servidor"/articulo/Lista-de-articulos/?portada=(True o False)``
"nombre_servidor"/articulo/Lista-de-articulos/?publicado=(True o False)``
```
### `Lista de articulos especiales`
Para hacer una consulta en la cual solo se podran saber los datos de los articulos especiales, se pueden filtrar estos articulos con varios criterios como son categoria, subcategoria, revista, slug, la validacion para saber si esta en portada(portada) o el estado del articulo(publicado), para ello debera ingresar en la siguiente url, (recuerda que categoria se utiliza en base a su identificador, subcategoria se utiliza en base a su identificador, revista se utiliza en base a su identificador, slug se utiliza en base nombre modificado del articulo, portada se utilizara en base a un valor booleano, status se basa en la validacion de si el articulo esta publicado o no con valores logicos).
```
"nombre_servidor"/articulo/Lista-de-especiales/?slug=nombre-articulo``
"nombre_servidor"/articulo/Lista-de-especiales/?idrevista=identificador-de-la-revista``
"nombre_servidor"/articulo/Lista-de-especiales/?idcategoria=identificador-de-la-categoria``
"nombre_servidor"/articulo/Lista-de-especiales/?idsubcategoria=identificador-de-la-subcategoria``
"nombre_servidor"/articulo/Lista-de-especiales/?portada=False-o-True(deben ser escritos de esta forma)``
"nombre_servidor"/articulo/Lista-de-especiales/?publicado=(True o False)``
```
### `Registro de articulo`
Para hacer una consulta en la cual se podran revisar los datos de los articulos y ademas el ingreso de nuevos articulos, en esta API se pueden filtrar por el id de cada articulo donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/articulo/Registro-de-articulos/identificador_del_articulo/``
```
### `Registro de iconos`
Para hacer una consulta en la cual se podran revisar los datos de los iconos y ademas el ingreso de nuevos iconos, en esta API se pueden filtrar por el id de cada icono donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/articulo/Registro-de-iconos/identificador_del_icono/``
```
_____________________________________________________________________________________________________
## contenido
### `Lista de Contenidos`
Para hacer una consulta en la cual solo se podran saber los datos de los contenidos, se pueden filtrar estos contenidos con varios criterios como son su identificador, el identificador del articulo al que pertenece o el tipo de contenido que es, para ello debera ingresar en la siguiente url, (recuerda que idcontenido se utilizara en base a su identificador, idarticulo se utilizara en base a el identificador del articulo al que pertenece dicho contenido y tipo pertenece a la seleccion hecha a traves del choice (Texto,Video,Imagen,Publicidad)).
```
"nombre_servidor"/contenido/Lista-de-Contenidos/?idarticulo=identificador-del-articulo``
"nombre_servidor"/contenido/Lista-de-Contenidos/?idcontenido=identificador-del-contenido``
"nombre_servidor"/contenido/Lista-de-Contenidos/?tipo=Texto o Video o Imagen o Publicidad``
```
### `Registro de Contenidos`
Para hacer una consulta en la cual se podran revisar los datos de los contenidos y ademas el ingreso de nuevos contenidos, en esta API se pueden filtrar por el id de cada publicidad donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/contenido/Registro-de-Contenidos/identificador_del_contenido/``
```
_____________________________________________________________________________________________________
## cotizador 
### `Registro de cotizaciones`
Para hacer una consulta en la cual se podran revisar los datos de ls cotizaciones y ademas el ingreso de nuevas cotizaciones, en esta API se pueden filtrar por el id de cada cotizacion donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/cotizacion/Registro-de-cotizaciones/identificador_de_cotizacion/``
```
_____________________________________________________________________________________________________
## patrocinadores
### `Lista de patrocinadores`
Para hacer una consulta en la cual solo se podran saber los datos de los patrocinadores, se pueden filtrar estos patrocinadores con varios criterios como son su identificados y el identificador de la revista a la que pertenece, para ello debera ingresar en la siguiente url, (recuerda que id patrocinador se utilizara en base a su identificador, idrevista se utilizara en base a el identificador de la revista.
```
"nombre_servidor"/patrocinadores/Lista-de-Patrocinadores/?idrevista=identificador-de-la-revista-de-pertenencia``
"nombre_servidor"/patrocinadores/Lista-de-Patrocinadores/?idpatrocinador=identificador-del-patrocinador``
```
### `Registro de patrocinadores`
Para hacer una consulta en la cual se podran revisar los datos de los patrocinadores y ademas el ingreso de nuevos patrocinadores, en esta API se pueden filtrar por el id de cada patrocinador donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/patrocinadores/Registro-de-Patrocinadores/identificador_del_articulo/``
```
_____________________________________________________________________________________________________
## planrevista
### `Lista de contratos`
Para hacer una consulta en la cual solo se podran saber los datos de los contratos, se pueden filtrar estos contratos con varios criterios como son su identificador, el identificador de la revista a la que pertenece, el identificador de la forma de pago(idpago), la fecha en la que inicio su contrato(inicio), para ello debera ingresar en la siguiente url, (recuerda que id del contrato se utilizara en base a su identificador, idrevista se utilizara en base a el identificador de la revista, idpago en base a el identificador de la forma de pago seleccionada y inicio en base a la fecha en la que inicio su contrato con el formato aaaa/mm/dd)
```
"nombre_servidor"/patrocinadores/Lista-de-Patrocinadores/?idcontrato=identificador-del-contrato``
"nombre_servidor"/patrocinadores/Lista-de-Patrocinadores/?idrevista=identificador-de-la-revista-de-pertenencia``
"nombre_servidor"/patrocinadores/Lista-de-Patrocinadores/?idpago=identificador-forma-de-pago``
"nombre_servidor"/patrocinadores/Lista-de-Patrocinadores/?inicio=aaaa-mm-dd``
```
### `Registro de planes`
Para hacer una consulta en la cual se podran revisar los datos de los planes y ademas el ingreso de nuevos planes, en esta API se pueden filtrar por el id de cada plan donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/planes/Registro-de-planes/identificador_del_plan/``
```
### `Registro de formas de pago`
Para hacer una consulta en la cual se podran revisar los datos de las formas de pago y ademas el ingreso de nuevas formas de pago, en esta API se pueden filtrar por el id de cada forma de pago donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/planes/Registro-de-formas-de-pago/identificador_de_la_forma_de_pago/``
```
### `Registro de contratos`
Para hacer una consulta en la cual se podran revisar los datos de los contratos y ademas el ingreso de nuevos contratos, en esta API se pueden filtrar por el id de cada contrato donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/planes/Registro-de-contratos/identificador_del_contrato/``
```
_____________________________________________________________________________________________________
## publicidad
### `Lista de publicidades`
Para hacer una consulta en la cual solo se podran saber los datos de las publicidades, se pueden filtrar estas publicidades con varios criterios como son su identificador o el identificador del patrocinador al que pertenece, para ello debera ingresar en la siguiente url, (recuerda que idpublicidad de la publicidad se utilizara en base a su identificador y idpatrocinador se utilizara en base a el identificador del patrocinador al que pertenece dicha publicidad).
```
"nombre_servidor"/publicidad/Lista-de-Publicidades/?idpublicidad=identificador-de-la-publicidad``
"nombre_servidor"/publicidad/Lista-de-Publicidades/?idpatrocinador=identificador-del-patrocinador``
```
### `Registro de publicidad`
Para hacer una consulta en la cual se podran revisar los datos de las publicidades y ademas el ingreso de nuevas publicidades, en esta API se pueden filtrar por el id de cada publicidad donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/publicidad/Registro-de-Publicidad/identificador_de_la_publicidad/``
```
_____________________________________________________________________________________________________
## regiones
### `Lista de estados`
Para hacer una consulta en la cual solo se podran saber los datos de los estados, se pueden filtrar estos estados con varios criterios como son su identificador, el identificador del pais al que pertenecen o el nombre del estado, para ello debera ingresar en la siguiente url, (recuerda que idestado se utilizara en base a su identificador, idpais se utilizara en base al identificador del pais al que pertence o nombre parcial o completo del estado).
```
"nombre_servidor"/regiones/Lista-de-estados/?idestado=identificador-del-estado``
"nombre_servidor"/regiones/Lista-de-estados/?idpais=identificador-del-pais-de-pertenencia``
"nombre_servidor"/regiones/Lista-de-estados/?nombre=nombre-estado``
```
### `Lista de ciudades`
Para hacer una consulta en la cual solo se podran saber los datos de las ciudades, se pueden filtrar estas ciudades con varios criterios como son su identificador, el identificador del estado al que pertenecen o el nombre de la ciudad, para ello debera ingresar en la siguiente url, (recuerda que idciudad se utilizara en base a su identificador, idestado se utilizara en base al identificador del estado al que pertence o el nombre parcial o completo de la ciudad).
```
"nombre_servidor"/regiones/Lista-de-ciudades/?idciudad=identificador-de-la-ciudad``
"nombre_servidor"/regiones/Lista-de-ciudades/?idestado=identificador-del-estado-de-pertenencia``
"nombre_servidor"/regiones/Lista-de-estados/?nombre=nombre-ciudad``
```
### `Registro de ciudades`
Para hacer una consulta en la cual se podran revisar los datos de las ciudades y ademas el ingreso de nuevas ciudades, en esta API se pueden filtrar por el id de cada ciudad donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/regiones/Registro-de-ciudades/identificador_de_la_ciudad/``
```
### `Registro de estados
Para hacer una consulta en la cual se podran revisar los datos de los estados y ademas el ingreso de nuevos estados, en esta API se pueden filtrar por el id de cada estado donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/regiones/Registro-de-estados/identificador_del_estado/``
```
### `Registro de paises`
Para hacer una consulta en la cual se podran revisar los datos de los paises y ademas el ingreso de nuevos paises, en esta API se pueden filtrar por el id de cada pais donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/regiones/Registro-de-paises/identificador_del_pais/``
```
_____________________________________________________________________________________________________
## revista
### `Lista de revistas`
Para hacer una consulta en la cual solo se podran saber los datos de las revistas, se pueden filtrar estas revistas con varios criterios como son su identificador, el identificador del pais al que pertenece, el identificador del estado al que pertenece, el identificador de la ciudad a la que pertenece, el identificador del plan contratado por la revista o el nombre de la revista, para ello debera ingresar en la siguiente url, (recuerda que idestado se utilizara en base a el identificador del estado, idpais se utilizara en base al identificador del pais al que pertence, idciudad se basa en el identificador de la ciudad, idrevista se basa en el identificador propio de la revista, idplan se basa en el identificador del plan contratado por la revista o por el nombre de la revista ya sea parcial o completo).
```
"nombre_servidor"/revista/Lista-de-revista/?idrevista=identificador-de-la-revista``
"nombre_servidor"/revista/Lista-de-revista/?idpais=identificador-del-pais``
"nombre_servidor"/revista/Lista-de-revista/?idestado=identificador-del-estado``
"nombre_servidor"/revista/Lista-de-revista/?idciudad=identificador-de-la-ciudad``
"nombre_servidor"/revista/Lista-de-revista/?idplan=identificador-del-plan``
"nombre_servidor"/revista/Lista-de-revista/?nombre=nombre-revista``
```
### `Lista de categorias`
Para hacer una consulta en la cual solo se podran saber los datos de las categorias, se pueden filtrar estas categorias con varios criterios como son su identificador, el identificador de la revista a la que pertenece o su nombre, para ello debera ingresar en la siguiente url, (recuerda que idcategoria se utilizara en base a su identificador, idrevista se utilizara en base al identificador de la revista a la que pertence y el nombre puede ser utilizado de forma parcial o completa).
```
"nombre_servidor"/revista/Lista-de-categoria/?idcategoria=identificador-de-la-categria``
"nombre_servidor"/revista/Lista-de-categoria/?idrevista=identificador-de-la-revista-de-pertenencia``
"nombre_servidor"/revista/Lista-de-revista/?nombre=nombre-categoria``
```
### `Lista de subcategorias`
Para hacer una consulta en la cual solo se podran saber los datos de las subcategorias, se pueden filtrar estas subcategorias con varios criterios como son su identificador, el identificador de la categoria a la que pertenecen o su nombre, para ello debera ingresar en la siguiente url, (recuerda que idsubcategoria se utilizara en base a su identificador, idcategoria se utilizara en base al identificador de la categoria a la que pertence y el nombre puede ser utilizado de forma parcial o completa).
```
"nombre_servidor"/revista/Lista-de-subcategorias/?idsubcategoria=identificador-de-la-subcategoria``
"nombre_servidor"/revista/Lista-de-subcategorias/?idcategoria=identificador-de-la-categoria``
"nombre_servidor"/revista/Lista-de-revista/?nombre=nombre-subcategoria``
```
### `Registro de revistas`
Para hacer una consulta en la cual se podran revisar los datos de las revistas y ademas el ingreso de nuevas revistas, en esta API se pueden filtrar por el id de cada revista donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/revista/Registro-de-revistas/identificador_de_la_revista/``
```
### `Registro de categorias
Para hacer una consulta en la cual se podran revisar los datos de las categorias y ademas el ingreso de nuevas categorias, en esta API se pueden filtrar por el id de cada categoria donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/revista/Registro-de-categorias/identificador_de_la_categoria/``
```
### `Registro de subcategorias
Para hacer una consulta en la cual se podran revisar los datos de las subcategorias y ademas el ingreso de nuevas subcategorias, en esta API se pueden filtrar por el id de cada subcategoria donde nos permitira hacer modificaciones y/o eliminaciones.
Para ello deberan ingresar a la siguiente url:
```
"nombre_servidor"/revista/Registro-de-subcategorias/identificador_de_la_subcategoria/``
```
_____________________________________________________________________________________________________
## publicos
### `Endpoints públicos`
Estos endpoints son solo de consulta en los cuales se habilitaran los modulos de reelevancia que no contengan informacion sensible de modo consulta, estos endpoint se pueden filtrar de la misma manera que en los endpoints originales.
Cada endpoint tiene nombres relacionados con lo que hace cada uno.
(recuerda que cada tipo de endpoint tiene caracteristicas de filtrado diferentes)
```
"nombre_servidor"/publicos``
```