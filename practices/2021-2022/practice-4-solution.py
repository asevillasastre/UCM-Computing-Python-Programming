class LineException(Exception):
    pass
class MetroException(Exception):
    pass

class Line(object):
    def __init__(self,estaciones,trayectos):
        self.estaciones=estaciones
        self.trayectos=trayectos
    def estaciones(self):
        return self.estaciones
    def contains_station(self,e):
        return e in self.estaciones
    def previous_e(self,e):
        if e not in self.estaciones:
            raise LineException("No existe la parada")
        else:
            if e==self.estaciones[0]:
                raise LineException("Es la primera parada")
            else:
                i=self.estaciones.index(e)
                return ("la parada anterior es "+self.estaciones[i-1])
    def next_e(self,e):
         if e not in self.estaciones:
             raise LineException("No existe la parada")
         else:
             if e==self.estaciones[-1]:
                 raise LineException("Es la última parada")
             else:
                 i=self.estaciones.index(e)
                 return ("la parada siguiente es "+self.estaciones[i+1])
             
    def cost_origin2destination(self,start, finish):
        if start not in self.estaciones or finish not in self.estaciones:
            raise LineException("No existe la linea")
        else:
            coste=0
            i=self.estaciones.index(start)
            j=self.estaciones.index(finish)
            k, l = min(i,j), max(i,j)
            for paradas in range(k,l):
                if self.estaciones[paradas][-13:] == " !!CERRADA!! ":
                    return None
                coste+=int(self.trayectos[paradas])
            return coste
    
    def __str__(self):
        cadena=''
        for i in range(len(self.estaciones)):
            cadena+=str(self.estaciones[i])+"->"
            if i < len(self.estaciones)-1:
                cadena += str(self.trayectos[i]) +"->"
        return cadena[:-2]

    def __repr__(self):
        cadena=''
        for i in range(len(self.estaciones)):
            cadena+=str(self.estaciones[i])+"->"
            if i < len(self.estaciones)-1:
                cadena += str(self.trayectos[i]) +"->"
        return cadena[:-2]
 
    def __hash__(self):
        return hash()
    
