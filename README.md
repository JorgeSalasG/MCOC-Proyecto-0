# MCOC-Proyecto-0
## Introducción
###### Para este proyecto se pide encontrar errores dado el tipo de dato ocupado, el cual surge del punto flotante, que varía según la cantidad de dígitos utilizados para nuestras operaciones.
## Ejemplo
###### El ejemplo presentado se basa en el resultado de la función f(x)=√(x^2+1)-x, ocurriendo una mayor perdida a medida que el valor de x aumenta, notándose una diferencia según la cantidad de dígitos de significancia que se utilizan. A continuación, se presenta gráficamente la variación del error a medida que aumenta el valor de x: 
![Grafico](https://github.com/JorgeSalasG/MCOC-Proyecto-0/blob/master/loss-of-significance.png)
###### Este error se produce al calcular la raíz del número, ya que utilizar menos dígitos (para dtype=32) el cálculo de la raíz cuadrada se vuele mas inexacto, siendo esta más inexacta a medida que el valor de x es mayor.
