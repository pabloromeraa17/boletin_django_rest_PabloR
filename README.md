# boletin_django_rest_PabloR  
Actividad número 1 del boletín de Django Rest  
$ python ./manage.py spectacular --color --file schema.yml  
$ docker run -p 80:8080 -e SWAGGER_JSON=/schema.yml -v ${PWD}/schema.yml:/schema.yml swaggerapi/swagger-ui  

- Listar todas las marcas y crear una nueva marca:
  - GET /marcas/: Listar todas las marcas  
  - POST /marcas/: Crear una nueva marca  

- Obtener detalles, actualizar y eliminar una marca específica:
  - GET /marcas/{id}/: Obtener detalles de una marca específica  
  - PUT /marcas/{id}/: Actualizar una marca específica  
  - DELETE /marcas/{id}/: Eliminar una marca específica  

- Listar todos los vehículos y crear un nuevo vehículo:
  - GET /vehiculos/: Listar todos los vehículos  
  - POST /vehiculos/: Crear un nuevo vehículo  

- Obtener detalles, actualizar y eliminar un vehículo específico:
    - GET /vehiculos/{id}/: Obtener detalles de un vehículo específico  
    - PUT /vehiculos/{id}/: Actualizar un vehículo específico  
    - DELETE /vehiculos/{id}/: Eliminar un vehículo específico  
- Filtrar vehículos por marca:  
  - GET /vehiculos/?marca={marca_id}: Filtrar vehículos por marca  

- Ordenar vehículos por fecha de fabricación:
  - GET /vehiculos/?ordering=fecha_fabricacion: Ordenar vehículos por fecha de fabricación (ascendente)
  - GET /vehiculos/?ordering=-fecha_fabricacion: Ordenar vehículos por fecha de fabricación (descendente)