class Metro(object):
    def __init__(self):
        self.lineas={}
        self.transbordos={}   

    def add_line(self,line_name,line):
        if line_name in self.lineas.keys():
            raise MetroException("linea ya existente")
        else:  
            self.lineas[line_name]=line    
            self.add_connections(line_name,line)

    def add_connections(self,line_name,line):
        for nueva in line.estaciones:
            for linea in self.lineas.values():
                for existente in linea.estaciones:
                    if existente == nueva:
                        if existente not in self.transbordos.keys():
                            self.transbordos[existente]={line_name}
                        else:
                            self.transbordos[existente].add(line_name)
    
    @staticmethod
    def load_metro(file_name):
        metro = Metro()
        f = open(file_name, "r")
        f = f.readlines()
        i = 0
        for texto in f:
            if i%2==0:
                line_name = texto[:-1]
            else:
                estaciones, trayectos = [], []
                j = 0
                for elemento in texto[:-1].split("->"):
                    if j%2==0:
                        estaciones.append(elemento)
                    else:
                        trayectos.append(elemento)
                    j+=1
                line = Line(estaciones, trayectos)
                metro.add_line(line_name,line)
            i+=1
        return metro
    
    def __repr__(self):
        listo = []
        for linea in self.lineas.values():
            listo.append(linea.__str__())
        return(str(list(self.lineas)) + "\n"  + "\n" +  str(listo) + "\n" + "\n" + str(self.transbordos))

    def __str__(self):
        listo = []
        for linea in self.lineas.values():
            listo.append(linea.__str__())
        return(str(list(self.lineas)) + "\n"  + "\n" +  str(listo) + "\n" + "\n" + str(self.transbordos))
    
    def get_connections(self, e, line_name):
        error = True
        for linea in self.lineas.values():
            for existente in linea.estaciones:
                if existente == e:
                    error = False
        if error:
            raise MetroException("La estacion no esta en el plano")
        else:
            result = list(self.transbordos[e])
            result.remove(line_name)
            return result
    
    def cost_origin2destination_transfer(self, start, finish):
        errorstart = True
        errorfinish = True
        for linea in self.lineas.values():
            for existente in linea.estaciones:
                if existente == start or existente + " !!CERRADA!! " == start \
                or start + " !!CERRADA!! " == existente:
                    errorstart = False
                if existente == finish or existente + " !!CERRADA!! " == finish\
                or finish + " !!CERRADA!! " == existente:
                    errorfinish = False
        if errorstart:
            raise MetroException("No existe la parada de inicio")
        elif errorfinish:
            raise MetroException("No existe la parada de destino")
        else:
            startlines = list(self.transbordos[start])
            finishlines = list(self.transbordos[finish])
            posibles = []
            directa = False
            for inicial in startlines:
                try:
                    if type(self.lineas[inicial].cost_origin2destination(start, finish)) == int:
                        posibles.append(self.lineas[inicial].cost_origin2destination(start, finish))
                        directa = True
                except:
                    pass
            if directa:
                #print(posibles)
                return(min(posibles))
            for inicial in startlines:
                for final in finishlines:
                    for transbordo in self.transbordos:
                        if inicial in self.transbordos[transbordo] and final in self.transbordos[transbordo]:
                            try:
                                suma = self.lineas[inicial].cost_origin2destination(start, transbordo) +\
                                + 300 + self.lineas[final].cost_origin2destination(finish, transbordo)
                                #print(transbordo,suma)
                                posibles.append(suma)
                            except:
                                pass
            if posibles == []:
                return None
            else:
                return min(posibles)
    
    def close_station(self, line_name, e):
        errormetro = True
        for linea in self.lineas.values():
            for existente in linea.estaciones:
                if existente == e or existente + " !!CERRADA!! " == e \
                or e + " !!CERRADA!! " == existente:
                    errormetro= False
        if errormetro:
            raise MetroException("estacion no encontrada")
        errorlinea = True
        for existente in self.lineas[line_name].estaciones:
                if existente == e or existente + " !!CERRADA!! " == e \
                or e + " !!CERRADA!! " == existente:
                    errorlinea = False
        if errorlinea:
            raise LineException("estacion no perteneciente a esta linea")
        i = self.lineas[line_name].estaciones.index(e)
        if self.lineas[line_name].estaciones[i][-13:] != " !!CERRADA!! ":
            self.lineas[line_name].estaciones[i] += " !!CERRADA!! "
            for transbordo in self.transbordos:
                if transbordo == e:
                    self.transbordos[transbordo].remove(line_name)
        #print(self.lineas[line_name])
        
    def open_station(self, line_name, e):
        errormetro = True
        for linea in self.lineas.values():
            for existente in linea.estaciones:
                if existente == e or existente + " !!CERRADA!! " == e \
                or e + " !!CERRADA!! " == existente:
                    errormetro= False
        if errormetro:
            raise MetroException("estacion no encontrada")
        errorlinea = True
        for existente in self.lineas[line_name].estaciones:
                if existente == e or existente + " !!CERRADA!! " == e \
                or e + " !!CERRADA!! " == existente:
                    errorlinea = False
        if errorlinea:
            raise LineException("estacion no perteneciente a esta linea")
        i = self.lineas[line_name].estaciones.index(e + " !!CERRADA!! ")
        if self.lineas[line_name].estaciones[i][-13:] == " !!CERRADA!! ":
            self.lineas[line_name].estaciones[i] = self.lineas[line_name].estaciones[i][:-13]
            for transbordo in self.transbordos:
                if transbordo == e:
                    self.transbordos[transbordo].add(line_name)
        #print(self.lineas[line_name])
        
    def close_section(self, line_name, start, finish):
        errorstart = True
        errorfinish = True
        for  linea in self.lineas:
            for existente in self.lineas[linea].estaciones:
                if existente == start or existente + " !!CERRADA!! " == start \
                or start + " !!CERRADA!! " == existente:
                    errorstart = False
                if existente == finish or existente + " !!CERRADA!! " == finish\
                or finish + " !!CERRADA!! " == existente:
                    errorfinish = False
        if errorstart:
            raise MetroException("la parada de inicio no existe")
        elif errorfinish:
            raise MetroException("la parada de destino no existe")
        errorstart = True
        errorfinish = True
        for existente in self.lineas[line_name].estaciones:
            if existente == start or existente + " !!CERRADA!! " == start \
            or start + " !!CERRADA!! " == existente:
                errorstart = False
            if existente == finish or existente + " !!CERRADA!! " == finish\
            or finish + " !!CERRADA!! " == existente:
                errorfinish = False
        if errorstart:
            raise LineException("la parada de inicio no esta en esta linea")
        elif errorfinish:
            raise LineException("la parada de destino no esta en esta linea")
        for parada in self.lineas[line_name].estaciones:
            if parada[-13:] == " !!CERRADA!! ":
                return None
        i, j = self.lineas[line_name].estaciones.index(start), self.lineas[line_name].estaciones.index(finish)
        k, l = min(i + 1, j + 1), max(i, j)
        for estacion in self.lineas[line_name].estaciones:
            if self.lineas[line_name].estaciones.index(estacion) in range(k,l):
                self.close_station(line_name, estacion)
        #print(self.lineas[line_name])
        #print(self.transbordos)
        
    def open_section(self, line_name, start, finish):
        errorstart = True
        errorfinish = True
        for  linea in self.lineas:
            for existente in self.lineas[linea].estaciones:
                if existente == start or existente + " !!CERRADA!! " == start \
                or start + " !!CERRADA!! " == existente:
                    errorstart = False
                if existente == finish or existente + " !!CERRADA!! " == finish\
                or finish + " !!CERRADA!! " == existente:
                    errorfinish = False
        if errorstart:
            raise MetroException("la parada de inicio no existe")
        elif errorfinish:
            raise MetroException("la parada de destino no existe")
        errorstart = True
        errorfinish = True
        for existente in self.lineas[line_name].estaciones:
            if existente == start or existente + " !!CERRADA!! " == start \
            or start + " !!CERRADA!! " == existente:
                errorstart = False
            if existente == finish or existente + " !!CERRADA!! " == finish\
            or finish + " !!CERRADA!! " == existente:
                errorfinish = False
        if errorstart:
            raise LineException("la parada de inicio no esta en esta linea")
        elif errorfinish:
            raise LineException("la parada de destino no esta en esta linea")
        ningun_cortado = True
        for parada in self.lineas[line_name].estaciones:
            if parada[-13:] != " !!CERRADA!! ":
                ningun_cortado = False
                break
        if ningun_cortado:
            return None
        i, j= self.lineas[line_name].estaciones.index(start), self.lineas[line_name].estaciones.index(finish)
        k, l = min(i,j), max(i,j)
        for estacion in self.lineas[line_name].estaciones:
            if self.lineas[line_name].estaciones.index(estacion) in range(k,l+1):
                self.open_station(line_name, estacion)
        #print(self.lineas[line_name])
        #print(self.transbordos)

#metro = Metro()
#line1 = Line(['Bilbao','Tribunal','Gran Vía','Sol'], [130, 200, 150])
#metro.add_line("linea 1", line1)
#line2 = Line(['Bil','Tribu','Gran','Sol'], [130, 200, 150])
#metro.add_line("linea 2", line2)
#print(metro)
metro2 = Metro.load_metro("metro_costes_capada.txt")
#print(metro2)
#print(metro2.get_connections('Iglesia','Línea 1: Pinar de Chamartín - Valdecarros'))
#print(line1.cost_origin2destination("Sol", "Bilbao"))
#print(metro2.cost_origin2destination_transfer("Menéndez Pelayo", "Alonso Martínez"))
metro2.close_station("Línea 1: Pinar de Chamartín - Valdecarros", "Sol")
metro2.open_station("Línea 1: Pinar de Chamartín - Valdecarros", "Sol")
#metro2.close_section("Línea 1: Pinar de Chamartín - Valdecarros", "Cuatro Caminos", "Tribunal")
#metro2.open_section("Línea 1: Pinar de Chamartín - Valdecarros", "Cuatro Caminos", "Tribunal")
#print("********************************")
#print(metro2.cost_origin2destination_transfer("Cuatro Caminos", "Gran Vía"))
