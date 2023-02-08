
<h1 align="center"> Formula_1 </h1>

Creador: Vinicio Díaz 

*[Descripción del proyecto](#descripción-del-proyecto)
Proyecto final para el curso de Python de CoderHouse. En el siguiente proyecto se genera un modelo MVT, con temática libre, en este caso se eligio 
de Formula 1. La finalidad del Proyecto es realizar una página de internet en la cual puedas acceder y leer noticias relevantes acerca del deporte, se
tienen listados actualizados sobre los pilotos, las escuderias y los circuitos para la Temporada 2023. Tambien hay un link con una tienda en la cual se ofertaran productos de todas las escuederias. 


*[Estado del proyecto](#Estado-del-proyecto)

<h4 align="center">
:construction: Proyecto en construcción :construction:
</h4>


*[Características de la aplicación y demostración](#Características-de-la-aplicación-y-demostración)
Funcionalidades del Proyecto 

Al momento de tener descargado el repositorio y poder acceder a él. Lo primero que nos encontramos es una página genérica con dos opciones:
 
      1.- /admin/ : Directamente abre el administrador de Django que cuenta hasta este momento con dos usuarios, un superadmin que es capaz de crear,
      borrar y  modificar variables dentro del administrador y mediante formularios generados desde la base de datos. Y el segundo usuario es para 
      cualquier persona que guste acceder para mirar el proyecto y únicamente tiene permisos para ver la apliación, no puede añadir nada.
      
      2./Formula_1/: Esta URL nos lleva directamente al Indice del Proyecto en cuestión y nos despliega un menú en el cual encontraremos diferentes URL 
      a las cuales podremos viajar para crear pilotos, escuderias y circuitos; de igual manera se encuentran las URLs que nos llevarán al listado de los
      pilotos, escuderias, circuitos creados. Se añadió una NavBar desde la cual podremos viajar de un listado a otro ya que se encuentrán enlazados 
      mediante un HTML Base que hereda la configuración de la NavBar. Por último, se agrego un menú desplegable correspondiente a la Temporada 2022
      que cuenta con Herencia del HTML Base y en el cual se despliegan dos menús en los cuales podremos visualizar la Tabla de Posiciones del campeonato
      de Pilotos y Constructores.
      
      3.-/Tienda/: Esta URL nos lleva directamente a una página para logearse, ya que al ser una tienda en la que se añadiran metodos de pago, se podrá           comprar mercancía, es necesario tener identificada a la persona que entra. Posterior al login, nos encontramos con un listado de productos. Si la 
      persona que se loguea es un usuario administrador, este podrá ser capaz de elimar, crear, modificar y visualizar si existe stock en el producto 
      ofrecido.
      
      4.-/Usuarios/: Por último nos encontramos en la última URL, la funcionalidad de está URL es para crear templates en los cuales se muestran 
      formularios para registrarse, loguearse y modificar perfiles de usuario, se puede modificar foto de perfil, telefono, correo, nombre de usuario
      entre otras cosas.
      
      
      
*[Acceso al proyecto](#acceso-proyecto)

Para acceder al repositorio es necesario descargarlo en el editor de código de preferencia con el siguiente comando: "Git Clone" y agregamos el
enlace de GitHub: https://github.com/VinicioDiaz/Proyecto_final.git. El repositorio está público por lo cual está descargable para cualquier persona. 

*[Conclusiones](#conclusiones)

Al ser un proyecto en construcción, queda mucho trabajo por hacer. A la fecha de Febrero 2023 el proyecto es capaz de generar Usuarios mediante un formulario, crear. modificar y eliminar mediante un CRUD pilotos, circuitos y escuderías, así como visualizar los listados de los mismo desde una NavBar.
En esta altura del proyecto, la página es completamente funcional y el siguiente pasó será darle un look mucho mejor con el uso de HTML + CSS. Espero la página sea de su agrado y estén al pendiente de las siguientes actualizaciones.

Saludos!!!!


