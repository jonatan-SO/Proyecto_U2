class ValidarFecha:

    _Anio = int(0)
    _Dia  = int(0)
    _Mes  = int(0)



    def __init__(self,Dia, Mes, Anio ):
        self._Anio = Anio
        self._Dia  = Dia
        self._Mes  = Mes
        self.Validacion()


    def Validacion(self):

        if(( self._Dia < 31 and self._Dia >0) and (self._Mes < 13 and self._Mes>0 ) and (self._Anio > 1)):
            return 1
            #print(f'La fecha {self._Dia}/{self._Mes}/{self._Anio} es correcta')
        else:
            return 0
            #print(f'La fecha {self._Dia}/{self._Mes}/{self._Anio} es incorrecta')



    def  getfecha(self):
       if(self.Validacion()== True):
          return self.Validacion()

       elif(self.Validacion()==False):
          return self.Validacion()


