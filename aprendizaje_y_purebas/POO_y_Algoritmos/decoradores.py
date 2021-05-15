
class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La {region} no es valida en {self._pais}')
    
    >>>> casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
    >>>>casilla.region
    None
    >>>>casilla.region = 'Ciudad de Mexico'
    >>>>casilla.region
    'Ciudad de Mexico'