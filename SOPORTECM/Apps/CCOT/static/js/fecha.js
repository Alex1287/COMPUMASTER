n =  new Date();
//Año
y = n.getFullYear();
//Mes
m = n.getMonth() + 1;
//Día
d = n.getDate();

//Lo ordenas a gusto.
document.getElementById("date").innerHTML = y;
