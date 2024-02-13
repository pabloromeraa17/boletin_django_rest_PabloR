Endpoints Principales  
patinetes/usuarios/: Endpoint para gestionar usuarios.  
patinetes/patinetes/: Endpoint para gestionar patinetes.  
patinetes/alquileres/: Endpoint para gestionar alquileres.  

Endpoints Secundarios
Alquilar un Patinete URL: /alquileres/alquilar/ Método: POST Datos requeridos: patinete_id: ID del patinete que deseas alquilar.

Liberar un Patinete URL: /alquileres/liberar/ Método: POST Datos requeridos: patinete_id: ID del patinete que deseas liberar.

Listar Alquileres (Solo Administradores) URL: /alquileres/alquileres_admin/ Método: GET

Listar Alquileres del Usuario Actual URL: /alquileres/alquileres_usuario/ Método: GET

Listar Patinetes Libres URL: /patinetes/patinetes_libres/ Método: GET

Listar Patinetes Ocupados URL: /patinetes/patinetes_ocupados/ Método: GET

Listar Usuarios por Débito URL: /usuarios/usuarios_por_debito/ Método: GET

Top Ten de Patinetes Alquilados URL: /patinetes/top_ten_patinetes_alquilados/ Método: GET

Top 3 de Usuarios en Número de Alquileres URL: /usuarios/top_tres_usuarios_alquileres/ Método: GET

Top 3 de Usuarios en Número de Débito URL: /usuarios/top_tres_usuarios_debito/ Método: GET